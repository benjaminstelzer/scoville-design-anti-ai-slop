const fs=require('fs'),path=require('path'),crypto=require('crypto'),assert=require('assert');
const {pathToFileURL}=require('url');
const {chromium}=require('C:/Users/benja/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root='Z:/Projekts/AI/output/design-plan8-supplements',out='Z:/Projekts/AI/output/playwright/design-plan8';
const hash=x=>crypto.createHash('sha256').update(x).digest('hex');
const paragraph='A repaired object keeps more than its material. It carries the marks of ordinary use, the decisions of its makers, and the patience of the people who kept it working. The archive records these traces without pretending that every object tells the same story.';
(async()=>{
 fs.mkdirSync(out,{recursive:true});
 const browser=await chromium.launch({channel:'chrome',headless:true});
 const context=await browser.newContext({viewport:{width:1600,height:1200}});
 await context.route(/^https?:/,r=>r.abort());
 const page=await context.newPage();
 const record={chrome:browser.version(),network:'external requests blocked',artifacts:[],motion:[]};
 const mode=process.argv[2];
 if(mode==='motion'){
  const source='Z:/Projekts/AI/output/design-plan7-trials/PG-11/candidate/main.html',original=fs.readFileSync(source,'utf8');
  const needle='A clear signal to continue.';assert.equal(original.split(needle).length,2);
  const fixed=original.replace(needle,'Status of the current step.');
  const dest=path.join(root,'PG-11-coordinator-derivative.html');
  fs.writeFileSync(dest,fixed,{flag:'wx'});
  record.derivative={source,source_sha256:hash(original),destination:dest,sha256:hash(fixed),actor:'coordinator',change:'One neutral subtitle substitution; original HTML, raw answer and behavior preserved.'};
  await page.setViewportSize({width:1200,height:1200});
  await page.goto(pathToFileURL(dest).href);await page.waitForTimeout(150);
  async function capture(label,expected){
   const state=await page.locator('#status-stage').evaluate(e=>({state:e.dataset.state,title:e.querySelector('#status-text').textContent,subtitle:e.querySelector('.state-subtitle').textContent,animations:document.getAnimations().map(a=>a.playState)}));
   assert.equal(state.title,expected);assert.equal(state.state,expected.toLowerCase());assert.equal(state.subtitle,'Status of the current step.');
   await page.screenshot({path:path.join(out,label+'.png')});record.motion.push({label,...state});
  }
  await capture('initial-ready','Ready');
  await page.locator('#replay-status').click();await page.waitForTimeout(100);await capture('waiting','Waiting');
  await page.waitForTimeout(1200);await capture('ready','Ready');
  await page.locator('#replay-status').click();await page.waitForTimeout(80);await page.locator('#replay-status').click();await capture('interrupted','Ready');
  await page.emulateMedia({reducedMotion:'reduce'});await page.locator('#replay-status').click();await page.waitForTimeout(100);await capture('reduced-waiting','Waiting');
  await page.waitForTimeout(1200);await capture('reduced-ready','Ready');assert.equal(record.motion.at(-1).animations.length,0);
 }else{
  for(const [id,arm] of [['PG-02S','baseline'],['PG-02S','candidate'],['PG-08S','candidate']]){
   for(const name of ['main','control']){
    const file=path.join(root,id,arm,name+'.html');
    await page.goto(pathToFileURL(file).href);await page.evaluate(()=>document.fonts.ready);
    const entry={id,arm,name,path:file,sha256:hash(fs.readFileSync(file)),pageErrors:[],text:await page.locator('body').innerText()};
    if(id==='PG-02S'&&name==='main'){
     entry.specimens=await page.locator('[data-specimen]').evaluateAll(es=>es.map(e=>{
      const c=getComputedStyle(e),rect=e.getBoundingClientRect();return {id:e.dataset.specimen,width:rect.width,font:c.fontFamily,size:c.fontSize,leading:c.lineHeight,paragraphs:[...e.querySelectorAll('p')].map(p=>({text:p.textContent,width:p.getBoundingClientRect().width,height:p.getBoundingClientRect().height}))};
     }));
     assert.equal(entry.specimens.length,3);
     for(const s of entry.specimens){assert.equal(s.paragraphs.length,2);assert.equal(s.size,'18px');for(const p of s.paragraphs)assert.equal(p.text,paragraph);assert.equal(s.width,s.id==='original'?648:432);if(s.id!=='selected')assert.equal(s.leading,'29px');}
     const cdp=await context.newCDPSession(page);await cdp.send('DOM.enable');await cdp.send('CSS.enable');
     const doc=await cdp.send('DOM.getDocument');const nodes=await cdp.send('DOM.querySelectorAll',{nodeId:doc.root.nodeId,selector:'[data-specimen] p'});
     entry.actualFonts=[];for(const nodeId of nodes.nodeIds)entry.actualFonts.push(await cdp.send('CSS.getPlatformFontsForNode',{nodeId}));await cdp.detach();
    }
    if(id==='PG-08S'&&name==='main'){
     entry.maps=await page.locator('svg').evaluateAll(es=>es.filter(e=>e.querySelector('[data-feature]')).map(e=>({viewBox:e.getAttribute('viewBox'),width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height,features:[...e.querySelectorAll('[data-feature]')].map(f=>({id:f.dataset.feature,tag:f.tagName,attrs:Object.fromEntries([...f.attributes].map(a=>[a.name,a.value]))})),labels:[...e.querySelectorAll('text')].map(t=>({text:t.textContent,rect:{x:t.getBoundingClientRect().x,y:t.getBoundingClientRect().y,width:t.getBoundingClientRect().width,height:t.getBoundingClientRect().height}}))})));
     assert.equal(entry.maps.length,2);assert.deepEqual(entry.maps.map(m=>m.width),[600,300]);
     for(const m of entry.maps){assert.equal(m.viewBox,'0 0 100 100');assert.equal(m.features.length,4);for(const text of ['Willow Brook','Orchard','Long Meadow','Depot'])assert(m.labels.some(t=>t.text.trim()===text));}
     const geom=m=>m.features.map(f=>({id:f.id,tag:f.tag,d:f.attrs.d,points:f.attrs.points,cx:f.attrs.cx,cy:f.attrs.cy}));
     assert.deepEqual(geom(entry.maps[0]),geom(entry.maps[1]));
    }
    const screenshot=path.join(out,id+'-'+arm+'-'+name+'.png');await page.screenshot({path:screenshot,fullPage:true});entry.screenshot=screenshot;record.artifacts.push(entry);
   }
  }
 }
 await browser.close();fs.writeFileSync(path.join(out,(mode==='motion'?'motion':'supplements')+'-receipt.json'),JSON.stringify(record,null,2)+'\n',{flag:'wx'});console.log(JSON.stringify({mode,artifacts:record.artifacts.length,motion:record.motion.length}));
})().catch(e=>{console.error(e);process.exitCode=1;});
