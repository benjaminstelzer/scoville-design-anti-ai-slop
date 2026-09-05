// Supplementary observed return/retrigger states, identical for both arms.
import { createRequire } from 'node:module';
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
const require = createRequire(import.meta.url);
const { chromium } = require('C:/Users/benja/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const [sourceArg, outputArg] = process.argv.slice(2);
const source = path.resolve(sourceArg), output = path.resolve(outputArg);
if (fs.existsSync(output)) throw new Error('Refusing to overwrite probe');
fs.mkdirSync(output);
const browser = await chromium.launch({ headless: true });
const result = { browser: browser.version(), source, states: [], errors: [], blockedRequests: [] };
try {
  const context = await browser.newContext({ viewport: { width: 1000, height: 900 }, serviceWorkers: 'block' });
  await context.route(/https?:\/\//, route => { result.blockedRequests.push(route.request().url()); return route.abort(); });
  const page = await context.newPage();
  page.on('pageerror', error => result.errors.push(error.message));
  await page.goto(pathToFileURL(source).href);
  await page.evaluate(() => document.fonts.ready);
  result.data = await page.evaluate(() => ({ samples, capacity }));
  const snapshot = async name => {
    result.states.push({ name, ...(await page.evaluate(() => ({ sample: document.querySelector('#sample')?.textContent, text: document.body.innerText, width: innerWidth, scrollWidth: document.documentElement.scrollWidth, animations: document.getAnimations().map(a => ({ state: a.playState, time: a.currentTime })), focused: document.activeElement?.id }))) });
    await page.screenshot({ path: path.join(output, name + '.png'), fullPage: true });
  };
  const advance = page.getByRole('button', { name: 'Advance sample', exact: true });
  await advance.click();
  await page.waitForTimeout(900);
  await advance.click();
  await page.waitForTimeout(900);
  await snapshot('return-sample-1');
  for (let i = 0; i < 3; i++) { await advance.click(); await page.waitForTimeout(70); }
  await page.waitForTimeout(900);
  await snapshot('retrigger-final-sample-2');
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.reload();
  await advance.click();
  await page.waitForTimeout(100);
  await snapshot('reduced-sample-2');
  await advance.click();
  await page.waitForTimeout(100);
  await snapshot('reduced-return-sample-1');
  await advance.focus();
  await page.keyboard.press('Enter');
  await snapshot('keyboard-enter-sample-2');
  await page.setViewportSize({ width: 390, height: 900 });
  await snapshot('narrow-selected-sample-2');
  await context.close();
} catch (error) { result.errors.push(error.stack); process.exitCode = 1; }
finally { await browser.close(); fs.writeFileSync(path.join(output, 'observations.json'), JSON.stringify(result, null, 2) + '\n'); }
console.log(JSON.stringify({ output, data: result.data, states: result.states.map(s => ({ name:s.name, sample:s.sample, width:s.width, scrollWidth:s.scrollWidth, animations:s.animations })), errors:result.errors }));
