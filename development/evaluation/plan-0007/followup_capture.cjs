// Bounded diagnostics and interaction proof; original artifacts/receipts stay intact.
const fs=require('fs'), path=require('path'), crypto=require('crypto');
const {pathToFileURL}=require('url');
const {chromium}=require('C:/Users/benja/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root='Z:/Projekts/AI/output/design-plan7-trials', out='Z:/Projekts/AI/output/playwright/design-plan7/followup-v2';
const hash=x=>crypto.createHash('sha256').update(x).digest('hex');
(async()=>{
 fs.mkdirSync(out,{recursive:true});
 const browser=await chromium.launch({channel:'chrome',headless:true});
 const record={chrome:browser.version(),repairs:[],interactions:[],motion:[]};
 const context=await browser.newContext({viewport:{width:1200,height:1200},reducedMotion:'no-preference'});
 await context.route(/^https?:/,r=>r.abort());
 const page=await context.newPage();
 const source=path.join(root,'PG-06/candidate/control.html'), original=fs.readFileSync(source,'utf8');
 const needle='.baseline{stroke:#768783;stroke-width:1.5}';
 if(original.split(needle).length!==2)throw Error('Expected exact axis rule');
 const repaired=original.replace(needle,'.baseline{fill:none;stroke:#768783;stroke-width:1.5}');
 const dest=path.join(out,'PG-06-control-host-repair.html');fs.writeFileSync(dest,repaired,{flag:'wx'});
 await page.goto(pathToFileURL(dest).href);await page.screenshot({path:path.join(out,'PG-06-control-host-repair.png')});
 record.repairs.push({original:source,original_sha256:hash(original),repaired:dest,repaired_sha256:hash(repaired),actor:'coordinator',change:'Only fill:none on the L-shaped SVG axis path. Original model artifact failed render; no model rerun or new Skill instruction.',computed_fill:await page.locator('.baseline').evaluate(e=>getComputedStyle(e).fill)});
 for(const arm of ['baseline','candidate']){
  await page.goto(pathToFileURL(path.join(root,'PG-09',arm,'main.html')).href);
  await page.setViewportSize({width:360,height:1000});
  await page.locator('.action').first().click();
  const row=page.locator('.repair').first();
  const input=row.locator('[name="object"]');
  const before=await input.inputValue();await input.fill('Desk lamp - preview');
  await row.locator('button[type="submit"]').click();
  const after=await row.innerText();
  await page.screenshot({path:path.join(out,'PG-09-'+arm+'-edited.png'),fullPage:true});
  await page.reload();
  record.interactions.push({case:'PG-09',arm,before,after,reloaded:await page.locator('.repair').first().innerText()});
 }
 await page.goto(pathToFileURL(path.join(root,'PG-13/candidate/main.html')).href);await page.setViewportSize({width:1200,height:1200});
 const before=await page.locator('#answer').isVisible();await page.locator('#reveal').click();
 record.interactions.push({case:'PG-13',answer_visible_before:before,answer_visible_after:await page.locator('#answer').isVisible(),answer:await page.locator('#answer').innerText()});
 await page.screenshot({path:path.join(out,'PG-13-revealed.png')});
 for(const arm of ['baseline','candidate']){
  await page.emulateMedia({reducedMotion:'no-preference'});
  await page.goto(pathToFileURL(path.join(root,'PG-11',arm,'main.html')).href);
  await page.waitForTimeout(200);
  const selector=arm==='baseline'?'#status-label':'#status-text';
  await page.locator('#replay-status').click();
  const states=[];
  for(const ms of [100,850,400]){
   await page.waitForTimeout(ms);states.push({additional_ms:ms,text:await page.locator(selector).innerText(),animations:await page.evaluate(()=>document.getAnimations().map(a=>({state:a.playState,time:a.currentTime}))) });
   await page.screenshot({path:path.join(out,'PG-11-'+arm+'-status-'+ms+'.png')});
  }
  await page.locator('#replay-status').click();await page.waitForTimeout(50);await page.locator('#replay-status').click();
  const interrupted=await page.locator(selector).innerText();
  await page.emulateMedia({reducedMotion:'reduce'});await page.locator('#replay-status').click();await page.waitForTimeout(1200);
  record.motion.push({arm,viewport:{width:1200,height:1200},states,interrupted,reduced_status:await page.locator(selector).innerText(),animations:await page.evaluate(()=>document.getAnimations().map(a=>a.playState))});
 }
 await browser.close();fs.writeFileSync(path.join(out,'receipt.json'),JSON.stringify(record,null,2)+'\n',{flag:'wx'});console.log(JSON.stringify(record));
})().catch(e=>{console.error(e);process.exitCode=1;});
