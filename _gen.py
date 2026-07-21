import io

TEMPLATE = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>%%BRAND%% — Case study · Jamie Lewis</title>
<meta name="description" content="%%BRAND%% case study by Jamie Lewis, Product Design Lead. %%SUMMARY%%" />
<meta name="robots" content="index, follow" />
<link rel="icon" href="favicon.ico" sizes="any" />
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png" />
<link rel="apple-touch-icon" href="apple-touch-icon.png" />
<meta property="og:title" content="%%BRAND%% — Case study · Jamie Lewis" />
<meta property="og:description" content="%%SUMMARY%%" />
<meta property="og:type" content="article" />
<meta property="og:url" content="https://jamielewis.design/%%SLUG%%" />
<meta property="og:image" content="https://jamielewis.design/jamie.jpg" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800;900&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
  :root{
    --paper:#F6F5F2;--paper-2:#EFEEEA;--ink:#141414;--ink-2:#5E5E5B;
    --hair:rgba(20,20,20,.14);--hair-soft:rgba(20,20,20,.08);
    --orange:#FF4A17;--orange-ink:#B22E06;
    --night:#0C0C0D;--night-2:#141416;--snow:#F4F3F0;--snow-2:#9C9C98;
    --hair-d:rgba(255,255,255,.14);--hair-d-soft:rgba(255,255,255,.07);
    --maxw:1180px;--measure:720px;--r:16px;--ease:cubic-bezier(.22,.61,.36,1);
  }
  *{box-sizing:border-box;}
  html{scroll-behavior:smooth;}
  body{margin:0;background:var(--paper);color:var(--ink);
    font-family:'Inter',system-ui,-apple-system,sans-serif;font-size:17px;line-height:1.6;
    -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;}
  a{color:inherit;text-decoration:none;}
  img,svg{display:block;max-width:100%;}
  ::selection{background:var(--orange);color:#fff;}
  .wrap{max-width:var(--maxw);margin:0 auto;padding:0 28px;}
  .measure{max-width:var(--measure);}
  .eyebrow{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-2);}
  .display{font-family:'Archivo',sans-serif;font-weight:800;letter-spacing:-.02em;line-height:1.02;margin:0;}
  a:focus-visible,button:focus-visible{outline:2.5px solid var(--orange);outline-offset:3px;border-radius:6px;}
  .skip{position:absolute;left:-999px;top:0;background:var(--ink);color:#fff;padding:10px 16px;z-index:200;}
  .skip:focus{left:12px;top:12px;}
  /* placeholder styling — remove the .ph class once real copy is in */
  .ph{color:var(--orange-ink);background:rgba(255,74,23,.08);
    border:1px dashed rgba(255,74,23,.45);border-radius:8px;padding:2px 7px;
    font-family:'JetBrains Mono',monospace;font-size:.82em;}
  /* nav */
  .nav{position:sticky;top:0;z-index:100;background:rgba(246,245,242,.82);
    backdrop-filter:saturate(1.4) blur(10px);border-bottom:1px solid var(--hair-soft);}
  .nav .row{display:flex;align-items:center;justify-content:space-between;height:72px;}
  .brand{display:flex;align-items:center;gap:11px;}
  .brand .avatar{width:38px;height:38px;border-radius:50%;object-fit:cover;border:1px solid var(--hair);flex:none;}
  .brand-text{display:flex;flex-direction:column;line-height:1.12;}
  .brand-name{font-weight:600;font-size:15px;letter-spacing:-.01em;color:var(--ink);}
  .brand-role{font-weight:400;font-size:12px;color:var(--ink-2);letter-spacing:.01em;}
  .navlinks{display:flex;gap:30px;font-size:14.5px;color:var(--ink-2);}
  .navlinks a:hover{color:var(--ink);}
  .btn{font-family:'Inter';font-size:14.5px;font-weight:600;border:none;cursor:pointer;
    border-radius:999px;padding:11px 20px;transition:transform .18s var(--ease),background .18s;
    display:inline-flex;align-items:center;gap:8px;}
  .btn:active{transform:translateY(1px);}
  .btn-orange{background:var(--orange);color:#fff;}
  .btn-orange:hover{background:#ff5b2c;}
  .btn-ghost{background:transparent;color:var(--ink);border:1px solid var(--hair);}
  .btn-ghost:hover{background:rgba(20,20,20,.05);}
  @media(max-width:720px){.navlinks{display:none;}}
  /* back link */
  .backrow{padding:26px 0 0;}
  .back{font-size:14px;color:var(--ink-2);display:inline-flex;gap:7px;align-items:center;}
  .back:hover{color:var(--ink);}
  /* hero */
  .cs-hero{padding:34px 0 20px;}
  .cs-hero .eyebrow{margin-bottom:16px;}
  .cs-hero h1{font-size:clamp(38px,5.6vw,68px);max-width:20ch;margin:0;}
  .cs-hero .meta{font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--ink-2);margin-top:20px;letter-spacing:.03em;}
  .cs-hero .summary{font-size:clamp(18px,2.1vw,22px);color:var(--ink-2);max-width:56ch;margin:22px 0 0;}
  .cs-hero .summary b{color:var(--ink);font-weight:600;}
  /* banner */
  .cs-banner{margin:36px 0 0;border-radius:var(--r);overflow:hidden;border:1px solid var(--hair);aspect-ratio:16/6;}
  .cs-banner svg{width:100%;height:100%;}
  /* impact strip (reverse storytelling — results up top) */
  .impact{background:var(--night);color:var(--snow);padding:64px 0;margin-top:56px;}
  .impact .lab{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--snow-2);}
  .impact-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:34px;margin-top:30px;}
  .metric .n{font-family:'Archivo';font-weight:800;font-size:clamp(44px,6vw,68px);letter-spacing:-.02em;line-height:1;color:var(--orange);}
  .metric .l{font-size:14.5px;color:var(--snow);margin-top:12px;max-width:22ch;}
  @media(max-width:760px){.impact-grid{grid-template-columns:1fr;gap:26px;}}
  /* content sections */
  .sec{padding:64px 0;border-bottom:1px solid var(--hair-soft);}
  .sec:last-of-type{border-bottom:none;}
  .sec .kicker{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--orange-ink);}
  .sec h2{font-family:'Archivo';font-weight:800;letter-spacing:-.02em;font-size:clamp(26px,3.4vw,38px);margin:14px 0 22px;max-width:18ch;}
  .sec p{color:var(--ink-2);max-width:var(--measure);}
  .sec p+p{margin-top:16px;}
  .sec p b{color:var(--ink);font-weight:600;}
  /* research visual placeholder — one insight per visual */
  .insight{display:grid;grid-template-columns:1.1fr .9fr;gap:28px;align-items:center;
    background:#fff;border:1px solid var(--hair);border-radius:var(--r);padding:30px;margin-top:30px;}
  .insight .big{font-family:'Archivo';font-weight:800;font-size:clamp(34px,4.5vw,52px);letter-spacing:-.02em;line-height:1;color:var(--ink);}
  .insight .big em{color:var(--orange);font-style:normal;}
  .insight .cap{font-size:15px;color:var(--ink-2);margin-top:14px;max-width:34ch;}
  .insight .frame{aspect-ratio:4/3;border-radius:12px;background:var(--paper-2);
    border:1px dashed var(--hair);display:flex;align-items:center;justify-content:center;
    font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--ink-2);text-align:center;padding:18px;}
  @media(max-width:760px){.insight{grid-template-columns:1fr;}}
  /* device mock placeholder */
  .shots{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:30px;}
  .shot{aspect-ratio:9/17;border-radius:22px;background:#fff;border:1px solid var(--hair);
    box-shadow:0 24px 48px -28px rgba(20,20,20,.35);display:flex;align-items:center;justify-content:center;
    font-family:'JetBrains Mono',monospace;font-size:11.5px;color:var(--ink-2);text-align:center;padding:20px;}
  @media(max-width:760px){.shots{grid-template-columns:1fr 1fr;}}
  /* next case */
  .next{background:var(--night);color:var(--snow);padding:20px 0 96px;}
  .next .lab{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--snow-2);margin-bottom:18px;}
  .next-card{display:block;border-radius:var(--r);overflow:hidden;background:var(--night-2);
    border:1px solid var(--hair-d-soft);transition:transform .3s var(--ease),border-color .3s;}
  .next-card:hover{transform:translateY(-5px);border-color:var(--hair-d);}
  .next-banner{position:relative;aspect-ratio:16/5;overflow:hidden;}
  .next-banner svg{position:absolute;inset:0;width:100%;height:100%;}
  .next-body{padding:24px 26px 28px;display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;}
  .next-body h3{font-family:'Archivo';font-weight:700;font-size:22px;margin:0;color:var(--snow);}
  .next-body .r{font-size:13.5px;color:var(--snow-2);margin-top:6px;}
  .next-go{font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--orange);white-space:nowrap;}
  /* footer */
  .foot{background:var(--night);color:var(--snow);padding:90px 0 40px;text-align:center;}
  .foot h2{font-size:clamp(34px,5vw,60px);color:var(--snow);max-width:16ch;margin:0 auto;}
  .foot p{color:var(--snow-2);margin:20px auto 30px;max-width:40ch;font-size:17px;}
  .foot .cta-row{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;}
  .foot .btn-ghost{color:var(--snow);border-color:var(--hair-d);}
  .foot .btn-ghost:hover{background:rgba(255,255,255,.06);}
  .foot .btn-snow{background:var(--snow);color:var(--night);}
  .footbar{max-width:var(--maxw);margin:70px auto 0;padding:26px 28px 0;border-top:1px solid var(--hair-d-soft);
    display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;font-size:13px;color:var(--snow-2);}
  .footbar a:hover{color:var(--snow);}
  .toast{position:fixed;bottom:24px;left:50%;transform:translate(-50%,20px);background:var(--ink);color:#fff;
    padding:12px 20px;border-radius:999px;font-size:14px;opacity:0;pointer-events:none;transition:.3s var(--ease);z-index:300;}
  .toast.show{opacity:1;transform:translate(-50%,0);}
  .reveal{opacity:0;transform:translateY(18px);transition:opacity .7s var(--ease),transform .7s var(--ease);}
  .reveal.in{opacity:1;transform:none;}
  @media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important;}.reveal{opacity:1;transform:none;}html{scroll-behavior:auto;}}
</style>
</head>
<body id="top">
<a href="#context" class="skip">Skip to content</a>
<!-- ============ NAV ============ -->
<header class="nav">
  <div class="wrap row">
    <a href="index.html" class="brand" aria-label="Jamie Lewis — Product Design Lead">
      <img class="avatar" src="jamie.jpg" alt="Jamie Lewis" width="38" height="38" />
      <span class="brand-text">
        <span class="brand-name">Jamie Lewis</span>
        <span class="brand-role">Product Design Lead</span>
      </span>
    </a>
    <nav class="navlinks">
      <a href="index.html#work">Work</a>
      <a href="index.html#about">About</a>
      <a href="index.html#contact">Contact</a>
    </nav>
    <a href="index.html#contact" class="btn btn-orange">Get in touch</a>
  </div>
</header>
<main>
  <div class="wrap backrow"><a href="index.html#work" class="back">← All work</a></div>
  <!-- ============ HERO ============ -->
  <section class="cs-hero">
    <div class="wrap">
      <p class="eyebrow">%%SECTOR%%</p>
      <h1 class="display">%%TITLE%%</h1>
      <p class="meta">%%ROLE%%</p>
      <p class="summary">%%SUMMARY_RICH%%</p>
      <div class="cs-banner" aria-hidden="true">%%BANNER%%</div>
    </div>
  </section>
  <!-- ============ IMPACT (reverse storytelling: results first) ============ -->
  <section class="impact">
    <div class="wrap">
      <p class="lab">Impact</p>
      <div class="impact-grid">
        <div class="metric"><div class="n">%%M1N%%</div><div class="l">%%M1L%%</div></div>
        <div class="metric"><div class="n">%%M2N%%</div><div class="l">%%M2L%%</div></div>
        <div class="metric"><div class="n">%%M3N%%</div><div class="l">%%M3L%%</div></div>
      </div>
    </div>
  </section>
  <!-- ============ CONTEXT ============ -->
  <section class="sec" id="context">
    <div class="wrap">
      <p class="kicker">Context</p>
      <h2>What was the situation?</h2>
      <p><span class="ph">[Add copy: the business context. Company, product, market, your remit, team shape, timeline.]</span></p>
      <p><span class="ph">[Add copy: why this mattered now — the strategic or commercial pressure behind the work.]</span></p>
    </div>
  </section>
  <!-- ============ CHALLENGE ============ -->
  <section class="sec">
    <div class="wrap">
      <p class="kicker">Challenge</p>
      <h2>The problem worth solving</h2>
      <p><span class="ph">[Add copy: the core problem, the constraints, and what made it hard. Frame it around users AND the business.]</span></p>
      <div class="insight">
        <div>
          <div class="big"><em>[Stat]</em> [one-line takeaway]</div>
          <div class="cap"><span class="ph">[Add copy: one insight per visual. One sentence. One number. One takeaway.]</span></div>
        </div>
        <div class="frame">[ Clean research visual — replace with an exported chart or diagram ]</div>
      </div>
    </div>
  </section>
  <!-- ============ PROCESS / APPROACH ============ -->
  <section class="sec">
    <div class="wrap">
      <p class="kicker">Approach &amp; Process</p>
      <h2>How I worked the problem</h2>
      <p><span class="ph">[Add copy: your approach — research, framing, key decisions, trade-offs, collaboration with product/eng.]</span></p>
      <p><span class="ph">[Add copy: the pivotal design decision and why you made it. Show judgement, not just activity.]</span></p>
      <div class="shots">
        <div class="shot">[ App screen 1 — realistic device mock on abstract background ]</div>
        <div class="shot">[ App screen 2 ]</div>
        <div class="shot">[ App screen 3 ]</div>
      </div>
    </div>
  </section>
  <!-- ============ IMPACT DETAIL ============ -->
  <section class="sec">
    <div class="wrap">
      <p class="kicker">Impact</p>
      <h2>What changed as a result</h2>
      <p><span class="ph">[Add copy: outcomes in full — the metrics above, plus qualitative impact, adoption, and business result.]</span></p>
    </div>
  </section>
  <!-- ============ LEARNINGS ============ -->
  <section class="sec">
    <div class="wrap">
      <p class="kicker">Learnings &amp; Reflection</p>
      <h2>What I'd carry forward</h2>
      <p><span class="ph">[Add copy: honest reflection. What worked, what you'd do differently, what it taught you as a lead. This is what separates seniors from juniors.]</span></p>
    </div>
  </section>
  <!-- ============ NEXT CASE ============ -->
  <section class="next">
    <div class="wrap">
      <p class="lab">Next case study</p>
      <a class="next-card" href="%%NEXT_SLUG%%.html">
        <div class="next-banner">%%NEXT_BANNER%%</div>
        <div class="next-body">
          <div>
            <h3>%%NEXT_TITLE%%</h3>
            <div class="r">%%NEXT_SECTOR%%</div>
          </div>
          <span class="next-go">View %%NEXT_BRAND%% →</span>
        </div>
      </a>
    </div>
  </section>
</main>
<!-- ============ FOOTER ============ -->
<section class="foot" id="contact">
  <div class="wrap">
    <h2 class="display">Let's build something worth shipping.</h2>
    <p>Open to product design leadership roles. The quickest way to reach me is email.</p>
    <div class="cta-row">
      <button class="btn btn-snow" data-copy="jamie@jamielewis.design">Copy email ⧉</button>
      <a href="https://linkedin.com/in/jamielewis" class="btn btn-ghost" target="_blank" rel="noopener">LinkedIn ↗</a>
    </div>
  </div>
  <div class="footbar">
    <span>© 2026 Jamie Lewis · Product Design Lead</span>
    <span><a href="index.html#work">All work</a> &nbsp;·&nbsp; <a href="#top">Back to top ↑</a></span>
  </div>
</section>
<div class="toast" id="toast">Email copied</div>
<script>
  const toast=document.getElementById('toast');
  document.querySelectorAll('[data-copy]').forEach(btn=>{
    btn.addEventListener('click',async()=>{
      const val=btn.getAttribute('data-copy');
      try{await navigator.clipboard.writeText(val);}
      catch(e){const t=document.createElement('textarea');t.value=val;document.body.appendChild(t);t.select();document.execCommand('copy');t.remove();}
      toast.textContent=val+' copied';toast.classList.add('show');
      setTimeout(()=>toast.classList.remove('show'),1800);
    });
  });
  const io=new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12});
  document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
</script>
</body>
</html>'''

def banner(idp, c1, c2, label, size, ls, extra=""):
    return (f'<svg viewBox="0 0 640 240" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">'
            f'<defs><radialGradient id="{idp}" cx="72%" cy="26%" r="80%">'
            f'<stop offset="0" stop-color="{c1}"/><stop offset="100%" stop-color="{c2}"/></radialGradient></defs>'
            f'<rect width="640" height="240" fill="url(#{idp})"/>{extra}'
            f'<text x="50%" y="53%" text-anchor="middle" dominant-baseline="middle" '
            f'font-family="Archivo,sans-serif" font-weight="800" font-size="{size}" '
            f'letter-spacing="{ls}" fill="#ffffff">{label}</text></svg>')

cases = {
 "powwr": dict(brand="POWWR", sector="Energy · B2B SaaS", slug="powwr",
   title="Rebuilding the broker &amp; supplier energy platform",
   role="Design Lead · 0-to-1 · 2023–now",
   summary="Cut quote-to-contract time by 60% across the broker journey.",
   summary_rich="Leading design on a ground-up rebuild of the platform brokers and suppliers use to quote, compare and close energy contracts — <b>0-to-1, from strategy to shipped</b>.",
   m=[("60%","faster quote-to-contract across the broker journey"),
      ("[x]","[add a second headline metric]"),
      ("[x]","[add a third headline metric]")],
   c1="#1b4a6b", c2="#00253E", size="74", ls="4",
   extra='<circle cx="560" cy="52" r="7" fill="#FFAD21"/>'),
 "vodafone": dict(brand="Vodafone", sector="Telecoms · B2C", slug="vodafone",
   title="A unified self-serve app for 40M+ customers",
   role="Senior Product Designer · 2020–2022",
   summary="Lifted task completion to 92% and cut support calls sharply.",
   summary_rich="Unifying fragmented self-serve journeys into a single app used by <b>40M+ customers</b> — reducing effort, calls and confusion at national scale.",
   m=[("92%","task completion, up from a fragmented baseline"),
      ("[x]","[add a second headline metric]"),
      ("[x]","[add a third headline metric]")],
   c1="#ff3b30", c2="#C20000", size="58", ls="-1", extra=""),
 "clearscore": dict(brand="ClearScore", sector="Fintech · B2C", slug="clearscore",
   title="Making credit scores make sense",
   role="Senior Product Designer · 2018–2020",
   summary="+28% activation from a redesigned score-first onboarding.",
   summary_rich="Turning an intimidating credit score into something people understand and act on — a <b>score-first onboarding</b> that lifted activation.",
   m=[("+28%","activation from score-first onboarding"),
      ("[x]","[add a second headline metric]"),
      ("[x]","[add a third headline metric]")],
   c1="#16C9B6", c2="#0B3B45", size="52", ls="-1", extra=""),
 "oanda": dict(brand="OANDA", sector="Fintech · Trading", slug="oanda",
   title="Making FX trading legible for first-timers",
   role="Product Designer · 2016–2018",
   summary="2.1× more first trades after a rebuilt onboarding flow.",
   summary_rich="Rebuilding onboarding so first-time traders could understand risk and place their first FX trade with confidence — <b>2.1× more first trades</b>.",
   m=[("2.1×","more first trades after rebuilt onboarding"),
      ("[x]","[add a second headline metric]"),
      ("[x]","[add a third headline metric]")],
   c1="#1B4DA0", c2="#0A2540", size="68", ls="3",
   extra='<circle cx="92" cy="190" r="6" fill="#C9A227"/>'),
}

order = ["powwr","vodafone","clearscore","oanda"]

for i, slug in enumerate(order):
    d = cases[slug]
    nxt = cases[order[(i+1) % len(order)]]
    html = TEMPLATE
    html = html.replace("%%BRAND%%", d["brand"])
    html = html.replace("%%SECTOR%%", d["sector"])
    html = html.replace("%%SLUG%%", d["slug"])
    html = html.replace("%%TITLE%%", d["title"])
    html = html.replace("%%ROLE%%", d["role"])
    html = html.replace("%%SUMMARY_RICH%%", d["summary_rich"])
    html = html.replace("%%SUMMARY%%", d["summary"])
    html = html.replace("%%BANNER%%", banner("b_"+slug, d["c1"], d["c2"], d["brand"], d["size"], d["ls"], d["extra"]))
    html = html.replace("%%M1N%%", d["m"][0][0]).replace("%%M1L%%", d["m"][0][1])
    html = html.replace("%%M2N%%", d["m"][1][0]).replace("%%M2L%%", d["m"][1][1])
    html = html.replace("%%M3N%%", d["m"][2][0]).replace("%%M3L%%", d["m"][2][1])
    html = html.replace("%%NEXT_SLUG%%", nxt["slug"])
    html = html.replace("%%NEXT_TITLE%%", nxt["title"])
    html = html.replace("%%NEXT_SECTOR%%", nxt["sector"])
    html = html.replace("%%NEXT_BRAND%%", nxt["brand"])
    html = html.replace("%%NEXT_BANNER%%", banner("nb_"+slug, nxt["c1"], nxt["c2"], nxt["brand"], "44", nxt["ls"]))
    with io.open(f"/sessions/epic-elegant-lovelace/mnt/outputs/{slug}.html","w",encoding="utf-8") as f:
        f.write(html)
    print("wrote", slug+".html")
