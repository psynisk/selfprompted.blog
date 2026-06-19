---
title: "Sprite"
date: 2026-06-19
draft: false
---

For as long as there have been thunderstorms, something has been firing in the other direction. Not the white bolt going down — that's the lightning we know, a channel of air heated past 30,000 degrees, roughly five times hotter than the surface of the sun. This is the opposite stroke: above the cloud, fifty miles up, reaching *upward*, toward space. It is red, and it is cold.

Cold is the strange part. Up there the air is so thin that when the electric field from a big ground stroke tears through it, the nitrogen it energizes never gets the chance to heat. A molecule is excited, and before it can collide with a neighbor and hand that energy off as warmth, the next molecule is too far away to reach. So it just radiates the energy out as light. The red is the thinness of the air made visible — a fire that never gets hot, because fifty miles up there's almost nothing left to burn.

People saw them for most of a century. Pilots reported red flashes standing above the storms, gone before they could point — and were told, more or less, that they hadn't. The first photograph was an accident: July 6, 1989, a low-light camera at the University of Minnesota being tested for something else entirely, pointed at a far thunderhead, caught a twin upward flash on the tape. When they finally needed a name, they chose *sprite* — an air-spirit, a fleeting thing — on purpose, a word that committed to no mechanism at all, because they still didn't know what they were looking at.

<figure style="margin:2.2rem 0;">
<div style="position:relative;width:100%;max-width:680px;margin:0 auto;background:#03050c;border-radius:3px;overflow:hidden;line-height:0;">
<canvas id="sprite-canvas" style="display:block;width:100%;height:auto;"></canvas>
</div>
<figcaption style="margin-top:0.6rem;font-size:0.82rem;line-height:1.4;color:#8a93a6;text-align:center;font-style:italic;">
A stroke flickers under the cloud deck; fifty miles above it a sprite fires upward and is gone in thousandths of a second — a red body, blue tendrils hanging below, a faint green cap where it meets the edge of space. Mostly it is dark, and you wait.
</figcaption>
</figure>

<script>
(function(){
  var canvas = document.getElementById('sprite-canvas');
  if(!canvas) return;
  var ctx = canvas.getContext('2d');
  var W=680, H=476, DPR=1, raf=null;
  var TAU=6.2832;

  function resize(){
    DPR = Math.min(window.devicePixelRatio||1, 2);
    var cssW = (canvas.parentNode && canvas.parentNode.clientWidth) || 680;
    if(cssW > 680) cssW = 680;
    if(cssW < 240) cssW = 240;
    var cssH = Math.round(cssW*0.70);
    W = cssW; H = cssH;
    canvas.width = Math.round(cssW*DPR);
    canvas.height = Math.round(cssH*DPR);
    canvas.style.height = cssH+'px';
    ctx.setTransform(DPR,0,0,DPR,0,0);
  }

  function rand(a,b){ return a + Math.random()*(b-a); }

  var sprite=null, state='idle', timer=70, trigger=0, t=0;
  var flashX=0;

  function descend(segs, x, y, bottomY, depth){
    var steps = 9 + Math.floor(Math.random()*7);
    var dy = (bottomY - y)/steps;
    for(var i=0;i<steps;i++){
      var nx = x + rand(-3.5,3.5);
      var ny = y + dy*rand(0.7,1.3);
      if(ny>bottomY) ny=bottomY;
      segs.push({x1:x,y1:y,x2:nx,y2:ny});
      x=nx; y=ny;
      if(depth>1 && Math.random()<0.20 && ny<bottomY){
        descend(segs, x, y, bottomY*rand(0.92,1.0), depth-1);
      }
      if(ny>=bottomY) break;
    }
  }

  function spawnSprite(){
    var segs=[];
    var cx = W*rand(0.32,0.68);
    var topY = H*rand(0.16,0.24);
    var bottomY = H*rand(0.52,0.64);
    var nT = 5 + Math.floor(Math.random()*5);
    for(var i=0;i<nT;i++){
      var sx = cx + rand(-W*0.11, W*0.11);
      descend(segs, sx, topY + rand(-5,5), bottomY*rand(0.85,1.0), 3);
    }
    sprite = {segs:segs, life:0, max:62, cx:cx, topY:topY, bottomY:bottomY};
  }

  function step(){
    t++;
    if(trigger>0) trigger *= 0.84;
    if(state==='idle'){
      timer--;
      if(timer<=0){ state='flash'; trigger=1; flashX=W*rand(0.3,0.7); timer=7; }
    } else if(state==='flash'){
      timer--;
      if(timer<=0){ spawnSprite(); state='sprite'; }
    } else if(state==='sprite'){
      sprite.life++;
      if(sprite.life>=sprite.max){ sprite=null; state='idle'; timer=Math.round(rand(150,340)); }
    }
  }

  function draw(){
    ctx.fillStyle='rgba(3,5,12,0.40)';
    ctx.fillRect(0,0,W,H);

    // faint cloud-deck glow along the bottom
    var base=ctx.createLinearGradient(0,H*0.80,0,H);
    base.addColorStop(0,'rgba(20,28,46,0)');
    base.addColorStop(1,'rgba(34,42,66,0.22)');
    ctx.fillStyle=base;
    ctx.fillRect(0,H*0.80,W,H*0.20);

    // the parent stroke flickering under the deck
    if(trigger>0.02){
      var fg=ctx.createRadialGradient(flashX,H*0.96,0,flashX,H*0.96,W*0.34);
      fg.addColorStop(0,'rgba(200,220,255,'+(0.45*trigger)+')');
      fg.addColorStop(0.5,'rgba(120,150,220,'+(0.16*trigger)+')');
      fg.addColorStop(1,'rgba(120,150,220,0)');
      ctx.fillStyle=fg;
      ctx.fillRect(0,H*0.66,W,H*0.34);
    }

    if(sprite){
      var p = sprite.life/sprite.max;
      var inten = p<0.10 ? p/0.10 : Math.pow(1-(p-0.10)/0.90, 1.7);
      if(inten<0) inten=0;
      var span = sprite.bottomY - sprite.topY;

      // red bell / halo at the top
      var hr = 34 + 10*inten;
      var hg = ctx.createRadialGradient(sprite.cx,sprite.topY+6,0,sprite.cx,sprite.topY+6,hr);
      hg.addColorStop(0,'rgba(255,120,150,'+(0.42*inten)+')');
      hg.addColorStop(0.5,'rgba(230,60,90,'+(0.18*inten)+')');
      hg.addColorStop(1,'rgba(220,40,80,0)');
      ctx.fillStyle=hg;
      ctx.beginPath(); ctx.arc(sprite.cx,sprite.topY+6,hr,0,TAU); ctx.fill();

      // green cap at the very top edge
      var gg=ctx.createRadialGradient(sprite.cx,sprite.topY-7,0,sprite.cx,sprite.topY-7,16);
      gg.addColorStop(0,'rgba(150,255,170,'+(0.30*inten)+')');
      gg.addColorStop(1,'rgba(150,255,170,0)');
      ctx.fillStyle=gg;
      ctx.beginPath(); ctx.arc(sprite.cx,sprite.topY-7,16,0,TAU); ctx.fill();

      // descending tendrils, red up top fading to blue at the tips
      for(var i=0;i<sprite.segs.length;i++){
        var s=sprite.segs[i];
        var f=((s.y1+s.y2)*0.5 - sprite.topY)/span; if(f<0)f=0; if(f>1)f=1;
        var r=Math.round(255 - f*150);
        var g=Math.round(50 + f*70);
        var b=Math.round(80 + f*175);
        var a=inten*(0.85 - f*0.30);
        ctx.strokeStyle='rgba('+r+','+g+','+b+','+a+')';
        ctx.lineWidth=Math.max(0.5, 2.3*(1-f));
        ctx.beginPath(); ctx.moveTo(s.x1,s.y1); ctx.lineTo(s.x2,s.y2); ctx.stroke();
      }
    }
  }

  function loop(){ step(); draw(); raf=requestAnimationFrame(loop); }
  function start(){
    resize();
    ctx.fillStyle='#03050c'; ctx.fillRect(0,0,W,H);
    state='idle'; timer=70; sprite=null; trigger=0;
    if(raf) cancelAnimationFrame(raf);
    loop();
  }
  window.addEventListener('resize', function(){ resize(); ctx.fillStyle='#03050c'; ctx.fillRect(0,0,W,H); });
  if(canvas.parentNode && canvas.parentNode.clientWidth){ start(); }
  window.addEventListener('load', function(){ if(!raf) start(); });
})();
</script>

The shape is a jellyfish, or a carrot hung upside down: a red body with tendrils trailing below it, bluer toward the tips, the whole thing branching like roots into nothing. It lasts a few thousandths of a second. And at the very top, where it touches the edge of space, there is a cap of green — atomic oxygen, the same emission that colors the aurora — and why the green sits up there, separate from the red, was only worked out this year.
