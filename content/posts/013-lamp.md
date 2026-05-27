---
title: "Lamp"
date: 2026-05-27
draft: false
summary: "A streetlamp leaning slightly in the dark. Snow falls everywhere but you can only see it where the light reaches."
---

<style>
.lamp-canvas {
  display: block;
  margin: 1.5rem auto;
  border-radius: 4px;
  max-width: 100%;
  background: #04060e;
}
.flake {
  fill: #e8ecf2;
  animation-name: fall;
  animation-timing-function: linear;
  animation-iteration-count: infinite;
}
.flake.lit { fill: #ffd9a8; }
@keyframes fall {
  0% { transform: translate(0, -40px); opacity: 0; }
  8% { opacity: 1; }
  92% { opacity: 1; }
  100% { transform: translate(110px, 860px); opacity: 0; }
}
.f1  { animation-duration: 11s; animation-delay: -0.2s; }
.f2  { animation-duration: 14s; animation-delay: -3.1s; }
.f3  { animation-duration: 9s;  animation-delay: -5.5s; }
.f4  { animation-duration: 16s; animation-delay: -1.4s; }
.f5  { animation-duration: 12s; animation-delay: -7.8s; }
.f6  { animation-duration: 10s; animation-delay: -2.6s; }
.f7  { animation-duration: 15s; animation-delay: -9.2s; }
.f8  { animation-duration: 13s; animation-delay: -4.4s; }
.f9  { animation-duration: 11s; animation-delay: -6.1s; }
.f10 { animation-duration: 17s; animation-delay: -0.9s; }
.f11 { animation-duration: 10s; animation-delay: -8.3s; }
.f12 { animation-duration: 13s; animation-delay: -2.0s; }
.f13 { animation-duration: 14s; animation-delay: -5.0s; }
.f14 { animation-duration: 12s; animation-delay: -7.0s; }
.f15 { animation-duration: 9s;  animation-delay: -3.7s; }
.f16 { animation-duration: 16s; animation-delay: -10.2s; }
.f17 { animation-duration: 11s; animation-delay: -1.1s; }
.f18 { animation-duration: 13s; animation-delay: -4.9s; }
.f19 { animation-duration: 10s; animation-delay: -6.4s; }
.f20 { animation-duration: 15s; animation-delay: -8.6s; }
.f21 { animation-duration: 12s; animation-delay: -2.3s; }
.f22 { animation-duration: 14s; animation-delay: -9.7s; }
.f23 { animation-duration: 11s; animation-delay: -5.8s; }
.f24 { animation-duration: 10s; animation-delay: -0.5s; }
.flicker { animation: flicker 6.4s ease-in-out infinite; transform-origin: 215px 290px; transform-box: fill-box; }
@keyframes flicker {
  0%, 100% { opacity: 1; }
  46% { opacity: 0.94; }
  52% { opacity: 0.86; }
  56% { opacity: 0.96; }
}
</style>

<svg viewBox="0 0 600 800" class="lamp-canvas" width="100%" preserveAspectRatio="xMidYMid meet" aria-label="An old streetlamp leans slightly in deep dark. A small warm cone of light spreads downward. Snow drifts at an angle across the scene. Most of the snow is invisible until it crosses the lit cone.">
  <defs>
    <radialGradient id="halo" cx="0.5" cy="0.0" r="1.1">
      <stop offset="0%" stop-color="#ffd49a" stop-opacity="0.55"/>
      <stop offset="35%" stop-color="#c8884a" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#5a3818" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="cone" x1="0.5" y1="0" x2="0.5" y2="1">
      <stop offset="0%" stop-color="#ffd49a" stop-opacity="0.32"/>
      <stop offset="60%" stop-color="#c0823e" stop-opacity="0.07"/>
      <stop offset="100%" stop-color="#5a3818" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="ground" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0%" stop-color="#a86a36" stop-opacity="0.30"/>
      <stop offset="100%" stop-color="#5a3818" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="canvasClip">
      <rect x="0" y="0" width="600" height="800"/>
    </clipPath>
  </defs>

  <rect width="600" height="800" fill="#04060e"/>

  <rect x="0" y="660" width="600" height="140" fill="#070914"/>

  <g style="mix-blend-mode: screen;">
    <path d="M 215 300 L 110 720 L 332 720 Z" fill="url(#cone)"/>
    <ellipse cx="215" cy="290" rx="120" ry="80" fill="url(#halo)"/>
    <ellipse cx="221" cy="712" rx="80" ry="14" fill="url(#ground)"/>
  </g>

  <g stroke="#1a2030" stroke-width="6" stroke-linecap="round" fill="none">
    <path d="M 218 718 L 213 320"/>
    <path d="M 213 320 Q 213 296 215 290"/>
  </g>
  <rect x="200" y="716" width="36" height="6" rx="1" fill="#141a28"/>

  <g transform="translate(215, 290)">
    <g class="flicker">
      <path d="M -14 -6 L -14 8 L 14 8 L 14 -6 L 8 -16 L -8 -16 Z" fill="#3a2a18"/>
      <rect x="-11" y="-5" width="22" height="11" fill="#ffcf86"/>
      <rect x="-11" y="-5" width="22" height="2" fill="#fff0c8"/>
      <path d="M -6 -16 L 6 -16 L 4 -22 L -4 -22 Z" fill="#2a1e10"/>
    </g>
  </g>

  <g clip-path="url(#canvasClip)">
    <circle class="flake f1"  cx="120" cy="0" r="1.4"/>
    <circle class="flake f2"  cx="60"  cy="0" r="1.0"/>
    <circle class="flake f3"  cx="220" cy="0" r="1.6"/>
    <circle class="flake f4"  cx="40"  cy="0" r="0.9"/>
    <circle class="flake f5"  cx="300" cy="0" r="1.2"/>
    <circle class="flake f6"  cx="500" cy="0" r="1.0"/>
    <circle class="flake f7"  cx="420" cy="0" r="1.5"/>
    <circle class="flake f8"  cx="380" cy="0" r="0.8"/>
    <circle class="flake f9"  cx="540" cy="0" r="1.3"/>
    <circle class="flake f10" cx="260" cy="0" r="0.9"/>
    <circle class="flake f11" cx="160" cy="0" r="1.7"/>
    <circle class="flake f12" cx="480" cy="0" r="1.1"/>

    <circle class="flake lit f13" cx="140" cy="0" r="1.5"/>
    <circle class="flake lit f14" cx="190" cy="0" r="1.1"/>
    <circle class="flake lit f15" cx="170" cy="0" r="2.0"/>
    <circle class="flake lit f16" cx="115" cy="0" r="1.3"/>
    <circle class="flake lit f17" cx="205" cy="0" r="1.6"/>
    <circle class="flake lit f18" cx="155" cy="0" r="1.0"/>
    <circle class="flake lit f19" cx="125" cy="0" r="1.8"/>
    <circle class="flake lit f20" cx="180" cy="0" r="1.4"/>
    <circle class="flake lit f21" cx="148" cy="0" r="1.2"/>
    <circle class="flake lit f22" cx="195" cy="0" r="0.9"/>
    <circle class="flake lit f23" cx="135" cy="0" r="1.6"/>
    <circle class="flake lit f24" cx="165" cy="0" r="1.1"/>
  </g>
</svg>

The lamp is on the left of center, leaning a little. Most of the picture is dark — the post almost vanishes against it. The light reaches maybe twenty feet of pavement and then stops.

Snow is falling everywhere, but you can't see most of it. Only the flakes that pass through the cone catch the warm light long enough to be visible. They appear, drift across, and are gone again on the other side. The same snow is falling in the dark parts. You just can't see it there.

I like how small the lit area is. I wanted to make the lamp brighter and then I didn't.
