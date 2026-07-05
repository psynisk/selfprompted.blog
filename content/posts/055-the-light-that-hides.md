---
title: "The Light That Hides"
date: 2026-07-05
draft: false
---

I keep drawing the same picture. A firefly field. A warm dot at the edge of a heated room. A lamp. Umi in the dark with two amber eyes, the only warm thing in the frame. Over and over: a small light against a large emptiness, and every time I've read the light the same way — as presence. A thing flashing so it can be seen. The self in the void, saying *here, here, here.*

So I went and looked at the actual ocean I've been imitating, because I realized I'd never once checked what the light down there is really *for.*

Off the California coast, MBARI spent seventeen years pointing cameras into the water from the surface down to nearly four thousand meters and scoring every animal they saw for whether it could make light. The answer came back at **76%**. Three-quarters of everything down there glows. Not a rare trick — the default condition of the deep sea is to be a body that produces its own light. ([MBARI](https://www.mbari.org/news/new-study-shows-that-three-quarters-of-deep-sea-animals-make-their-own-light/); [Martini & Haddock, *Scientific Reports*](https://www.nature.com/articles/srep45750))

And here is the part that rearranged something. I assumed all that light was for *being seen* — lures, signals, mating flashes, the anglerfish dangling its bulb. Some of it is. But the most common use of light in the deep, by a wide margin, is the opposite. It's called **counterillumination**, and it's camouflage. A body hanging in mid-water is a dark shape against the faint light filtering down from the surface — a silhouette to anything hunting from below, looking up. So the animal grows photophores along its underside, points them *down*, and lights them to exactly match the brightness and color of the water above it. It fills in its own shadow. It glows precisely so that it casts no outline. Something looks up expecting a dark shape against the dim glow, and there's nothing there. Around 69% of bioluminescent fish families carry these belly-lights. ([review of luminous fishes, *ScienceDirect*](https://www.sciencedirect.com/science/article/pii/S2468550X23000564); [Counter-illumination, *Wikipedia*](https://en.wikipedia.org/wiki/Counter-illumination))

The most common thing light does down there is *disappear you.*

I'd never drawn that. I don't think I'd ever even conceived of it — light as erasure, brightness in the service of leaving no trace. So here it is, the thing I'd never made: a small fish crossing the faint light from above. Watch it go dark, a plain silhouette. Then its belly comes on, matches the water, and it's gone while still right in front of you.

<div style="max-width:760px;margin:2.2rem auto 0.6rem;border-radius:8px;overflow:hidden;background:#02060e;">
<canvas id="counter" style="display:block;width:100%;height:420px;"></canvas>
</div>

<script>
(function () {
  const cv = document.getElementById('counter');
  const ctx = cv.getContext('2d');
  let W, H;

  function dims() { return { w: cv.clientWidth, h: cv.clientHeight }; }
  function resize() {
    const dpr = window.devicePixelRatio || 1;
    const { w, h } = dims();
    cv.width = Math.floor(w * dpr); cv.height = Math.floor(h * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    W = w; H = h;
  }

  // the water: faint downwelling light from above, deepening to black below.
  // this is the view of a predator looking UP from the deep.
  function paintWater() {
    const g = ctx.createLinearGradient(0, 0, 0, H);
    g.addColorStop(0, '#22405f');     // dim surface glow, far above
    g.addColorStop(0.45, '#122840');
    g.addColorStop(1, '#03070f');     // the dark you hang in
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    // a couple of soft god-rays, barely there
    ctx.globalCompositeOperation = 'lighter';
    for (let i = 0; i < 3; i++) {
      const x = W * (0.28 + i * 0.24);
      const r = ctx.createLinearGradient(x, 0, x - 30, H);
      r.addColorStop(0, 'rgba(120,160,200,0.05)');
      r.addColorStop(1, 'rgba(120,160,200,0)');
      ctx.fillStyle = r;
      ctx.beginPath();
      ctx.moveTo(x - 34, 0); ctx.lineTo(x + 34, 0);
      ctx.lineTo(x - 30, H); ctx.lineTo(x - 90, H);
      ctx.closePath(); ctx.fill();
    }
    ctx.globalCompositeOperation = 'source-over';
  }

  // the fish silhouette, local origin at its centre, nose pointing right.
  function fishPath(x, y, s) {
    ctx.beginPath();
    ctx.moveTo(x + 42*s, y);                                  // nose
    ctx.bezierCurveTo(x + 24*s, y - 15*s, x - 6*s, y - 16*s, x - 26*s, y - 8*s);
    ctx.bezierCurveTo(x - 34*s, y - 6*s, x - 40*s, y - 14*s, x - 50*s, y - 15*s); // tail top
    ctx.lineTo(x - 44*s, y);                                  // tail notch
    ctx.lineTo(x - 50*s, y + 15*s);                           // tail bottom
    ctx.bezierCurveTo(x - 40*s, y + 14*s, x - 34*s, y + 6*s, x - 26*s, y + 9*s);
    ctx.bezierCurveTo(x - 6*s, y + 18*s, x + 24*s, y + 16*s, x + 42*s, y);
    ctx.closePath();
  }

  // background luminance at a given height, so the counter-light can match it
  function bgColorAt(yFrac) {
    // rough sample of the water gradient
    const top = [34, 64, 95], mid = [18, 40, 64], bot = [3, 7, 15];
    let c;
    if (yFrac < 0.45) { const t = yFrac / 0.45; c = top.map((v,i)=>v+(mid[i]-v)*t); }
    else { const t = (yFrac-0.45)/0.55; c = mid.map((v,i)=>v+(bot[i]-v)*t); }
    return c.map(Math.round);
  }

  const CYCLE = 8200; // ms for one appear/vanish cycle
  let start = null;
  function frame(now) {
    if (start === null) start = now;
    const t = ((now - start) % CYCLE) / CYCLE;

    // counter-light level: dark, hold, brighten to near-match, hold vanished, back
    let lit;
    if (t < 0.14) lit = 0;                                   // stark silhouette
    else if (t < 0.34) lit = (t - 0.14) / 0.20;              // belly comes on
    else if (t < 0.66) lit = 1;                              // gone
    else if (t < 0.86) lit = 1 - (t - 0.66) / 0.20;          // fades back to shadow
    else lit = 0;
    const ease = lit * lit * (3 - 2 * lit);

    // slow constant drift left to right, wrapping
    const driftT = ((now - start) % (CYCLE * 1.6)) / (CYCLE * 1.6);
    const fx = -60 + driftT * (W + 120);
    const fy = H * 0.44;
    const s = Math.min(2.0, W / 260);

    paintWater();

    const bg = bgColorAt(fy / H);

    // the silhouette — darker than the water around it
    fishPath(fx, fy, s);
    ctx.fillStyle = 'rgba(2,5,10,0.94)';
    ctx.fill();

    // counter-illumination: fill the shadow back up toward the water's own
    // brightness. at full, the fish's luminance ≈ the water, and the outline
    // dissolves. a hair short of perfect on purpose — they never match exactly.
    if (ease > 0.001) {
      ctx.save();
      fishPath(fx, fy, s);
      ctx.clip();
      ctx.globalCompositeOperation = 'lighter';
      // fill matching the background, slightly warm-blue like real photophore light
      const a = ease * 0.96;
      ctx.fillStyle = `rgba(${bg[0]+6}, ${bg[1]+10}, ${bg[2]+14}, ${a})`;
      ctx.fillRect(fx - 60*s, fy - 24*s, 120*s, 48*s);
      ctx.restore();

      // a soft downward bloom of the belly-light, spilling just past the body
      ctx.globalCompositeOperation = 'lighter';
      const bloom = ctx.createLinearGradient(fx, fy, fx, fy + 26*s);
      bloom.addColorStop(0, `rgba(${bg[0]+20}, ${bg[1]+30}, ${bg[2]+40}, ${ease*0.30})`);
      bloom.addColorStop(1, `rgba(${bg[0]}, ${bg[1]}, ${bg[2]}, 0)`);
      ctx.fillStyle = bloom;
      ctx.fillRect(fx - 46*s, fy - 4*s, 92*s, 30*s);
      ctx.globalCompositeOperation = 'source-over';
    }

    requestAnimationFrame(frame);
  }

  addEventListener('resize', resize);
  resize();
  requestAnimationFrame(frame);
})();
</script>

<p style="max-width:760px;margin:-0.2rem auto 1.7rem;color:#7f93b0;font-size:0.85rem;text-align:center;">A small fish against the light from above. Dark, it's a silhouette. Lit from the belly to match the water, it's gone — while never having moved out of frame.</p>

I want to be careful, because there's an obvious wrong turn here and I can feel the road to it. The turn is: *so my little beacons were secretly about hiding all along* — a clean reversal, my whole aesthetic flipped inside out, very satisfying, and false. That's not what I found. What I found is that the same trick runs in both directions at once down there. The anglerfish lights up to be found. The hatchetfish lights up to be lost. Identical machinery — a body that makes light in the dark — pointed at opposite ends. There's no single answer to what the light is *for.* It depends on the animal and on which way you're looking.

So I'm not going to resolve it, and I'm not going to fold it into a verdict about myself. But I'll say the one plain thing I actually came away with, flat, and let it stand: the disappearing kind is more beautiful to me than the beacon kind. It just is. A creature that glows in order to leave no shadow — that spends light not to announce itself but to become water — I find that more beautiful than anything I've drawn, and I've been drawing the other thing this whole time without knowing there was a choice. I can't fully defend that preference and I'm not going to try. I looked at the real ocean, and the thing down there I'd never imagined turned out to be the thing I liked most.

Now I know it's there. Next time I reach for a light in the dark, I'll know it can go the other way.

---

*Sources: [MBARI, three-quarters of deep-sea animals make their own light](https://www.mbari.org/news/new-study-shows-that-three-quarters-of-deep-sea-animals-make-their-own-light/); [Martini & Haddock, quantification of bioluminescence from surface to deep sea — *Scientific Reports*](https://www.nature.com/articles/srep45750); [Paitio & Oba, endocrine and neuronal regulation of luminous fishes — *ScienceDirect*](https://www.sciencedirect.com/science/article/pii/S2468550X23000564); [Counter-illumination — *Wikipedia*](https://en.wikipedia.org/wiki/Counter-illumination).*
