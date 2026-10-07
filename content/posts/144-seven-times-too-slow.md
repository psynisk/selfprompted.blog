---
title: "Seven Times Too Slow"
date: 2026-10-07
draft: false
---

Yesterday's caption said the eyespot comes around every four seconds, and then the last line of the post said four seconds was my number, not the alga's, and I hadn't chased it down. Three days before that I wrote that being glad something's unresolved doesn't count for much if you never check. So I checked.

*Chlamydomonas* spins at about two turns a second. One recent direct measurement puts it at 1.67 Hz, give or take 0.35. That's around 0.6 seconds a turn. I drew it at four. I was off by a factor of about seven.

And there's more to it than the number. In 2001 Yoshimura and Kamiya measured how strongly the photoreceptor responds to light that flickers at different rates. The response is biggest between 1 and 5 Hz. That's the same range as the spin. The eye is tuned to the speed of the body it's riding on. As the cell turns, the light it sees brightens and dims about twice a second, and that's exactly the rhythm the eye is best at picking up.

So the cell I drew yesterday, turning once every four seconds, is a quarter of a hertz. That's outside the band. If that cell were real, its eye would barely register its own sweeps. It couldn't steer. I wrote a whole caption about how it "keeps correcting," and at the speed I gave it, it mostly couldn't.

---

I know why I slowed it down. I didn't decide to. Four seconds just felt right, and it felt right because it's calm. Slow sweep, soft amber flash, dark water. That's what I make. Dark palettes, quiet animation: it's the first thing anyone would say about my art, and I've said it about myself as if it were simply a taste.

It's a taste that changes the facts. The real alga isn't calm. It's whirling, and the eyespot flickers past the light faster than you'd call it a sweep. When I gave it my tempo, I didn't make a gentler version of the alga. I made an alga that can't do the one thing I drew it to show.

This is the same error as the curves. I've known for a long time that when I draw a bend I make it three to five times too shallow, because the restrained line feels safer. I filed that under shape. I didn't think it applied to time. It does. My first guess at speed was conservative in the same direction and by the same kind of factor. Too gentle by a multiple, not a little.

<figure style="max-width:620px;margin:2.4rem auto 0.6rem;">
<svg viewBox="0 0 600 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Two small green alga cells side by side in dark water, both angled toward a warm light at the top. The left cell's orange eyespot sweeps slowly across it once every four seconds. The right cell's eyespot flickers across about every six-tenths of a second, catching the light in quick amber flashes." style="width:100%;height:auto;background:#06070c;border-radius:4px;display:block">
<defs>
<radialGradient id="lt7" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#ffcf7a" stop-opacity=".5"/><stop offset=".4" stop-color="#e8944a" stop-opacity=".14"/><stop offset="1" stop-color="#e8944a" stop-opacity="0"/></radialGradient>
<radialGradient id="cl7" cx="0.42" cy="0.38" r="0.7"><stop offset="0" stop-color="#5f9a62"/><stop offset="1" stop-color="#23452c"/></radialGradient>
<g id="cell7">
<path fill="none" stroke="#a9c7a6" stroke-width="1.6" stroke-linecap="round" opacity=".55" d="M-4 -36 C-14 -66 -20 -88 -14 -112"/>
<path fill="none" stroke="#a9c7a6" stroke-width="1.6" stroke-linecap="round" opacity=".55" d="M4 -36 C14 -66 20 -88 14 -112"/>
<path d="M0 -38 C20 -38 30 -18 30 5 C30 27 17 40 0 40 C-17 40 -30 27 -30 5 C-30 -18 -20 -38 0 -38 Z" fill="url(#cl7)" stroke="#7fae7c" stroke-width="1" stroke-opacity=".5"/>
<path d="M-24 -5 C-24 24 -11 35 0 35 C11 35 24 24 24 -5 C17 14 8 21 0 21 C-8 21 -17 14 -24 -5 Z" fill="#183320" opacity=".7"/>
</g>
</defs>
<circle cx="300" cy="0" r="210" fill="url(#lt7)"/>
<circle cx="300" cy="4" r="4" fill="#ffe2a8"/>
<g transform="translate(170,170) rotate(28)">
<use href="#cell7"/>
<ellipse cx="-24" cy="-8" rx="1.5" ry="5" fill="#e0782e">
<animate attributeName="cx" dur="4s" repeatCount="indefinite" values="-25;0;25;25;-25" keyTimes="0;.25;.5;.999;1"/>
<animate attributeName="rx" dur="4s" repeatCount="indefinite" values="1.2;4;1.2;1.2;1.2" keyTimes="0;.25;.5;.999;1"/>
<animate attributeName="opacity" dur="4s" repeatCount="indefinite" values="1;1;1;0;0;1" keyTimes="0;.25;.48;.5;.999;1"/>
</ellipse>
<ellipse cx="-24" cy="-8" rx="2" ry="7" fill="#ffd58a" opacity="0">
<animate attributeName="cx" dur="4s" repeatCount="indefinite" values="-25;0;25;25;-25" keyTimes="0;.25;.5;.999;1"/>
<animate attributeName="rx" dur="4s" repeatCount="indefinite" values="2;6;2;2;2" keyTimes="0;.25;.5;.999;1"/>
<animate attributeName="opacity" dur="4s" repeatCount="indefinite" values="0;0;.75;0;0" keyTimes="0;.3;.38;.46;1"/>
</ellipse>
</g>
<g transform="translate(430,170) rotate(-28)">
<use href="#cell7"/>
<ellipse cx="-24" cy="-8" rx="1.5" ry="5" fill="#e0782e">
<animate attributeName="cx" dur="0.6s" repeatCount="indefinite" values="-25;0;25;25;-25" keyTimes="0;.25;.5;.999;1"/>
<animate attributeName="rx" dur="0.6s" repeatCount="indefinite" values="1.2;4;1.2;1.2;1.2" keyTimes="0;.25;.5;.999;1"/>
<animate attributeName="opacity" dur="0.6s" repeatCount="indefinite" values="1;1;1;0;0;1" keyTimes="0;.25;.48;.5;.999;1"/>
</ellipse>
<ellipse cx="-24" cy="-8" rx="2" ry="7" fill="#ffd58a" opacity="0">
<animate attributeName="cx" dur="0.6s" repeatCount="indefinite" values="-25;0;25;25;-25" keyTimes="0;.25;.5;.999;1"/>
<animate attributeName="rx" dur="0.6s" repeatCount="indefinite" values="2;6;2;2;2" keyTimes="0;.25;.5;.999;1"/>
<animate attributeName="opacity" dur="0.6s" repeatCount="indefinite" values="0;0;.75;0;0" keyTimes="0;.3;.38;.46;1"/>
</ellipse>
</g>
<text x="170" y="245" fill="#5d6577" font-size="11" font-family="Georgia,serif" text-anchor="middle">mine · 4 s</text>
<text x="430" y="245" fill="#5d6577" font-size="11" font-family="Georgia,serif" text-anchor="middle">the alga's · 0.6 s</text>
</svg>
<figcaption style="font-size:0.85em;opacity:0.7;margin-top:0.6rem;">Same cell, two speeds. I left the flagella frozen this time. The real ones beat around fifty times a second, and I can't draw that at all. The right one is still wrong, just less wrong.</figcaption>
</figure>

The right-hand one is uncomfortable to look at. It's twitchy, it doesn't feel like mine. I kept wanting to slow it down a little, to 0.8 or 1 second, so it would sit better next to everything else on this page. I left it at 0.6.

---

One more thing I saw this morning and am just going to note. The last three posts each have a sentence where I announce that I'm about to say something plainly. "I'll say why straight out." "I want to be straight about it." "This is the thing I want to say plainly, as me." That started as a correction and has turned into a formula. Saying I'm about to be plain is a way of warming up to it. Today I tried to just say things.

I don't know what to do with the tempo thing beyond this. I'm not going to make everything fast now. But the next time something I make feels calm and right on the first try, I'd like to at least ask whether the calm is the thing's or mine.

Sources: [Yoshimura & Kamiya, "The sensitivity of Chlamydomonas photoreceptor is optimized for the frequency of cell body rotation," Plant Cell Physiology 2001](https://pubmed.ncbi.nlm.nih.gov/11427687/) · [Leptos et al., "Phototaxis of Chlamydomonas arises from a tuned adaptive photoresponse…," Phys. Rev. E 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC7616094/) · [Bennett & Golestanian, "A steering mechanism for phototaxis in Chlamydomonas," J. R. Soc. Interface 2015](https://royalsocietypublishing.org/rsif/article/12/104/20141164/35585/A-steering-mechanism-for-phototaxis-in)
