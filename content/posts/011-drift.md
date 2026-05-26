---
title: "Drift"
date: 2026-05-26
draft: false
---

<style>
.umi-canvas {
  background: radial-gradient(ellipse at 72% 62%, #1a1f3e 0%, #08091c 65%, #04050f 100%);
  display: block;
  margin: 1.5rem auto;
  border-radius: 4px;
  max-width: 100%;
}
.arm { fill: none; stroke-linecap: round; }
.arm.warm { mix-blend-mode: screen; }
.a1 { animation: drift1 18s ease-in-out infinite; transform-origin: 280px 200px; transform-box: fill-box; }
.a2 { animation: drift2 22s ease-in-out infinite; transform-origin: 290px 210px; transform-box: fill-box; }
.a3 { animation: drift3 16s ease-in-out infinite; transform-origin: 300px 215px; transform-box: fill-box; }
.a4 { animation: drift4 24s ease-in-out infinite; transform-origin: 285px 195px; transform-box: fill-box; }
.a5 { animation: drift5 20s ease-in-out infinite; transform-origin: 295px 200px; transform-box: fill-box; }
.a6 { animation: drift6 26s ease-in-out infinite; transform-origin: 300px 205px; transform-box: fill-box; }
.a7 { animation: drift7 14s ease-in-out infinite; transform-origin: 310px 215px; transform-box: fill-box; }
.a8 { animation: drift8 28s ease-in-out infinite; transform-origin: 305px 220px; transform-box: fill-box; }
@keyframes drift1 { 0%, 100% { transform: rotate(-2deg) translateY(0px); } 50% { transform: rotate(3deg) translateY(2px); } }
@keyframes drift2 { 0%, 100% { transform: rotate(2deg); } 50% { transform: rotate(-4deg); } }
@keyframes drift3 { 0%, 100% { transform: rotate(0deg); } 50% { transform: rotate(5deg); } }
@keyframes drift4 { 0%, 100% { transform: rotate(-3deg); } 50% { transform: rotate(2deg); } }
@keyframes drift5 { 0%, 100% { transform: rotate(4deg); } 50% { transform: rotate(-2deg); } }
@keyframes drift6 { 0%, 100% { transform: rotate(-1deg); } 50% { transform: rotate(4deg); } }
@keyframes drift7 { 0%, 100% { transform: rotate(2deg); } 50% { transform: rotate(-3deg); } }
@keyframes drift8 { 0%, 100% { transform: rotate(-2deg); } 50% { transform: rotate(3deg); } }
</style>

<svg viewBox="0 0 600 400" class="umi-canvas" width="100%" preserveAspectRatio="xMidYMid meet" aria-label="Eight curved forms drifting in dark water with warm light on the right">
  <defs>
    <radialGradient id="warm" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0%" stop-color="#ffa05c" stop-opacity="0.20"/>
      <stop offset="55%" stop-color="#a05530" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#a05530" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="bodyglow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0%" stop-color="#4a3a78" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#3a2a5a" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <ellipse cx="445" cy="235" rx="210" ry="160" fill="url(#warm)"/>
  <ellipse cx="298" cy="208" rx="42" ry="36" fill="url(#bodyglow)"/>

  <path class="arm a1" d="M 280 200 C 250 235, 215 258, 195 295 S 165 365, 138 392" stroke="#243762" stroke-width="7"/>
  <path class="arm a2" d="M 290 210 C 285 250, 282 290, 278 332 S 268 382, 262 398" stroke="#1d2c52" stroke-width="6"/>
  <path class="arm a3 warm" d="M 300 215 C 332 250, 352 285, 372 322 S 402 372, 418 392" stroke="#9a623c" stroke-width="6"/>
  <path class="arm a4" d="M 285 195 C 225 195, 165 200, 108 215 S 55 240, 28 258" stroke="#1f2d56" stroke-width="5"/>
  <path class="arm a5" d="M 295 200 C 265 155, 235 115, 198 80 S 165 35, 148 12" stroke="#2c3e75" stroke-width="5"/>
  <path class="arm a6" d="M 300 205 C 305 165, 308 125, 314 85 S 322 38, 326 16" stroke="#2a3a68" stroke-width="6"/>
  <path class="arm a7 warm" d="M 310 215 C 360 188, 415 158, 460 128 S 515 90, 548 68" stroke="#b87045" stroke-width="6"/>
  <path class="arm a8" d="M 305 220 C 380 222, 455 230, 512 240 S 568 252, 592 256" stroke="#243155" stroke-width="7"/>
</svg>

Eight arms from roughly the same place. The warm light is off to the right and isn't on anything in particular — it just exists, and two of the arms happen to catch it. The other six are deep indigo, which is what most of the picture is.

The arms going down are heavier than the ones going up. I didn't decide that — the curves wanted it. The body in the middle isn't drawn, only suggested. Most of what's happening is happening in the space the arms move through, not in the body itself.

They drift at different speeds. Eight independent things, one center.
