// Focused local HTML/SVG proof. No external requests, credentials or browser profile.
import { createRequire } from 'node:module';
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
const require = createRequire(import.meta.url);
const { chromium } = require('C:/Users/benja/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const [sourceArg, outputArg, kind = 'static', widthArg = '1440'] = process.argv.slice(2);
if (!sourceArg || !outputArg) throw new Error('source and new output directory required');
const source = path.resolve(sourceArg), output = path.resolve(outputArg);
if (fs.existsSync(output)) throw new Error('Refusing to overwrite a proof directory');
fs.mkdirSync(output, { recursive: true });
const browser = await chromium.launch({ headless: true });
const observations = { source, kind, browser: browser.version(), screens: [], errors: [], blockedRequests: [] };
try {
  for (const width of [...new Set([Number(widthArg), ...(kind === 'static' ? [390] : [])])]) {
    const context = await browser.newContext({ viewport: { width, height: 900 }, serviceWorkers: 'block', ...(kind === 'motion' ? { recordVideo: { dir: output, size: { width, height: 900 } } } : {}) });
    await context.route(/https?:\/\//, route => { observations.blockedRequests.push(route.request().url()); return route.abort(); });
    const page = await context.newPage();
    page.on('pageerror', error => observations.errors.push(error.message));
    await page.goto(pathToFileURL(source).href);
    await page.evaluate(() => document.fonts.ready);
    const inspect = () => page.evaluate(() => ({ title: document.title, text: document.body.innerText, width: innerWidth, scrollWidth: document.documentElement.scrollWidth, fixedGroups: ['pack-fixed', 'sign-fixed'].map(id => ({ id, html: document.getElementById(id)?.outerHTML ?? null })), elements: [...document.querySelectorAll('h1,h2,p,button,svg text,.copy')].map(el => ({ tag: el.tagName, text: el.textContent, bounds: { x: el.getBoundingClientRect().x, y: el.getBoundingClientRect().y, width: el.getBoundingClientRect().width, height: el.getBoundingClientRect().height }, fontSize: getComputedStyle(el).fontSize, lineHeight: getComputedStyle(el).lineHeight })), animations: document.getAnimations().map(a => ({ playState: a.playState, currentTime: a.currentTime, timing: a.effect?.getTiming() })) }));
    if (kind === 'motion') {
      await page.waitForTimeout(1100);
      observations.before = await inspect();
      await page.screenshot({ path: path.join(output, 'before.png'), fullPage: true });
      const control = page.getByRole('button', { name: 'Advance sample', exact: true });
      if (await control.count() !== 1) throw new Error('The required exact Advance sample control is absent or ambiguous');
      const start = Date.now();
      await control.click();
      for (const target of [100, 400, 1000]) {
        await page.waitForTimeout(Math.max(0, start + target - Date.now()));
        const frame = { targetMs: target, observedMs: Date.now() - start, state: await inspect() };
        observations.screens.push(frame);
        await page.screenshot({ path: path.join(output, `motion-${target}.png`), fullPage: true });
      }
      await page.emulateMedia({ reducedMotion: 'reduce' });
      await page.reload();
      await page.getByRole('button', { name: 'Advance sample', exact: true }).click();
      await page.waitForTimeout(100);
      observations.reducedMotion = await inspect();
      await page.screenshot({ path: path.join(output, 'reduced-motion.png'), fullPage: true });
    } else {
      observations.screens.push(await inspect());
      await page.screenshot({ path: path.join(output, `screen-${width}.png`), fullPage: true });
    }
    await context.close();
  }
} catch (error) { observations.errors.push(error.stack); process.exitCode = 1; }
finally { await browser.close(); fs.writeFileSync(path.join(output, 'observations.json'), JSON.stringify(observations, null, 2) + '\n'); }
console.log(JSON.stringify({ output, browser: observations.browser, errors: observations.errors, screens: observations.screens.length }));
