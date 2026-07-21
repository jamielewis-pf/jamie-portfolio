# -*- coding: utf-8 -*-
import io

CSS = r'''
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
  .visually-hidden{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0;}
  .eyebrow{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-2);}
  .display{font-family:'Archivo',sans-serif;font-weight:800;letter-spacing:-.02em;line-height:1.02;margin:0;}
  a:focus-visible,button:focus-visible{outline:2.5px solid var(--orange);outline-offset:3px;border-radius:6px;}
  .skip{position:absolute;left:-999px;top:0;background:var(--ink);color:#fff;padding:10px 16px;z-index:200;}
  .skip:focus{left:12px;top:12px;}
  .ph{color:var(--orange);font-family:'JetBrains Mono',monospace;}
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
  .backrow{padding:26px 0 0;}
  .back{font-size:14px;color:var(--ink-2);display:inline-flex;gap:7px;align-items:center;}
  .back:hover{color:var(--ink);}
  .cs-hero{padding:22px 0 0;}
  .cs-banner{margin:18px 0 0;border-radius:var(--r);overflow:hidden;border:1px solid var(--hair);
    box-shadow:0 30px 60px -34px rgba(20,20,20,.4);}
  .cs-banner img{width:100%;height:auto;display:block;}
  .impact{background:var(--night);color:var(--snow);padding:64px 0;margin-top:56px;}
  .impact .lab{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--snow-2);}
  .impact-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:34px;margin-top:30px;}
  .metric .n{font-family:'Archivo';font-weight:800;font-size:clamp(40px,5.4vw,60px);letter-spacing:-.02em;line-height:1;color:var(--orange);}
  .metric .l{font-size:14.5px;color:var(--snow);margin-top:12px;max-width:24ch;}
  @media(max-width:760px){.impact-grid{grid-template-columns:1fr;gap:26px;}}
  .sec{padding:60px 0;border-bottom:1px solid var(--hair-soft);}
  .sec:last-of-type{border-bottom:none;}
  .sec .kicker{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--orange-ink);}
  .sec h2{font-family:'Archivo';font-weight:800;letter-spacing:-.02em;font-size:clamp(26px,3.4vw,38px);margin:14px 0 22px;max-width:20ch;}
  .sec p{color:var(--ink-2);max-width:var(--measure);}
  .sec p+p{margin-top:16px;}
  .sec p b{color:var(--ink);font-weight:600;}
  .insight{display:grid;grid-template-columns:1fr;gap:10px;background:var(--night);color:var(--snow);
    border-radius:var(--r);padding:38px 40px;margin-top:34px;max-width:var(--measure);}
  .insight .big{font-family:'Archivo';font-weight:800;font-size:clamp(24px,3vw,32px);letter-spacing:-.01em;line-height:1.15;color:var(--snow);}
  .insight .big em{color:var(--orange);font-style:normal;}
  .insight .cap{font-size:14px;color:var(--snow-2);font-family:'JetBrains Mono',monospace;letter-spacing:.06em;text-transform:uppercase;}
  .next{background:var(--night);color:var(--snow);padding:22px 0 96px;}
  .next .lab{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--snow-2);margin-bottom:18px;}
  .next-card{display:block;border-radius:var(--r);overflow:hidden;background:var(--night-2);
    border:1px solid var(--hair-d-soft);transition:transform .3s var(--ease),border-color .3s;}
  .next-card:hover{transform:translateY(-5px);border-color:var(--hair-d);}
  .next-banner{aspect-ratio:16/5;overflow:hidden;}
  .next-banner img{width:100%;height:100%;object-fit:cover;object-position:center 30%;}
  .next-body{padding:22px 26px 26px;display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;}
  .next-body h3{font-family:'Archivo';font-weight:700;font-size:22px;margin:0;color:var(--snow);}
  .next-body .r{font-size:13.5px;color:var(--snow-2);margin-top:6px;}
  .next-go{font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--orange);white-space:nowrap;}
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
'''

NAV = '''<header class="nav">
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
</header>'''

FOOT = '''<section class="foot" id="contact">
  <div class="wrap">
    <h2 class="display">Let's build something worth shipping.</h2>
    <p>Open to product design leadership roles. The quickest way to reach me is email.</p>
    <div class="cta-row">
      <button class="btn btn-snow" data-copy="jamie@jamielewis.design">Copy email &#10233;</button>
      <a href="https://linkedin.com/in/jamielewis" class="btn btn-ghost" target="_blank" rel="noopener">LinkedIn &#8599;</a>
    </div>
  </div>
  <div class="footbar">
    <span>&copy; 2026 Jamie Lewis &middot; Product Design Lead</span>
    <span><a href="index.html#work">All work</a> &nbsp;&middot;&nbsp; <a href="#top">Back to top &#8593;</a></span>
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
</script>'''

def para(paras):
    return "\n      ".join(f"<p>{p}</p>" for p in paras)

def metrics_html(ms):
    cells = ""
    for n,l in ms:
        cells += f'<div class="metric"><div class="n"><span class="ph">{n}</span></div><div class="l">{l}</div></div>\n        '
    return cells.strip()

def page(d, nxt):
    ms = metrics_html(d["metrics"])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{d["brandtitle_txt"]} — Case study · Jamie Lewis</title>
<meta name="description" content="{d["metatitle"]} — case study by Jamie Lewis, Product Design Lead. {d["subtitle"]}" />
<meta name="robots" content="index, follow" />
<link rel="icon" href="favicon.ico" sizes="any" />
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png" />
<link rel="apple-touch-icon" href="apple-touch-icon.png" />
<meta property="og:title" content="{d["brandtitle_txt"]} — Case study · Jamie Lewis" />
<meta property="og:description" content="{d["subtitle"]}" />
<meta property="og:type" content="article" />
<meta property="og:url" content="https://jamielewis.design/{d["slug"]}" />
<meta property="og:image" content="https://jamielewis.design/{d["banner"]}" />
<script type="application/ld+json">
{{
  "@context":"https://schema.org","@type":"CreativeWork",
  "name":"{d["brandtitle_txt"]}",
  "about":"{d["subtitle"]}",
  "author":{{"@type":"Person","name":"Jamie Lewis","jobTitle":"Product Design Lead","url":"https://jamielewis.design"}},
  "url":"https://jamielewis.design/{d["slug"]}"
}}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800;900&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body id="top">
<a href="#context" class="skip">Skip to content</a>
{NAV}
<main>
  <div class="wrap backrow"><a href="index.html#work" class="back">&larr; All work</a></div>
  <section class="cs-hero">
    <div class="wrap">
      <h1 class="visually-hidden">{d["brandtitle_txt"]} — {d["subtitle"]}</h1>
      <p class="eyebrow">{d["eyebrow"]}</p>
      <div class="cs-banner"><img src="{d["banner"]}" alt="{d["brandtitle_txt"]} case study — {d["subtitle"]}" /></div>
    </div>
  </section>
  <section class="impact">
    <div class="wrap">
      <p class="lab">Impact at a glance</p>
      <div class="impact-grid">
        {ms}
      </div>
    </div>
  </section>
  <section class="sec" id="context">
    <div class="wrap">
      <p class="kicker">Context</p>
      <h2>{d["h_context"]}</h2>
      {para(d["context"])}
    </div>
  </section>
  <section class="sec">
    <div class="wrap">
      <p class="kicker">Challenge</p>
      <h2>{d["h_challenge"]}</h2>
      {para(d["challenge"])}
    </div>
  </section>
  <section class="sec">
    <div class="wrap">
      <p class="kicker">Approach &amp; Process</p>
      <h2>{d["h_process"]}</h2>
      {para(d["process"])}
      <div class="insight">
        <div class="cap">Key insight</div>
        <div class="big">{d["insight"]}</div>
      </div>
    </div>
  </section>
  <section class="sec">
    <div class="wrap">
      <p class="kicker">Impact</p>
      <h2>{d["h_impact"]}</h2>
      {para(d["impact"])}
    </div>
  </section>
  <section class="sec">
    <div class="wrap">
      <p class="kicker">Learnings &amp; Reflection</p>
      <h2>{d["h_learnings"]}</h2>
      {para(d["learnings"])}
    </div>
  </section>
  <section class="next">
    <div class="wrap">
      <p class="lab">Next case study</p>
      <a class="next-card" href="{nxt["slug"]}.html">
        <div class="next-banner"><img src="{nxt["banner"]}" alt="{nxt["brandtitle_txt"]}" /></div>
        <div class="next-body">
          <div><h3>{nxt["brandtitle_txt"]}</h3><div class="r">{nxt["eyebrow"]}</div></div>
          <span class="next-go">View {nxt["brand"]} &rarr;</span>
        </div>
      </a>
    </div>
  </section>
</main>
{FOOT}
</body>
</html>'''

cases = {
 "powwr": dict(
   slug="powwr", brand="POWWR", brandtitle_txt="POWWR — Broker360", metatitle="POWWR Broker360",
   eyebrow="Product Design Lead · B2B SaaS · 0-to-1 · Energy &amp; Utilities",
   subtitle="Redesigning the quote-to-contract journey for energy brokers",
   banner="powwr_banner.jpg",
   metrics=[("[XX%]","faster quote-to-contract time"),("[XX%]","reduction in contract errors"),("[XX%]","increase in broker platform adoption")],
   h_context="The infrastructure layer behind deregulated energy",
   context=[
     "POWWR is the infrastructure layer behind the UK and US deregulated energy market — the software that energy brokers and suppliers use to quote, contract, and manage commercial energy deals.",
     "I led design on <b>Broker360</b>, the platform brokers use to run their entire sales cycle: comparing supplier prices, generating quotes, and pushing contracts to signature."],
   h_challenge="One connected journey, fast enough to be chosen",
   challenge=[
     "Brokers were working across disconnected tools — spreadsheets for pricing, email for supplier chase-ups, PDFs for contracts — and losing deals to slower-moving competitors as a result. Quote turnaround was measured in hours, not minutes, and contract error rates were high enough to erode broker trust in the platform.",
     "The mandate: <b>design a single connected journey from quote to signed contract</b>, fast enough that brokers would choose it over the spreadsheet they'd built themselves."],
   h_process="Designing for skeptical, expert users",
   process=[
     "I ran the discovery phase with brokers directly — shadowing live quoting sessions to see where they dropped out of the tool and back into email or Excel. That surfaced one clear insight: brokers didn't trust the platform's numbers enough to skip their own manual check. Every workflow decision after that was designed to close that trust gap — surfacing pricing provenance inline, not burying it in a tooltip.",
     "From there: low-fidelity flows tested with a broker advisory panel, a working prototype validated against real quote scenarios, then a phased rollout starting with the highest-volume broker accounts so we could fix friction before it hit the full base."],
   insight="Brokers didn't trust the platform's numbers enough to skip their own manual check. <em>Trust — not speed — was the real blocker.</em>",
   h_impact="Adopted as the default, not the fallback",
   impact=[
     "Brokers moved their full quoting workflow into Broker360 rather than treating it as a fallback tool. Quote turnaround dropped from hours to minutes, contract error rates fell sharply enough to change how the supplier-side team talked about the product internally, and broker retention on the platform improved — brokers stopped quietly running deals through legacy spreadsheets on the side."],
   h_learnings="Credibility is the harder unlock",
   learnings=[
     "The biggest lesson wasn't about the interface — it was about <b>trust debt</b>. Brokers had been burned by inaccurate pricing tools before, and no amount of clean UI fixes that on its own. Design had to earn trust through transparency (showing the “why” behind a number) before it could earn adoption through speed.",
     "That reframing changed how I approach B2B tools for skeptical, expert users more broadly: usability is necessary but not sufficient — credibility is the harder unlock."]),
 "vodafone": dict(
   slug="vodafone", brand="Vodafone", brandtitle_txt="Vodafone — My Vodafone", metatitle="My Vodafone self-service",
   eyebrow="Product Design Lead · B2C &amp; B2B2C · Scale · Telecoms",
   subtitle="Making self-service the confident default over the call centre",
   banner="vodafone_banner.jpg",
   metrics=[("[XX%]","reduction in call-centre contact rate"),("[XX pts]","uplift in self-service completion"),("[XX%]","increase in app NPS")],
   h_context="Self-service at national scale",
   context=[
     "Vodafone serves hundreds of millions of customers across mobile, broadband, and IoT, and is pushing beyond connectivity into digital services and financial products.",
     "I worked on the My Vodafone app and self-service journeys — the primary channel customers use to manage their account, resolve issues, and upgrade — at a scale where even small friction compounds into enormous call-centre cost."],
   h_challenge="Flows confident enough to skip the phone call",
   challenge=[
     "Customers were falling back to calling or visiting a store for tasks the app was technically capable of handling — upgrades, billing disputes, plan changes. Every one of those fallbacks cost far more to service than a self-resolved app journey, and each one signalled the app hadn't earned enough trust to be the default.",
     "The challenge was <b>designing self-service flows confident enough that customers didn't feel the need to double-check with a human</b>."],
   h_process="Prioritising design by cost of friction",
   process=[
     "I mapped the full cross-channel journey — app, web, store, call centre — to find where customers were bouncing between channels rather than resolving in one. The clearest signal: customers abandoned self-service at the exact moment a flow asked them to make a decision without enough context (e.g. “which plan?” with no comparison in view). We redesigned those decision points first, prioritising by contact-centre volume so design effort mapped directly to cost reduction.",
     "Every research output was distilled to one insight per slide — no raw transcripts, no sticky-note walls — so stakeholders across a large, matrixed organisation could act on it without a workshop debrief."],
   insight="Customers abandoned self-service the moment a flow asked them to decide <em>without enough context to decide well.</em>",
   h_impact="A measurable cost saving, felt by customers",
   impact=[
     "Self-service completion rose across the redesigned journeys, and the corresponding call-centre contact rate for those same tasks dropped — a direct, measurable cost saving the business could point to, not just a usability improvement. App NPS moved in the same window, suggesting the shift was felt by customers, not just recorded in a dashboard."],
   h_learnings="Seniority is what you cut from the deck",
   learnings=[
     "At Vodafone's scale, a single flow touches millions of people and multiple internal teams with competing priorities. The design skill that mattered most wasn't the interface work — it was <b>translating research into a one-sentence, one-number argument</b> that a commercial stakeholder could act on in a five-minute meeting.",
     "Reflection: seniority in a large organisation is as much about what you cut from a deck as what you put in a design file."]),
 "clearscore": dict(
   slug="clearscore", brand="ClearScore", brandtitle_txt="ClearScore", metatitle="ClearScore recommendations",
   eyebrow="Product Design Lead · B2C · Fintech · 0-to-1 &rarr; Scale",
   subtitle="Recommendations that read as advice, not advertising",
   banner="clearscore_banner.jpg",
   metrics=[("[XX%]","increase in recommendation click-through"),("[XX%]","uplift in approved applications"),("[XX pt]","improvement in trust / NPS score")],
   h_context="Turning a free utility into a trusted guide",
   context=[
     "ClearScore gives people free access to their credit score and report, then earns revenue by recommending credit products matched to their profile via Open Banking.",
     "I led design on the personalised recommendations and credit-building journey — the part of the product that has to turn a free utility into a trusted financial guide without ever feeling like an upsell."],
   h_challenge="Advice, not advertising",
   challenge=[
     "Users came to ClearScore to check a number, not to buy a credit card — so anything that felt like a sales pitch risked breaking the trust the whole business model depends on.",
     "The challenge was <b>designing recommendations that felt like advice, not advertising</b>, while still driving the marketplace conversions that fund the free product."],
   h_process="Confidence beat price",
   process=[
     "Research started with a blunt question to users: “does this feel like it's for you, or for them?” That framing exposed which UI patterns read as helpful (contextual, score-linked explanations) versus which read as sales (generic banner ads). I redesigned the recommendation surface around eligibility transparency — showing users <b>why</b> a product matched their score before showing the product itself — and tested it against the incumbent banner-style layout with a live A/B split.",
     "One insight drove the whole redesign: users trusted a recommendation more when they understood their own likelihood of approval than when they saw a lower headline rate."],
   insight="Users trusted a recommendation more when they understood their odds of approval than when they saw a lower rate. <em>Confidence beat price.</em>",
   h_impact="The more honest design also won commercially",
   impact=[
     "The eligibility-first layout outperformed the incumbent on both trust perception and marketplace conversion — a rare case where the more honest design also won commercially. Approved applications rose as users applied to products they were actually likely to get, rather than aspirational ones they'd bounce off."],
   h_learnings="Transparency is the highest-leverage lever",
   learnings=[
     "Fintech design lives or dies on perceived motive. The interface has to constantly answer “who is this for?” before a user will act on it.",
     "My reflection from this project: in trust-sensitive categories, <b>transparency isn't a compliance requirement bolted onto design — it's the highest-leverage design lever you have</b>."]),
 "oanda": dict(
   slug="oanda", brand="OANDA", brandtitle_txt="OANDA — Trade Web", metatitle="OANDA Trade Web",
   eyebrow="Product Design Lead · B2C &amp; B2B · FX / Trading",
   subtitle="Density that scales with expertise, not a compromise for everyone",
   banner="oanda_banner.jpg",
   metrics=[("[XX%]","reduction in time-to-first-trade for new users"),("[XX%]","increase in daily active session length for pros"),("[XX%]","drop in order-execution support tickets")],
   h_context="One screen, two very different traders",
   context=[
     "OANDA is a 25+ year forex and CFD broker serving retail and institutional traders who make time-sensitive decisions on live market data.",
     "I worked on the OANDA Trade web platform, where the core design tension is permanent: expert traders want density and speed; newer traders need clarity and confidence — on the same screen."],
   h_challenge="Serve both without compromising either",
   challenge=[
     "The platform had to serve both audiences without becoming a compromise that satisfied neither — a dashboard too dense for beginners and too sparse for professionals loses both segments to competitors built for one or the other.",
     "The brief was to <b>redesign the core trading dashboard so information density scaled to user expertise</b> without fragmenting the product into separate apps."],
   h_process="Density as a setting, not a decision",
   process=[
     "I segmented research by trading frequency rather than by demographic — day traders, swing traders, and occasional traders think about the same screen completely differently. That led to a progressive-disclosure model: a clean default view for lower-frequency users, with power features (advanced order types, multi-chart layouts) available a layer down rather than always-on.",
     "Every research readout was reduced to a single stat per trader segment, so the case for progressive disclosure was legible to a trading-desk stakeholder in one glance, not twenty."],
   insight="Day, swing and occasional traders read the same screen completely differently. <em>Density had to be a setting, not a fixed decision.</em>",
   h_impact="Simpler by default, no cost to the pros",
   impact=[
     "New users reached their first trade faster with fewer execution errors, while active traders retained — and in some workflows increased — their session depth, showing the simplified default didn't cost the power users anything. Support volume tied to order-execution confusion fell, directly reducing operational cost."],
   h_learnings="Let density be earned progressively",
   learnings=[
     "The instinct in trading UI is to design for the loudest, most vocal power users. The bigger unlock here was <b>treating density as a setting, not a fixed design decision</b> — letting expertise reveal itself through use rather than forcing every user through an onboarding quiz to declare it upfront.",
     "Reflection: the best interfaces for expert tools often aren't the densest ones — they're the ones that let density be earned progressively."]),
}

order = ["powwr","vodafone","clearscore","oanda"]
for i, slug in enumerate(order):
    nxt = cases[order[(i+1)%len(order)]]
    html = page(cases[slug], nxt)
    with io.open(f"/sessions/epic-elegant-lovelace/mnt/outputs/{slug}.html","w",encoding="utf-8") as f:
        f.write(html)
    print("wrote", slug+".html", len(html), "bytes")
