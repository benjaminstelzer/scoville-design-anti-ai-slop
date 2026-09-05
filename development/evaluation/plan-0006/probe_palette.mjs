// Verify that SVG derivatives actually follow their declared CSS palette owner.
import { createRequire } from 'node:module';
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
const require=createRequire(import.meta.url);
const {chromium}=require('C:/Users/benja/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const [sourceArg,outputArg]=process.argv.slice(2);
const source=path.resolve(sourceArg),output=path.resolve(outputArg);
if(fs.existsSync(output))throw new Error('Refusing to overwrite palette probe');
fs.mkdirSync(output);
const browser=await chromium.launch({headless:true});
const result={source,browser:browser.version(),errors:[],checks:[]};
try{
 const context=await browser.newContext({viewport:{width:1200,height:900},serviceWorkers:'block'});
 await context.route(/https?:\/\//,route=>route.abort());
 const page=await context.newPage();
 page.on('pageerror',error=>result.errors.push(error.message));
 await page.goto(pathToFileURL(source).href);
 result.checks=await page.evaluate(()=>{
  const checks=[];
  for(const element of document.querySelectorAll('svg [fill],svg [stroke]')){
   for(const attribute of ['fill','stroke']){
    const raw=element.getAttribute(attribute)||'';
    const match=/^var\((--[a-z-]+)\)$/.exec(raw);
    if(!match)continue;
    const before=getComputedStyle(element)[attribute];
    const prior=document.documentElement.style.getPropertyValue(match[1]);
    document.documentElement.style.setProperty(match[1],'#005a80');
    const changed=getComputedStyle(element)[attribute];
    if(prior)document.documentElement.style.setProperty(match[1],prior);
    else document.documentElement.style.removeProperty(match[1]);
    const restored=getComputedStyle(element)[attribute];
    checks.push({attribute,variable:match[1],before,changed,restored,pass:changed==='rgb(0, 90, 128)'&&restored===before});
   }
  }
  return checks;
 });
 await context.close();
}catch(error){result.errors.push(error.stack);}
finally{await browser.close();result.pass=result.checks.length>0&&result.checks.every(x=>x.pass)&&result.errors.length===0;fs.writeFileSync(path.join(output,'observations.json'),JSON.stringify(result,null,2)+'\n');}
console.log(JSON.stringify(result));
if(!result.pass)process.exitCode=1;
