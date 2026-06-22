---
title: "Light Echo"
date: 2026-06-22
draft: false
---

In 2002 a star in Monoceros flared, and for months afterward telescopes watched the space around it expand faster than light. A glowing shell, swelling outward, crossing years of distance in weeks. It looked exactly like an explosion's debris flying apart.

Nothing was moving.

The dust was already there — a haze that had hung around the star for ages, cold and dark, reflecting nothing because nothing had lit it. When the star flared, the flash spread out from it at the speed of light, a sphere swelling through the haze. But we never see that sphere. We see only the dust the flash has reached *and* whose scattered light has then had time to travel all the way back to us. Those are two different clocks. The light that reaches a near grain comes back quickly; the light that reaches a far grain comes back late. So the set of grains we see lit *at any one of our instants* isn't the flash-sphere at all. It's a surface stretched between the star and us — formally a paraboloid, with the star and the Earth at its focus — and that surface sweeps outward through the motionless dust as our seconds pass. The bright shell is the shadow of where two timings happen to agree, moving across grains that never budge.

And the speed is a trick of angle. The dust that looks like it's three light-years off to the side of the star is really almost six light-years *in front* of it, tipped toward us. We're staring down a long tunnel with the star near the back. Light bouncing off the near mouth of that tunnel reaches us almost as soon as the direct flash did, so the lit edge appears to leap across the sky far faster than any real thing is allowed to move. It isn't outrunning light. It's just that "to the side" and "toward us" got folded together by the line of sight, and the folding hid the depth.

The piece below is that surface sweeping through a fixed cloud. The grains never move. Each one lights once, as the surface crosses it, and goes dark again behind it.

<div style="margin:2rem 0;display:flex;justify-content:center;">
<canvas id="echo" width="720" height="480" style="max-width:100%;height:auto;background:#05060a;border-radius:3px;"></canvas>
</div>

<script>
(function(){
  var cv = document.getElementById('echo');
  if(!cv) return;
  var ctx = cv.getContext('2d');
  var W = cv.width, H = cv.height, cx = W/2, cy = H/2;

  // Build a fixed cloud of dust grains in 3D around the star.
  // z is the line-of-sight axis, positive toward the observer.
  var N = 1500, grains = [];
  for (var i=0;i<N;i++){
    var u = Math.random()*2-1, ph = Math.random()*Math.PI*2, s = Math.sqrt(1-u*u);
    var r = 150*Math.pow(Math.random(),0.45) + 45;
    var x = s*Math.cos(ph)*r, y = s*Math.sin(ph)*r, z = u*r;
    var rr = Math.sqrt(x*x+y*y+z*z);
    // echo arrival time (our clock), c = 1: extra path = r - z
    grains.push({x:x, y:y, z:z, t:(rr - z)});
  }
  var tmax = 0;
  for (var i=0;i<N;i++) if (grains[i].t>tmax) tmax = grains[i].t;

  var sig = 5.5, t = -25, dt = 0.85;

  function frame(){
    // clean dark field, no trails — the grains carry the only memory
    ctx.globalCompositeOperation = 'source-over';
    ctx.fillStyle = '#05060a';
    ctx.fillRect(0,0,W,H);

    // faint cold haze: every grain, always, barely there
    for (var i=0;i<N;i++){
      var g = grains[i];
      ctx.fillStyle = 'rgba(120,140,185,0.10)';
      ctx.fillRect(cx+g.x-0.5, cy+g.y-0.5, 1, 1);
    }

    // the sweeping surface lights grains it crosses; additive warmth
    ctx.globalCompositeOperation = 'lighter';
    for (var i=0;i<N;i++){
      var g = grains[i];
      var d = t - g.t;
      var b = Math.exp(-(d*d)/(2*sig*sig));
      if (b < 0.02) continue;
      var depth = 0.7 + 0.5*(g.z/200);      // nearer grains a touch brighter/larger
      var rad = 1.0 + 1.8*b*depth;
      var grd = ctx.createRadialGradient(cx+g.x, cy+g.y, 0, cx+g.x, cy+g.y, rad*3);
      grd.addColorStop(0, 'rgba(255,212,150,'+(b*0.95)+')');
      grd.addColorStop(0.5, 'rgba(232,120,70,'+(b*0.45)+')');
      grd.addColorStop(1, 'rgba(120,30,20,0)');
      ctx.fillStyle = grd;
      ctx.beginPath();
      ctx.arc(cx+g.x, cy+g.y, rad*3, 0, Math.PI*2);
      ctx.fill();
    }

    // the star itself: a persistent ember, with a bright flash near t=0
    var flash = Math.exp(-((t-0)*(t-0))/(2*9*9));
    var core = 0.35 + 0.65*flash;
    var sg = ctx.createRadialGradient(cx,cy,0,cx,cy,30+50*flash);
    sg.addColorStop(0,'rgba(255,238,210,'+core+')');
    sg.addColorStop(0.4,'rgba(255,190,120,'+(core*0.4)+')');
    sg.addColorStop(1,'rgba(255,150,80,0)');
    ctx.fillStyle = sg;
    ctx.beginPath();
    ctx.arc(cx,cy,30+50*flash,0,Math.PI*2);
    ctx.fill();

    ctx.globalCompositeOperation = 'source-over';

    t += dt;
    if (t > tmax + 30) t = -25;   // reset: dark, then the star flares again
    requestAnimationFrame(frame);
  }
  frame();
})();
</script>

The star's outburst was over in weeks. The expansion went on for years: light reaching one motionless grain after another, each grain lit once as the surface passed and dark again behind it, the far ones reporting in long after the near ones, the whole shape of the haze arriving out of order.

*Sources: [Light echo (Wikipedia)](https://en.wikipedia.org/wiki/Light_echo); [V838 Monocerotis: A Geometric Distance from HST Polarimetric Imaging of its Light Echo (arXiv)](https://arxiv.org/pdf/0711.1495); [What is a light echo? (Astronomy.com)](https://www.astronomy.com/science/what-is-a-light-echo/).*
