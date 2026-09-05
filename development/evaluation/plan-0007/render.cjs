// Local, network-blocked artifact capture. This is not a Playwright test suite.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const {pathToFileURL} = require('url');
const {chromium} = require('C:/Users/benja/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root = process.argv[2] || 'Z:/Projekts/AI/output/design-plan7-trials';
const out = 'Z:/Projekts/AI/output/playwright/design-plan7';
const sha = x => crypto.createHash('sha256').update(x).digest('hex');
const write = (p,x) => fs.writeFileSync(p,JSON.stringify(x,null,2)+'\n',{flag:'wx'});
(async()=>{
  fs.mkdirSync(out,{recursive:true});
  const browser = await chromium.launch({channel:'chrome',headless:true});
  const captures=[];
  for(const family of fs.readdirSync(root).filter(n=>n.startsWith('PG-'))){
    for(const arm of fs.readdirSync(path.join(root,family)).filter(n=>fs.statSync(path.join(root,family,n)).isDirectory())){
      for(const file of ['main.html','control.html']){
        const source=path.join(root,family,arm,file); if(!fs.existsSync(source))continue;
        const bytes=fs.readFileSync(source); const label='V'+sha(source+'|'+sha(bytes)).slice(0,10);
        const receipt=path.join(out,label+'.json'); if(fs.existsSync(receipt))continue;
        const sizes=family==='PG-01'?[720]:family==='PG-02'?[760]:family==='PG-T1'?[360,720,1000]:family==='PG-09'?[360,720,1200]:[1200];
        const entry={label,family,arm,file,source,source_sha256:sha(bytes),chrome:browser.version(),captures:[],errors:[]};
        const context=await browser.newContext({viewport:{width:sizes[0],height:900},deviceScaleFactor:1,recordVideo:family==='PG-11'?{dir:path.join(out,label+'-video'),size:{width:1200,height:900}}:undefined});
        await context.route(/^https?:/,r=>r.abort());
        const page=await context.newPage(); page.on('pageerror',e=>entry.errors.push(String(e)));
        for(const width of sizes){
          await page.setViewportSize({width,height:900}); await page.goto(pathToFileURL(source).href); await page.evaluate(()=>document.fonts.ready); await page.waitForTimeout(100);
          const name=label+'-'+width+'.png'; await page.screenshot({path:path.join(out,name),fullPage:true});
          const dom=await page.evaluate(()=>({text:document.body.innerText,scrollWidth:document.documentElement.scrollWidth,clientWidth:document.documentElement.clientWidth,height:document.documentElement.scrollHeight,fonts:[...document.fonts].map(f=>({family:f.family,status:f.status})),textBoxes:[...document.querySelectorAll('h1,h2,h3,p,li,td,th,figcaption,svg text')].map(e=>{const r=e.getBoundingClientRect(),s=getComputedStyle(e);return {text:e.textContent,x:r.x,y:r.y,width:r.width,height:r.height,font:s.fontFamily,size:s.fontSize,colour:s.color,display:s.display};})}));
          entry.captures.push({width,image:name,dom});
          if(family==='PG-02'){
            const cdp=await context.newCDPSession(page); await cdp.send('DOM.enable'); await cdp.send('CSS.enable');
            const {root:doc}=await cdp.send('DOM.getDocument'); const {nodeIds}=await cdp.send('DOM.querySelectorAll',{nodeId:doc.nodeId,selector:'p,td,span'}); entry.actual_fonts=[];
            for(const nodeId of nodeIds.slice(0,60)){try{entry.actual_fonts.push({nodeId,...await cdp.send('CSS.getPlatformFontsForNode',{nodeId})});}catch(e){entry.errors.push(String(e));}}
          }
        }
        if(family==='PG-11' && file==='main.html'){
          entry.playback=[];
          for(const id of ['replay-status','replay-story']){
            const button=page.locator('#'+id);
            if(await button.count()!==1){entry.errors.push('Missing exact replay id '+id);continue;}
            await button.click();
            for(const ms of [80,220,700,1600]){
              await page.waitForTimeout(ms); const name=label+'-'+id+'-'+ms+'.png'; await page.screenshot({path:path.join(out,name),fullPage:true});
              entry.playback.push({id,additional_elapsed_ms:ms,image:name,state:await page.evaluate(()=>({text:document.body.innerText,animations:document.getAnimations().map(a=>({time:a.currentTime,playState:a.playState,duration:a.effect?.getTiming().duration}))}))});
            }
          }
          const status=page.locator('#replay-status'); if(await status.count()===1){await status.click();await page.waitForTimeout(50);await status.click();await page.waitForTimeout(2000);entry.interrupted_text=await page.innerText('body');}
          await page.emulateMedia({reducedMotion:'reduce'}); await page.reload(); await page.waitForTimeout(300);
          const button=page.locator('#replay-story');if(await button.count()===1)await button.click();await page.waitForTimeout(300);
          await page.screenshot({path:path.join(out,label+'-reduced.png'),fullPage:true});
          entry.reduced={text:await page.innerText('body'),image:label+'-reduced.png',animations:await page.evaluate(()=>document.getAnimations().map(a=>a.playState))};
        }
        await context.close(); write(receipt,entry); captures.push({label,family,arm,file,errors:entry.errors});
      }
    }
  }
  await browser.close(); console.log(JSON.stringify({chrome:browser.version(),captured:captures}));
})().catch(e=>{console.error(e);process.exitCode=1;});
