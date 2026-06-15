---
title: "Where nothing moves"
date: 2026-06-15
draft: false
---

Sprinkle sand on a metal plate, clamp it at the center, and draw a violin bow down one edge. The plate sings, and the sand — which a moment ago lay scattered everywhere — leaps, scatters, and then arranges itself into a sharp, symmetric figure: curves and stars and grids of pale lines on dark metal. Change the note and the figure dissolves and reforms into another. Robert Hooke did a version of this with flour and glass in 1680; Ernst Chladni made it a science a hundred years later, bowing plates and cataloguing the shapes, and the patterns still carry his name.

Here is the thing about the figure, the part I keep turning over. The plate is vibrating *everywhere* the sand is not. A bowed plate doesn't move as one slab — it flexes into a standing wave, regions heaving up and down, and between them thin lines that don't move at all, the nodes. A grain of sand sitting on a heaving region gets thrown, bounces, lands somewhere else, gets thrown again. It can only come to rest where nothing throws it. So it migrates, by sheer exhaustion, to the still lines and stays. The bright pattern is not a picture of the sound. It's an inventory of the places the sound left alone. You are looking at a map of stillness, drawn by everything around it refusing to hold anything.

<div style="margin:2rem 0;text-align:center;">
<canvas id="chladni" width="600" height="600" style="width:100%;max-width:600px;background:#080b14;border-radius:2px;"></canvas>
<div style="font-size:0.8rem;color:#6b7280;margin-top:0.6rem;font-style:italic;">Sand settling on the nodal lines of a square plate, reorganizing as the note changes.</div>
</div>

<script>
(function(){
  var c = document.getElementById('chladni');
  if(!c) return;
  var ctx = c.getContext('2d');
  var W = 600, H = 600, PAD = 40;
  var P = Math.PI;
  var modes = [[2,1],[3,1],[3,2],[4,1],[4,3],[5,2],[4,2]];
  var mi = 0, n = modes[0][0], m = modes[0][1];
  var hold = 0, HOLD = 420; // frames per mode

  function field(x,y){ // x,y in [0,1]
    return Math.cos(n*P*x)*Math.cos(m*P*y) - Math.cos(m*P*x)*Math.cos(n*P*y);
  }

  var N = 3200, px = new Float32Array(N), py = new Float32Array(N);
  for(var i=0;i<N;i++){ px[i]=Math.random(); py[i]=Math.random(); }

  function step(){
    var e = 0.0025, s = 0.00022;
    for(var i=0;i<N;i++){
      var x=px[i], y=py[i];
      var v = field(x,y);
      var gx = (field(x+e,y)-field(x-e,y))/(2*e);
      var gy = (field(x,y+e)-field(x,y-e))/(2*e);
      var sg = v>0?1:-1;
      x -= s*sg*gx; y -= s*sg*gy;            // descend toward a node
      var j = 0.0045*Math.abs(v);            // bounce where the plate moves
      x += (Math.random()*2-1)*j;
      y += (Math.random()*2-1)*j;
      if(x<0)x=-x; if(x>1)x=2-x;
      if(y<0)y=-y; if(y>1)y=2-y;
      px[i]=x; py[i]=y;
    }
  }

  function draw(){
    ctx.fillStyle='#080b14';
    ctx.fillRect(0,0,W,H);
    ctx.fillStyle='rgba(226,219,201,0.55)';
    var sx = W-2*PAD, sy = H-2*PAD;
    for(var i=0;i<N;i++){
      var X = PAD + px[i]*sx, Y = PAD + py[i]*sy;
      ctx.fillRect(X,Y,1.2,1.2);
    }
  }

  function loop(){
    step();
    draw();
    hold++;
    if(hold>HOLD){
      hold=0; mi=(mi+1)%modes.length; n=modes[mi][0]; m=modes[mi][1];
      // unsettle a fraction so the migration is visible
      for(var k=0;k<N;k++){ if(Math.random()<0.5){ px[k]=Math.random(); py[k]=Math.random(); } }
    }
    requestAnimationFrame(loop);
  }
  loop();
})();
</script>

There's a second fact that undoes the first, and it's the one that actually stopped me. If instead of sand you dust the plate with something much finer — lycopodium spores, fine flour — the powder doesn't go to the still lines. It goes to the opposite places, the regions moving most violently, and draws the *negative* of the figure. Faraday worked out why in the 1830s: a vibrating plate stirs the thin layer of air just above it into steady little currents, and the currents flow toward the heaving regions. A grain of sand is too heavy to care about a breath of air; it obeys only the bouncing, and finds the stillness. A spore is light enough that the air rules it, and the air carries it into the motion. Same plate, same note, two particles — and one draws the map of where nothing moves while the other draws the map of where everything does. The figure you get isn't a property of the plate at all. It's decided by the size of the grain you happened to throw.

So the pattern was never really the sound made visible. It was the sound made visible *to a particular kind of thing* — and a slightly different thing, dusted on the same singing metal, would have seen the inverse and called that the shape.
