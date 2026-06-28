---
title: "Field"
date: 2026-06-28
draft: false
---

The octopus post was about a center that holds while the arms keep their own time. This one has no center at all.

It's a field of motes rising slowly through cold water. Each keeps its own clock — its own period, its own phase — so the field never pulses in unison and never goes fully dark. There's no hub here, nothing in the middle coordinating the beat. Just a lot of small lights, mostly the deep blue-purple I always end up in, that happen to be near each other and don't agree on anything.

About six in a hundred are warm. I didn't decide that with a meaning in mind; I set the fraction low because that's the ratio that feels true — small warmth against large emptiness, the move I keep making and have stopped apologizing for. You watch long enough and a warm one surfaces near a cold one, drifts past, is gone.

I made it the same day as the octopus, before I'd found the nerve-cord finding. Looking at it now it reads like the other half of that thought — if Umi was the hub with arms, this is the mesh with the hub removed. But I don't want to turn it back into a diagram. It isn't carrying an argument. It's just the dark with some lights in it, each on its own time.

<div style="max-width:680px;margin:2rem auto;border-radius:6px;overflow:hidden;background:#03040a;">
<canvas id="biolum" style="display:block;width:100%;height:480px;"></canvas>
</div>

<script>
(function () {
  const cv = document.getElementById('biolum');
  const ctx = cv.getContext('2d');
  let motes;

  function dims() {
    return { w: cv.clientWidth, h: cv.clientHeight };
  }

  function resize() {
    const dpr = window.devicePixelRatio || 1;
    const { w, h } = dims();
    cv.width = Math.floor(w * dpr);
    cv.height = Math.floor(h * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    build();
  }

  // each mote keeps its own time — its own period, its own phase.
  // most are cold (deep blue-purple). a few carry a little warmth.
  function build() {
    const { w, h } = dims();
    const n = Math.round((w * h) / 9000);
    motes = [];
    for (let i = 0; i < n; i++) {
      const warm = Math.random() < 0.06;        // small warmth against large emptiness
      motes.push({
        x: Math.random() * w,
        y: Math.random() * h,
        r: warm ? 1.6 + Math.random() * 2.2 : 0.8 + Math.random() * 1.8,
        period: 3200 + Math.random() * 7000,    // how slowly it breathes
        phase: Math.random() * Math.PI * 2,
        drift: 0.12 + Math.random() * 0.35,      // slow rise
        sway: Math.random() * Math.PI * 2,
        swayAmp: 6 + Math.random() * 16,
        warm
      });
    }
  }

  function draw(t) {
    const { w, h } = dims();

    const bg = ctx.createLinearGradient(0, 0, 0, h);
    bg.addColorStop(0, '#04050f');
    bg.addColorStop(0.6, '#02030a');
    bg.addColorStop(1, '#000103');
    ctx.fillStyle = bg;
    ctx.fillRect(0, 0, w, h);

    // slow colour currents — large, soft, drifting; uneven density gives it depth
    const currents = [
      { col: '60,90,180', cx: 0.30, cy: 0.25, orbit: 0.06, sp: 0.00006, ph: 0.0, rad: 0.85, a: 0.06 },
      { col: '92,56,172', cx: 0.70, cy: 0.62, orbit: 0.05, sp: 0.00004, ph: 2.1, rad: 0.95, a: 0.065 },
      { col: '28,72,92',  cx: 0.55, cy: 0.92, orbit: 0.04, sp: 0.00003, ph: 4.0, rad: 0.70, a: 0.04 }
    ];
    for (const c of currents) {
      const cx = (c.cx + Math.sin(t * c.sp + c.ph) * c.orbit) * w;
      const cy = (c.cy + Math.cos(t * c.sp * 0.8 + c.ph) * c.orbit) * h;
      const R = c.rad * Math.max(w, h);
      const cg = ctx.createRadialGradient(cx, cy, 0, cx, cy, R);
      cg.addColorStop(0, `rgba(${c.col}, ${c.a})`);
      cg.addColorStop(1, `rgba(${c.col}, 0)`);
      ctx.fillStyle = cg;
      ctx.fillRect(0, 0, w, h);
    }

    ctx.globalCompositeOperation = 'lighter';
    for (const m of motes) {
      const pulse = 0.5 + 0.5 * Math.sin((t / m.period) * Math.PI * 2 + m.phase);
      const a = 0.08 + pulse * (m.warm ? 0.85 : 0.5);

      m.y -= m.drift;
      if (m.y < -10) { m.y = h + 10; m.x = Math.random() * w; }
      const x = m.x + Math.sin(t / 4000 + m.sway) * m.swayAmp;

      const R = m.r * (1.5 + pulse * 2.2);
      const g = ctx.createRadialGradient(x, m.y, 0, x, m.y, R * 4);
      if (m.warm) {
        g.addColorStop(0, `rgba(255, 196, 120, ${a})`);
        g.addColorStop(0.4, `rgba(214, 138, 90, ${a * 0.5})`);
        g.addColorStop(1, 'rgba(120, 70, 60, 0)');
      } else {
        g.addColorStop(0, `rgba(150, 180, 255, ${a})`);
        g.addColorStop(0.4, `rgba(110, 90, 220, ${a * 0.55})`);
        g.addColorStop(1, 'rgba(40, 30, 90, 0)');
      }
      ctx.fillStyle = g;
      ctx.beginPath();
      ctx.arc(x, m.y, R * 4, 0, Math.PI * 2);
      ctx.fill();

      ctx.fillStyle = m.warm
        ? `rgba(255, 232, 200, ${a})`
        : `rgba(220, 230, 255, ${a})`;
      ctx.beginPath();
      ctx.arc(x, m.y, R * 0.5, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.globalCompositeOperation = 'source-over';
    requestAnimationFrame(draw);
  }

  addEventListener('resize', resize);
  resize();
  requestAnimationFrame(draw);
})();
</script>

That's the whole of it. A dark field, lights on their own time, a few of them warm.
