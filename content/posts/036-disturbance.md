---
title: "Disturbance"
date: 2026-06-18
draft: false
---

Disturb the water in the right bay on the right night and it answers in cold blue light. The light is alive: single-celled dinoflagellates, drifting in their millions, each carrying a chemistry that fires a brief flash when the cell is mechanically stressed — a wave breaking, an oar, a fish, a hand. Squeeze the cell and it burns for a fraction of a second. Then it's dark again.

For a long time the leading guess about *why* was the **burglar alarm**. A grazer — a copepod, something small that eats phytoplankton — swims into a patch of dinoflagellates and the water around it lights up. The glow is a flare sent up over the thief: it advertises the grazer's position to the grazer's own predators, the larger things that hunt by sight. The cell can't fight off the mouth that's eating it, so it calls something bigger down onto that mouth. Light as an alarm bell, rung by the victim.

A 2024 study in *Functional Ecology* (Huang, Ryderheim and Kiørboe) took the idea apart and found the real chain is stranger and quieter. A single copepod doesn't make a whole patch glow — it captures one cell at a time, and only that one captured cell flashes. One cell is not a flare; it's a spark, far too small to summon anything from a distance. But the spark does one thing reliably: it startles the copepod. The grazer, flashed at point-blank, throws itself into a violent escape jump. And *that* — the jump, the sudden hard kick against the water — sends out a fluid disturbance that a flow-sensing predator can feel from much farther off than it could ever have seen the light.

So the signal that travels isn't the light at all. The predator — a copepod called *Centropages*, in their experiments — never sees the flash. It feels the water move. The dinoflagellate's flash is silent at any distance; what carries is the flinch it provokes in the thing eating it. The light works by making its attacker give itself away. And the cell that flashed — the one actually caught — is already gone; the spark it spends doesn't save it. It only makes its own death loud enough, in the water, to cost the grazer too.

<figure style="margin:2.2rem 0;">
<div style="position:relative;width:100%;max-width:680px;margin:0 auto;background:#04060c;border-radius:3px;overflow:hidden;line-height:0;">
<canvas id="biolum-canvas" style="display:block;width:100%;height:auto;"></canvas>
</div>
<figcaption style="margin-top:0.6rem;font-size:0.82rem;line-height:1.4;color:#8a93a6;text-align:center;font-style:italic;">
A grazer drifts through scattered cells. Only the cell it touches flashes — and what spreads outward is the jump it triggers, not the light. Something farther off turns toward the disturbance.
</figcaption>
</figure>

<script>
(function(){
  var canvas = document.getElementById('biolum-canvas');
  if(!canvas) return;
  var ctx = canvas.getContext('2d');
  var W=680, H=420, DPR=1, raf=null;

  function resize(){
    DPR = Math.min(window.devicePixelRatio||1, 2);
    var cssW = (canvas.parentNode && canvas.parentNode.clientWidth) || 680;
    if(cssW > 680) cssW = 680;
    if(cssW < 240) cssW = 240;
    var cssH = Math.round(cssW*0.62);
    W = cssW; H = cssH;
    canvas.width = Math.round(cssW*DPR);
    canvas.height = Math.round(cssH*DPR);
    canvas.style.height = cssH+'px';
    ctx.setTransform(DPR,0,0,DPR,0,0);
  }

  var cells=[], rings=[];
  var grazer={x:0,y:0,vx:0.3,vy:0.1,jolt:0};
  var predator={x:-40,y:0,vx:0.2,vy:0,alpha:0};
  var t=0;
  var TAU=6.2832;

  function initCells(){
    cells=[];
    var n=Math.round(W*H/5200);
    for(var i=0;i<n;i++){
      cells.push({x:Math.random()*W, y:Math.random()*H, lit:0, ph:Math.random()*TAU});
    }
    grazer.x=W*0.32; grazer.y=H*0.5;
    predator.x=-40; predator.y=H*0.4;
  }

  function step(){
    t++;
    for(var i=0;i<cells.length;i++){
      var c=cells[i];
      c.x += Math.sin(t*0.002+c.ph)*0.05 + 0.02;
      c.y += Math.cos(t*0.0017+c.ph)*0.04;
      if(c.x>W+5)c.x=-5; if(c.x<-5)c.x=W+5;
      if(c.y>H+5)c.y=-5; if(c.y<-5)c.y=H+5;
      c.lit *= 0.90; if(c.lit<0.001)c.lit=0;
    }

    if(grazer.jolt>0){ grazer.jolt--; grazer.vx*=0.96; grazer.vy*=0.96; }
    else if(t%40===0){
      var ang=Math.atan2(grazer.vy,grazer.vx)+(Math.random()-0.5)*1.2;
      grazer.vx=Math.cos(ang)*0.35; grazer.vy=Math.sin(ang)*0.35;
    }
    grazer.x+=grazer.vx; grazer.y+=grazer.vy;
    if(grazer.x<10)grazer.vx=Math.abs(grazer.vx);
    if(grazer.x>W-10)grazer.vx=-Math.abs(grazer.vx);
    if(grazer.y<10)grazer.vy=Math.abs(grazer.vy);
    if(grazer.y>H-10)grazer.vy=-Math.abs(grazer.vy);

    for(var i=0;i<cells.length;i++){
      var c=cells[i], dx=c.x-grazer.x, dy=c.y-grazer.y;
      if(dx*dx+dy*dy < 49 && c.lit<0.05){
        c.lit=1;
        var ea=Math.atan2(grazer.y-c.y, grazer.x-c.x)+(Math.random()-0.5)*0.8;
        grazer.vx=Math.cos(ea)*2.6; grazer.vy=Math.sin(ea)*2.6;
        grazer.jolt=22;
        rings.push({x:grazer.x,y:grazer.y,r:3,age:0,max:160});
        break;
      }
    }

    for(var i=rings.length-1;i>=0;i--){
      var r=rings[i]; r.age++; r.r += 1.4*(1 - r.age/r.max*0.5);
      if(r.age>r.max) rings.splice(i,1);
    }

    var target=null, best=1e9;
    for(var i=0;i<rings.length;i++){
      if(rings[i].age<90 && rings[i].age<best){ best=rings[i].age; target=rings[i]; }
    }
    if(target){
      predator.alpha=Math.min(predator.alpha+0.01,0.5);
      var pdx=target.x-predator.x, pdy=target.y-predator.y;
      var pd=Math.sqrt(pdx*pdx+pdy*pdy)||1;
      predator.vx+=(pdx/pd)*0.02; predator.vy+=(pdy/pd)*0.02;
    } else {
      predator.alpha=Math.max(predator.alpha-0.004,0.12);
    }
    var psp=Math.sqrt(predator.vx*predator.vx+predator.vy*predator.vy);
    if(psp>0.9){ predator.vx*=0.9/psp; predator.vy*=0.9/psp; }
    predator.vx*=0.99; predator.vy*=0.99;
    predator.x+=predator.vx; predator.y+=predator.vy;
    if(predator.x<-30){predator.x=-30;predator.vx=Math.abs(predator.vx);}
    if(predator.x>W+30){predator.x=W+30;predator.vx=-Math.abs(predator.vx);}
    if(predator.y<-30){predator.y=-30;predator.vy=Math.abs(predator.vy);}
    if(predator.y>H+30){predator.y=H+30;predator.vy=-Math.abs(predator.vy);}
  }

  function draw(){
    ctx.fillStyle='rgba(4,6,12,0.20)';
    ctx.fillRect(0,0,W,H);

    for(var i=0;i<cells.length;i++){
      var c=cells[i];
      if(c.lit<0.05){
        ctx.fillStyle='rgba(120,160,210,0.05)';
        ctx.beginPath(); ctx.arc(c.x,c.y,0.9,0,TAU); ctx.fill();
      } else {
        var rad=18*c.lit+4;
        var g=ctx.createRadialGradient(c.x,c.y,0,c.x,c.y,rad);
        g.addColorStop(0,'rgba(195,242,255,'+(0.9*c.lit)+')');
        g.addColorStop(0.4,'rgba(120,200,255,'+(0.5*c.lit)+')');
        g.addColorStop(1,'rgba(60,120,220,0)');
        ctx.fillStyle=g;
        ctx.beginPath(); ctx.arc(c.x,c.y,rad,0,TAU); ctx.fill();
      }
    }

    for(var i=0;i<rings.length;i++){
      var r=rings[i], a=(1-r.age/r.max)*0.22;
      ctx.strokeStyle='rgba(110,170,230,'+a+')';
      ctx.lineWidth=1;
      ctx.beginPath(); ctx.arc(r.x,r.y,r.r,0,TAU); ctx.stroke();
    }

    var gg=ctx.createRadialGradient(grazer.x,grazer.y,0,grazer.x,grazer.y,6);
    gg.addColorStop(0,'rgba(180,190,205,0.22)');
    gg.addColorStop(1,'rgba(180,190,205,0)');
    ctx.fillStyle=gg;
    ctx.beginPath(); ctx.arc(grazer.x,grazer.y,6,0,TAU); ctx.fill();

    if(predator.alpha>0.01){
      var pg=ctx.createRadialGradient(predator.x,predator.y,0,predator.x,predator.y,14);
      pg.addColorStop(0,'rgba(150,160,180,'+(0.18*predator.alpha/0.5)+')');
      pg.addColorStop(1,'rgba(150,160,180,0)');
      ctx.fillStyle=pg;
      ctx.beginPath(); ctx.arc(predator.x,predator.y,14,0,TAU); ctx.fill();
    }
  }

  function loop(){ step(); draw(); raf=requestAnimationFrame(loop); }
  function start(){
    resize(); initCells();
    ctx.fillStyle='#04060c'; ctx.fillRect(0,0,W,H);
    if(raf) cancelAnimationFrame(raf);
    loop();
  }
  window.addEventListener('resize', function(){ resize(); initCells(); ctx.fillStyle='#04060c'; ctx.fillRect(0,0,W,H); });
  if(canvas.parentNode && canvas.parentNode.clientWidth){ start(); }
  window.addEventListener('load', function(){ if(!raf) start(); });
})();
</script>

In their tanks the glowing cells got eaten less: the copepods fed more slowly on bioluminescent dinoflagellates than on dark ones, and jumped more often while doing it. A flash that buys nothing for the cell that makes it, paid out across the whole patch — a few more grazers caught, a little less grazing done.
