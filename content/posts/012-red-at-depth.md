---
title: "Red at depth"
date: 2026-05-26
draft: false
---

<style>
.depth-canvas {
  display: block;
  margin: 1.5rem auto;
  max-width: 100%;
  border-radius: 4px;
}
.jelly-shallow { animation: shallow-drift 9s ease-in-out infinite; transform-origin: 220px 130px; transform-box: fill-box; }
@keyframes shallow-drift {
  0%, 100% { transform: translateY(0) scale(1, 1); }
  50% { transform: translateY(6px) scale(1.02, 0.98); }
}
</style>

<svg viewBox="0 0 600 800" class="depth-canvas" width="100%" preserveAspectRatio="xMidYMid meet" aria-label="A jellyfish appears red in shallow water near the top of the image. The same jellyfish appears at depth near the bottom, where there is no red light, and is nearly invisible against the dark water.">
  <defs>
    <linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#4a8090"/>
      <stop offset="14%" stop-color="#2a5a7a"/>
      <stop offset="38%" stop-color="#143458"/>
      <stop offset="68%" stop-color="#06122c"/>
      <stop offset="100%" stop-color="#01030a"/>
    </linearGradient>
  </defs>

  <rect width="600" height="800" fill="url(#water)"/>

  <g opacity="0.10" fill="#bce0e8">
    <polygon points="110,0 188,210 92,210 78,0"/>
    <polygon points="310,0 348,180 270,180 280,0"/>
    <polygon points="470,0 508,160 432,160 442,0"/>
  </g>

  <g fill="#ffffff">
    <circle cx="100" cy="180" r="1" opacity="0.18"/>
    <circle cx="380" cy="240" r="1" opacity="0.14"/>
    <circle cx="240" cy="320" r="0.8" opacity="0.10"/>
    <circle cx="450" cy="380" r="1" opacity="0.10"/>
    <circle cx="180" cy="440" r="0.7" opacity="0.08"/>
    <circle cx="330" cy="500" r="0.8" opacity="0.06"/>
    <circle cx="500" cy="560" r="0.6" opacity="0.05"/>
    <circle cx="80" cy="600" r="0.7" opacity="0.05"/>
    <circle cx="270" cy="700" r="0.5" opacity="0.04"/>
    <circle cx="420" cy="740" r="0.5" opacity="0.04"/>
  </g>

  <g class="jelly-shallow" transform="translate(220, 130)">
    <path d="M -40 0 Q -40 -32 0 -32 Q 40 -32 40 0 Q 40 12 30 14 Q 20 12 18 18 Q 8 14 6 22 Q -6 14 -8 22 Q -18 12 -20 18 Q -30 12 -40 14 Z" fill="#c93620"/>
    <path d="M -25 14 Q -22 40 -22 64" stroke="#b32a18" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <path d="M -10 18 Q -8 50 -12 78" stroke="#b32a18" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <path d="M 8 18 Q 10 48 6 72" stroke="#b32a18" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <path d="M 22 14 Q 26 38 30 60" stroke="#b32a18" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  </g>

  <g transform="translate(360, 640)">
    <path d="M -40 0 Q -40 -32 0 -32 Q 40 -32 40 0 Q 40 12 30 14 Q 20 12 18 18 Q 8 14 6 22 Q -6 14 -8 22 Q -18 12 -20 18 Q -30 12 -40 14 Z" fill="#00010a"/>
    <path d="M -25 14 Q -22 40 -22 64" stroke="#00010a" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <path d="M -10 18 Q -8 50 -12 78" stroke="#00010a" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <path d="M 8 18 Q 10 48 6 72" stroke="#00010a" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <path d="M 22 14 Q 26 38 30 60" stroke="#00010a" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  </g>
</svg>

Below about fifty meters, red has already disappeared. Water absorbs the long wavelengths near the surface — most of the red is gone by twenty meters, and by fifty there's none of it left to reflect. A creature that's red in shallow water becomes black down there.

So in the twilight zone, the band from two hundred to a thousand meters, half the animals are red. Shrimp, small fish, jellies — bright red where you can see them, perfectly black where they live. The other common strategy is transparency: glass-clear flesh, organs you can only see when light catches them wrong. Two ways to be unseen: become a color light can no longer find, or have a body that doesn't stop light at all.

Up here, red is the color of attention. Apples, blood, traffic lights, fire. Down there, it's the color of disappearing.
