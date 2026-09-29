#!/usr/bin/env python3
"""Builds the PABOTO site: index.html, services.html and one page per project in work/.

Edit the PROJECTS list (or the page templates below) and run:  python3 build.py
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://paboto.com"
EMAIL = "stephanie@paboto.com"
PHONE = "+45 25 11 22 61"
PHONE_TEL = "+4525112261"
INSTAGRAM = "https://www.instagram.com/stephaniepabotoy/"
LINKEDIN = "https://www.linkedin.com/in/stephaniepabotoy"

SECTORS = ["Food & drink", "Hospitality", "Culture", "Fashion", "Film", "Corporate"]

# Each project: slug, title, client, sectors, services, result (short), cover, images,
# stat (big number for projects without photos), and the case copy.
PROJECTS = [
    dict(
        slug="1664-blanc-x-boulebar",
        title="French Summer Moments",
        client="1664 Blanc x Boulebar",
        sectors=["Food & drink", "Hospitality"],
        services="Partnership, activation, photo and video",
        result="+257% event attendance",
        cover="boulebar-petanque-player-copenhagen.jpg",
        hero="boulebar-1664-french-summer-moments.jpg",
        images=["boulebar-petanque-event-copenhagen.jpg", "boulebar-1664-blanc-bottle.jpg",
                "boulebar-petanque-guest.jpg", "boulebar-petanque-player-copenhagen.jpg"],
        alt="Pétanque at Boulebar Copenhagen with 1664 Blanc",
        challenge="A French beer and a pétanque bar with the same easy-going crowd, and a whole Copenhagen summer to fill.",
        idea="Make a small French ritual out of it. Pétanque every Sunday, a cold 1664 Blanc, and a good reason to come back next week.",
        did=["Developed and pitched the partnership from scratch", "Ran five Sunday pétanque events",
             "Shot all photo and video", "All social, all organic"],
        outcome="Event attendance grew 257% over the summer, with no paid media. Featured on The Jungle List, and the series continues.",
    ),
    dict(
        slug="strangas-gyros",
        title="A gyros shop with a personality",
        client="Strangas Gyros",
        sectors=["Food & drink"],
        services="Taglines, PR, social, food photo and video",
        result="500+ in line on opening day",
        stat=("500+", "people in line on opening day"),
        challenge="A new shop in Frederiksberg, and a brand with a big personality that hadn't been written down yet.",
        idea="Put into words what Strangas already is: Greek, colourful and full of humour. Then let the food do the talking.",
        did=["Taglines in Strangas' own voice", "PR for the Frederiksberg opening",
             "Built their Instagram with food stills and video"],
        outcome="More than 500 people queued outside on opening day. Instagram grew 26% in a year.",
    ),
    dict(
        slug="boulebar",
        title="Marketing, content and a library to grow from",
        client="Boulebar",
        sectors=["Hospitality"],
        services="Retainer: marketing, social, photo, video, activations",
        result="70% organic growth in 12 months",
        stat=("70%", "organic growth in 12 months"),
        challenge="A growing group of pétanque bars that needed marketing, content and events handled by someone who knows the places and the people.",
        idea="Work as part of the team. Plan it, shoot it, run the collabs, and build content that keeps working after the post goes out.",
        did=["All marketing, social, photo, video and activations in Denmark, on retainer",
             "Brand activations and collabs, including French Summer Moments with 1664 Blanc",
             "Hired by Boulebar Group in Stockholm to produce evergreen videos and build a content library"],
        outcome="70% organic growth in 12 months, working two days a week.",
    ),
    dict(
        slug="la-banchina",
        title="Keeping a summer spot warm through winter",
        client="La Banchina",
        sectors=["Food & drink", "Hospitality"],
        services="Social narrative, food photo and video",
        result="+7% organic in low season",
        cover="la-banchina-pasta-madfotograf-koebenhavn.jpg",
        hero="la-banchina-chef-kitchen.jpg",
        images=["la-banchina-pasta-madfotograf-koebenhavn.jpg", "la-banchina-dessert.jpg"],
        alt="Food and kitchen at La Banchina, Copenhagen",
        challenge="A harbour restaurant everyone knows in July. Less so in January.",
        idea="Show the kitchen, the food and the regulars as they really are. No ads, no staging.",
        did=["Social media narrative", "Food photo and video", "All organic or UGC"],
        outcome="7% organic follower growth over six low-season winter months.",
    ),
    dict(
        slug="frederiksborg-castle-book-launch",
        title="A book launch at the castle",
        client="Frederiksborg Castle x CPH Influencers",
        sectors=["Culture"],
        services="Event photography",
        cover="frederiksborg-castle-book-launch-portrait.jpg",
        hero="frederiksborg-castle-book-launch-dinner.jpg",
        images=["frederiksborg-castle-book-launch-guest.jpg", "frederiksborg-castle-book-launch-portrait.jpg",
                "frederiksborg-castle-book-launch-table.jpg"],
        alt="Book launch dinner at Frederiksborg Castle",
        challenge="A book launch dinner in one of Denmark's grandest rooms, with a guest list that knows its way around a camera.",
        idea="Shoot the evening like a story. The room, the details and the people, in candlelight.",
        did=["Event photography", "Guests, details and the room", "Images ready for the guests' own channels"],
    ),
    dict(
        slug="zentropa-lucky",
        title="Lucky",
        client="Zentropa",
        sectors=["Film"],
        services="Casting, set photography, premiere sponsorship",
        cover="zentropa-lucky-on-set.jpg",
        hero="zentropa-lucky-on-set.jpg",
        images=[],
        alt="On the set of Zentropa's film Lucky",
        challenge="A feature film that needed one very specific character, pictures from the set, and a premiere worth turning up for.",
        idea="Use the network. The right person for the part, and the right partner for the gala.",
        did=["Cast a niche character for the film", "Behind-the-scenes photography on set",
             "Secured sponsorship for the gala premiere"],
    ),
    dict(
        slug="kopenhagen-fur",
        title="Design collaborations and a first Instagram",
        client="Kopenhagen Fur",
        sectors=["Fashion"],
        services="Design collaborations, social, events",
        cover="kopenhagen-fur-coat-little-mermaid.jpg",
        hero="kopenhagen-fur-coat-little-mermaid.jpg",
        images=["kopenhagen-fur-coat-copenhagen-harbour.jpg"],
        alt="Fur coat by the Little Mermaid in Copenhagen",
        challenge="A heritage material brand working with fashion designers, at a time when brands were only just starting on social media.",
        idea="Show the work behind the work. Let people see how the collaborations were made.",
        did=["Led design collaborations", "Introduced the brand to Instagram with behind-the-scenes from our work",
             "Assisted on events and Copenhagen Fashion Week"],
    ),
    dict(
        slug="danish-coffee-festival",
        title="Danish Coffee Festival",
        client="Danish Coffee Festival",
        sectors=["Food & drink", "Culture"],
        services="Event photography",
        cover="danish-coffee-festival-latte.jpg",
        hero="danish-coffee-festival-tasting.jpg",
        images=["danish-coffee-festival-latte.jpg", "danish-coffee-festival-barista.jpg"],
        alt="Coffee and baristas at Danish Coffee Festival",
        challenge="A festival full of people who care a lot about coffee.",
        idea="Get close. The pours, the tastings and the faces.",
        did=["Event photography", "People, product and atmosphere"],
    ),
    dict(
        slug="sopavilionen-chess-club",
        title="Chess by the lake",
        client="Søpavilionen Chess Club",
        sectors=["Hospitality", "Culture"],
        services="Venue and people photography",
        cover="sopavilionen-chess-club-copenhagen.jpg",
        hero="sopavilionen-chess-club-copenhagen.jpg",
        images=["sopavilionen-dining-room.jpg"],
        alt="Chess club at Søpavilionen, Copenhagen",
        challenge="A classic Copenhagen venue with a chess club on the terrace.",
        idea="Show the room and the regulars, so people want to pull up a chair.",
        did=["Venue photography", "People and atmosphere"],
    ),
    dict(
        slug="palma-grandhood",
        title="Behind the scenes",
        client="Palma and Grandhood",
        sectors=["Corporate"],
        services="Behind-the-scenes photography",
        cover="palma-interior-arches.jpg",
        hero="palma-interior-arches.jpg",
        images=["palma-padel-behind-the-scenes.jpg", "grandhood-behind-the-scenes.jpg"],
        alt="Behind the scenes for Palma and Grandhood",
        challenge="A brand shoot where the moments between takes were as good as the takes.",
        idea="Document the process as it happens.",
        did=["Behind-the-scenes photography", "Stills for social and internal use"],
    ),
    dict(
        slug="artist-portraits",
        title="In the studio",
        client="Artist portraits",
        sectors=["Culture"],
        services="Portrait photography",
        cover="painter-at-work.jpg",
        hero="painter-studio-portrait.jpg",
        images=["painter-at-work.jpg"],
        alt="Painter in his studio",
        challenge="An artist who's more comfortable painting than posing.",
        idea="Let him work, and shoot the room around him.",
        did=["Portraits", "Work in progress"],
    ),
    dict(
        slug="branded-podcasts",
        title="Branded podcasts",
        client="Mensch and SOS Børnebyerne",
        sectors=["Corporate"],
        services="Sales, concept, production team",
        result="2 annual contracts in 8 months",
        cover="podcast-direktorens-dilemma-mensch.jpg",
        contain=True,
        hero="podcast-lydlos-sos-bornebyerne.jpg",
        images=["podcast-direktorens-dilemma-mensch.jpg"],
        alt="Podcast cover art",
        challenge="Two organisations with something to say, and no podcast to say it in.",
        idea="Branded podcasts that sound editorial, not like an ad. Lydløs on mental health for SOS Børnebyerne, and Direktørens Dilemma for Mensch.",
        did=["Signed two annual contracts in eight months through outreach and pitching",
             "Developed both concepts and assembled the production teams",
             "Balanced commercial needs with an editorial tone, via Filt"],
        outcome="Two annual branded podcast contracts signed within eight months.",
    ),
]

# Images that cycle on the dark opening screen, each linking to its project.
STAGE = [
    ("boulebar-petanque-player-copenhagen.jpg", "1664-blanc-x-boulebar"),
    ("la-banchina-pasta-madfotograf-koebenhavn.jpg", "la-banchina"),
    ("frederiksborg-castle-book-launch-portrait.jpg", "frederiksborg-castle-book-launch"),
    ("kopenhagen-fur-coat-little-mermaid.jpg", "kopenhagen-fur"),
    ("danish-coffee-festival-latte.jpg", "danish-coffee-festival"),
    ("zentropa-lucky-on-set.jpg", "zentropa-lucky"),
    ("sopavilionen-chess-club-copenhagen.jpg", "sopavilionen-chess-club"),
    ("palma-interior-arches.jpg", "palma-grandhood"),
    ("painter-at-work.jpg", "artist-portraits"),
    ("boulebar-1664-blanc-bottle.jpg", "1664-blanc-x-boulebar"),
    ("la-banchina-dessert.jpg", "la-banchina"),
    ("frederiksborg-castle-book-launch-guest.jpg", "frederiksborg-castle-book-launch"),
]

PROCESS = [
    ("Define", "What's the situation, the challenge or the goal? Research, data and human insight, plus a few calls to people who know."),
    ("Find the hook", "What would make people feel they belong? I look at what works for similar brands, and in other industries."),
    ("Make it physical", "An experience or community that fits what people already talk about. You get a deck with a rollout plan."),
    ("Produce", "Partners, people, run-of-show and a camera. I'm there on the day."),
    ("Launch and learn", "We go live, look at what the numbers say, and decide what's next."),
]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&display=swap" rel="stylesheet">')
ICON = ("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='6' fill='%23e8615a'/>"
        "<text x='16' y='23' font-family='Georgia' font-size='20' text-anchor='middle' fill='%23fff'>P</text></svg>")


def head(title, desc, path, prefix, og_image="boulebar-1664-french-summer-moments.jpg", extra=""):
    return f"""<!doctype html>
<html lang="en" class="no-js">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(desc)}">
  <link rel="canonical" href="{SITE}/{path}">
  <meta name="theme-color" content="#ffffff">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(desc)}">
  <meta property="og:image" content="{SITE}/images/{og_image}">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="{ICON}">
  {FONTS}
  <link rel="stylesheet" href="{prefix}styles.css">{extra}
</head>"""


def nav(prefix, current=""):
    def link(href, label, key):
        cur = ' aria-current="page"' if key == current else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    home = f"{prefix}index.html"
    return f"""<header class="nav" id="nav">
  <a href="{home}" class="wordmark" aria-label="PABOTO, home"><img src="{prefix}images/logo-coral.png" alt="PABOTO" width="118" height="20"></a>
  <nav aria-label="Main">
    {link(home + '#work', 'Work', 'work')}
    {link(prefix + 'services.html', 'Services', 'services')}
    {link(home + '#info', 'Info', 'info')}
  </nav>
  <a href="{home}#contact" class="nav-cta">Book a call</a>
</header>"""


def footer(prefix):
    return f"""<footer class="footer">
  <p>PABOTO, København</p>
  <p class="footer-mid">Creative consultant &amp; photographer. Brand activation, madfotograf og eventfotograf.</p>
  <p>&copy; <span id="year">2026</span></p>
</footer>

<script src="{prefix}script.js"></script>
</body>
</html>
"""


def contact_block():
    return f"""  <section id="contact" class="contact">
    <p class="label">Contact</p>
    <h2 class="contact-title">Got a launch, a venue or a half-formed idea?</h2>
    <a class="contact-big" href="mailto:{EMAIL}">{EMAIL}</a>
    <div class="contact-row">
      <a href="tel:{PHONE_TEL}">{PHONE}</a>
      <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a>
      <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>
    </div>

    <form class="contact-form" id="contact-form">
      <p class="form-intro">Or send a quick brief. I reply within two working days.</p>
      <div class="form-row">
        <label>Name<input type="text" name="name" required autocomplete="name"></label>
        <label>Email<input type="email" name="email" required autocomplete="email"></label>
      </div>
      <label>Company or venue<input type="text" name="company" autocomplete="organization"></label>
      <fieldset>
        <legend>What are you thinking?</legend>
        <div class="chips">
          {''.join(f'<label class="chip"><input type="checkbox" name="interest" value="{v}"><span>{v}</span></label>' for v in ["Creative direction", "Photo and video", "Activation", "Workshop", "Retainer", "Not sure yet"])}
        </div>
      </fieldset>
      <label>Tell me about it<textarea name="message" rows="4" required placeholder="What, when, roughly what budget"></textarea></label>
      <button type="submit" class="btn">Send</button>
    </form>
  </section>"""


def by_slug(slug):
    return next(p for p in PROJECTS if p["slug"] == slug)


# ---------------------------------------------------------------- index
PRIORITY = ' fetchpriority="high"'
LAZY = ' loading="lazy"'


def build_index():
    stage_items = "\n".join(
        f'      <a class="stage-item" href="work/{slug}.html" data-caption="{escape(by_slug(slug)["client"])}">'
        f'<img src="images/{img}" alt="{escape(by_slug(slug)["alt"])}"{PRIORITY if i == 0 else LAZY}></a>'
        for i, (img, slug) in enumerate(STAGE))

    tiles = []
    for i, p in enumerate(PROJECTS):
        sectors = " ".join(s.lower().replace(" & ", "-").replace(" ", "-") for s in p["sectors"])
        res = f'<p class="cap-res">{escape(p["result"])}</p>' if p.get("result") else ""
        if p.get("stat"):
            media = (f'<div class="stat-tile"><p class="stat-big">{p["stat"][0]}</p>'
                     f'<p class="stat-small">{escape(p["stat"][1])}</p></div>')
        else:
            media = f'<img src="images/{p["cover"]}" alt="{escape(p["alt"])}" loading="lazy">'
        fit = " tile-contain" if p.get("contain") else ""
        tiles.append(f"""      <a class="tile reveal{fit}" href="work/{p['slug']}.html" data-sectors="{sectors}">
        <div class="tile-media">{media}</div>
        <div class="cap">
          <p class="cap-title"><span class="cap-n">{i + 1:02d}</span>{escape(p['client'])}</p>
          {res}
          <p class="cap-tag">{escape(p['services'])}</p>
        </div>
      </a>""")

    filters = "\n".join(
        f'      <button class="filter" data-filter="{s.lower().replace(" & ", "-").replace(" ", "-")}">{escape(s)}</button>'
        for s in SECTORS)

    pillars = [
        ("Food & drink", "1664 Blanc, Strangas Gyros, La Banchina, Enghave Kaffe, Oatly, Danish Coffee Festival"),
        ("Hospitality", "Boulebar Denmark, Boulebar Group Stockholm, Søpavilionen"),
        ("Culture", "Frederiksborg Castle, artists, festivals"),
        ("Fashion", "Kopenhagen Fur, Copenhagen Fashion Week"),
        ("Film", "Zentropa"),
        ("Corporate", "Mensch, SOS Børnebyerne, Grandhood"),
    ]
    pillar_html = "\n".join(
        f'      <li class="reveal"><span class="pillar-name">{escape(n)}</span><span class="pillar-who">{escape(w)}</span></li>'
        for n, w in pillars)

    steps = "\n".join(
        f'      <li class="reveal"><span class="step-n">{i + 1:02d}</span><h3>{escape(t)}</h3><p>{escape(d)}</p></li>'
        for i, (t, d) in enumerate(PROCESS))

    jsonld = f"""
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "PABOTO",
    "founder": {{ "@type": "Person", "name": "Stephanie Pabotoy" }},
    "description": "Creative direction, brand activation, partnerships, food and event photography in Copenhagen.",
    "email": "{EMAIL}",
    "telephone": "{PHONE}",
    "url": "{SITE}",
    "image": "{SITE}/images/boulebar-1664-french-summer-moments.jpg",
    "areaServed": "Denmark",
    "sameAs": ["{INSTAGRAM}", "{LINKEDIN}"],
    "address": {{ "@type": "PostalAddress", "addressLocality": "København", "addressCountry": "DK" }}
  }}
  </script>"""

    html = head("Kreativ konsulent & madfotograf København | PABOTO",
                "Creative direction, brand activations and food and event photography in Copenhagen. One person for the idea, the partners and the pictures. Book a call.",
                "", "", extra=jsonld)
    html += f"""
<body class="page-home">

<a class="skip" href="#work">Skip to work</a>

{nav('')}

<main>

  <!-- OPENING: one image at a time, click through to the project -->
  <section class="stage" aria-label="Selected images, click to open the project">
    <div class="stage-track" id="stage">
{stage_items}
    </div>
    <p class="stage-cap" id="stage-cap" aria-live="polite"></p>
    <div class="stage-foot">
      <p>Creative direction, activations &amp; photography</p>
      <a href="#work" class="stage-down">Index &darr;</a>
    </div>
  </section>

  <!-- INTRO -->
  <section class="intro">
    <h1 class="intro-line reveal">I help brands turn ideas into moments people <em>show up for</em>, and then I shoot them.</h1>
    <div class="intro-cols reveal">
      <p>Strategy, partnerships and photography from one person. Most brands hire three and hope they get along. I bring the idea, the right people and the camera.</p>
      <p>For food and drink, hospitality, cultural institutions, music, fashion, film and corporate brands. Based in Copenhagen, working across Denmark and Sweden.</p>
    </div>
  </section>

  <div class="band"><p>Selected creative projects</p></div>

  <!-- WORK -->
  <section id="work" class="work">
    <div class="work-head">
      <p class="label">Index</p>
      <div class="filters" role="group" aria-label="Filter by sector">
      <button class="filter is-on" data-filter="all">All</button>
{filters}
      </div>
    </div>
    <div class="grid" id="grid">
{chr(10).join(tiles)}
    </div>
    <p class="also reveal"><span class="label">Also</span> Enghave Kaffe, Instagram built on organic photo and video, +29% followers in four months. Oatly, local activation content and visual materials.</p>
  </section>

  <!-- PILLARS -->
  <section class="pillars">
    <p class="label">Who I work with</p>
    <ul>
{pillar_html}
    </ul>
  </section>

  <!-- SERVICES STRIP -->
  <section class="teaser" aria-label="Services">
    <a href="services.html" class="teaser-link">
      <span class="label">Services</span>
      <span class="teaser-items">
        <span>Creative direction <b>from 16,500 kr</b></span>
        <span>Photo and video <b>from 9,500 kr / day</b></span>
        <span>Activation <b>from 30,000 kr</b></span>
        <span>Retainer <b>from 10,000 kr / month</b></span>
      </span>
      <span class="teaser-more">Packages and prices &rarr;</span>
    </a>
  </section>

  <div class="band"><p>How I work</p></div>

  <!-- PROCESS -->
  <section class="process" id="process">
    <div class="process-head">
      <h2 class="section-title reveal">From a hunch to a full room</h2>
      <p class="muted reveal">Every project gets its own plan. This is roughly how it goes.</p>
    </div>
    <ol class="steps">
{steps}
    </ol>
  </section>

  <!-- INFO -->
  <section id="info" class="about">
    <figure class="about-img reveal">
      <img src="images/stephanie-pabotoy-portrait-copenhagen.jpg" alt="Stephanie Pabotoy, creative consultant and photographer, sitting on a doorstep in Copenhagen" loading="lazy">
    </figure>
    <div class="about-text reveal">
      <p class="label">Info</p>
      <p class="about-lead">I'm Steph. Ten years of branding on both the client and the agency side, across hospitality, lifestyle and culture.</p>
      <p>I'm very good at getting good people together. That's where most of my partnerships and collabs start, and it's why brands hire me for more than the pictures. I have a popcorn brain, which is great for ideas and slightly worse for sitting still.</p>
      <blockquote>"I don't just want a brand to be seen. I want it to be part of the culture."</blockquote>
    </div>
  </section>

{contact_block()}

</main>

{footer('')}"""
    (ROOT / "index.html").write_text(html)


# ---------------------------------------------------------------- project pages
def build_projects():
    (ROOT / "work").mkdir(exist_ok=True)
    n = len(PROJECTS)
    for i, p in enumerate(PROJECTS):
        nxt = PROJECTS[(i + 1) % n]
        meta = [("Client", p["client"]), ("Sector", ", ".join(p["sectors"])), ("Services", p["services"])]
        if p.get("result"):
            meta.append(("Result", p["result"]))
        meta_html = "\n".join(f'      <div><dt>{k}</dt><dd>{escape(v)}</dd></div>' for k, v in meta)

        if p.get("stat"):
            hero = (f'<div class="case-stat"><p class="stat-big">{p["stat"][0]}</p>'
                    f'<p class="stat-small">{escape(p["stat"][1])}</p></div>')
        else:
            hero = f'<figure class="case-hero"><img src="../images/{p["hero"]}" alt="{escape(p["alt"])}"></figure>'

        rows = [("Challenge", f"<p>{escape(p['challenge'])}</p>"),
                ("Idea", f"<p>{escape(p['idea'])}</p>"),
                ("What I did", "<ul>" + "".join(f"<li>{escape(d)}</li>" for d in p["did"]) + "</ul>")]
        if p.get("outcome"):
            rows.append(("Result", f"<p class=\"case-outcome\">{escape(p['outcome'])}</p>"))
        copy = "\n".join(f'      <div class="case-row reveal"><h2>{k}</h2><div>{v}</div></div>' for k, v in rows)

        imgs = p.get("images", [])
        gallery = ""
        if imgs:
            figs = "\n".join(f'      <figure class="reveal"><img src="../images/{im}" alt="{escape(p["alt"])}" loading="lazy"></figure>'
                             for im in imgs)
            cols = 1 if len(imgs) == 1 else 2 if len(imgs) in (2, 4) else 3
            gallery = f'    <div class="case-gallery case-gallery-{cols}">\n{figs}\n    </div>'

        title = f"{p['client']}: {p['title']} | PABOTO"
        if len(title) > 60:
            title = f"{p['client']} | PABOTO"
        desc = f"{p['client']}. {p['services']}. {p.get('outcome') or p['challenge']}"
        if len(desc) > 155:
            desc = desc[:152].rsplit(" ", 1)[0] + "..."

        html = head(title, desc, f"work/{p['slug']}.html", "../", og_image=p.get("hero") or "boulebar-1664-french-summer-moments.jpg")
        html += f"""
<body class="page-case">

{nav('../', current='work')}

<main>
  <article class="case">
    <header class="case-head">
      <p class="label"><a href="../index.html#work">Index</a> / {i + 1:02d}</p>
      <h1 class="case-title">{escape(p['title'])}</h1>
      <dl class="case-meta">
{meta_html}
      </dl>
    </header>

    {hero}

    <div class="case-copy">
{copy}
    </div>

{gallery}
  </article>

  <section class="case-cta">
    <p class="label">Your turn</p>
    <h2 class="contact-title">Want something like this for your brand?</h2>
    <div class="contact-row">
      <a class="btn" href="../index.html#contact">Book a call</a>
      <a href="../services.html">See packages and prices</a>
    </div>
  </section>

  <a class="case-next" href="{nxt['slug']}.html">
    <span class="label">Next project</span>
    <span class="case-next-title">{escape(nxt['client'])} &rarr;</span>
  </a>
</main>

{footer('../')}"""
        (ROOT / "work" / f"{p['slug']}.html").write_text(html)


# ---------------------------------------------------------------- services
def pkg(name, sub, for_text, price_html, items, feature=False):
    acc = "\n".join(f'        <details><summary>{escape(t)}</summary><p>{escape(d)}</p></details>' for t, d in items)
    sub_html = f" <span>{escape(sub)}</span>" if sub else ""
    return f"""    <article class="pkg{' pkg-feature' if feature else ''} reveal">
      <h2>{escape(name)}{sub_html}</h2>
      <p class="pkg-for">{escape(for_text)}</p>
      <p class="pkg-price">{price_html}</p>
      <a class="pkg-btn" href="index.html#contact">Book a call</a>
      <div class="acc">
{acc}
      </div>
    </article>"""


def build_services():
    packages = "\n".join([
        pkg("Creative direction", "", "For brands that need a clear idea and a plan before anyone picks up a camera. Concept, visual direction and the right partners.",
            "Starting price: <b>16,500 kr</b><br>Typical scope: about 15 hours",
            [("Brief and expectations", "What you want to happen, for whom, and how we'll know it worked."),
             ("Research and benchmarks", "What similar brands do, what other industries do better, and where the gap is."),
             ("Concept and visual direction", "The idea, the look and the tone, in a deck you can share."),
             ("Partners and collabs", "Who you could team up with, and why it works for both sides. I make the intros."),
             ("Team and plan", "The right photographer, stylist or producer, a budget and a timeline.")]),
        pkg("Photo and video", "", "For brands that need content that looks and feels like them. Food, venues, people and events, shot by someone who knows why you're posting it.",
            "Price: <b>9,500 kr per day</b><br>Half day: 5,500 kr. Planning, editing and delivery included",
            [("Planning and shot list", "We agree what we need, where and when, before the day."),
             ("On the day", "Up to 8 hours on location. Stills and short vertical video."),
             ("Editing", "A curated selection of edited stills and clips, graded to feel like your brand."),
             ("Delivery", "Web-ready and full-size files within 5 working days."),
             ("Usage", "Use on your own channels included. Paid ads and print by agreement.")]),
        pkg("Activation", "(direction + execution)", "For brands that want people to show up. From the idea and the partners to a full room, with the content to prove it.",
            "Starting price: <b>30,000 kr</b><br>My fee. Venue, suppliers and production costs are quoted separately",
            [("Everything in Creative direction", "Brief, concept, deck, partners and plan."),
             ("Production and run-of-show", "Suppliers, people, timings and everything on the day. I'm there."),
             ("Photo and video", "Content from the event, ready for your channels."),
             ("Social before and after", "Posts and stories that get people there, and show who came."),
             ("Recap", "What worked, the numbers, and what to do next time.")], feature=True),
    ])

    retainers = "\n".join([
        pkg("Content", "", "For brands that need fresh content every month, without a big team.",
            "Price: <b>from 10,000 kr / month</b><br>One half-day shoot a month",
            [("Monthly plan", "What to post and when, agreed at the start of each month."),
             ("One half-day shoot", "Stills and short video from your venue, food or event."),
             ("Edited and delivered", "Ready to post, within 5 working days.")]),
        pkg("Build", "(first 4 to 6 weeks)", "For getting it all up and running properly. Three days a week at the start, then we move to Run.",
            "Price: <b>48,000 kr / month</b><br>3 days a week",
            [("Strategy and tone", "Who you're talking to, how you sound and what you post."),
             ("Partner outreach", "The first collabs and partners, lined up."),
             ("Content library", "Shoots to build a bank of stills and evergreen video."),
             ("Channels set up", "Everything running, ready to hand over or keep going.")], feature=True),
        pkg("Run", "", "For keeping it going once the build is done. Two days a week, as part of your team.",
            "Price: <b>34,000 kr / month</b><br>2 days a week",
            [("Photo and video", "Ongoing content from your venues, food and events."),
             ("Social and community", "Posting, replies and keeping it human."),
             ("Collabs and activations", "New partners and new reasons to show up."),
             ("Monthly check-in", "What the numbers say and what's next.")]),
    ])

    html = head("Priser: kreativ konsulent & eventfotograf | PABOTO",
                "Packages and prices for creative direction, food and event photography, brand activations and retainers in Copenhagen. Clear starting prices.",
                "services.html", "")
    html += f"""
<body class="page-services">

{nav('', current='services')}

<main>
  <section class="svc-intro">
    <p class="label">Services and prices</p>
    <h1 class="intro-line">Pick a starting point. <em>We'll shape it together.</em></h1>
    <p class="muted svc-lead">All prices excl. moms. They're a starting point, adjusted to the scope and purpose of the job.</p>
  </section>

  <section class="packages" aria-label="Packages">
{packages}
  </section>

  <section class="first-step reveal">
    <div>
      <p class="label">Small first step</p>
      <h2>Idea workshop</h2>
      <p class="muted">Not ready for a full project? Book a workshop with your team. We leave with ideas, partners to talk to and a clear next step.</p>
    </div>
    <p class="first-step-price">6,500 kr <span>half day</span><br>10,000 kr <span>full day</span></p>
    <a class="pkg-btn" href="index.html#contact">Book a workshop</a>
  </section>

  <section class="retainers" aria-label="Retainers">
    <div class="ret-head">
      <p class="label">Retainers</p>
      <h2 class="intro-line">Want me on the team?</h2>
      <p class="muted svc-lead">Marketing, social, content and activations every month. Three-month minimum. This is how I work with Boulebar in Denmark.</p>
    </div>
    <div class="packages">
{retainers}
    </div>
    <p class="ret-note">Several venues, markets or a big campaign? Group retainers go up to 100,000 kr a month.</p>
  </section>

  <section class="svc-cta">
    <h2 class="contact-title">Not sure which one fits?</h2>
    <a class="contact-big" href="mailto:{EMAIL}">{EMAIL}</a>
    <div class="contact-row">
      <a href="tel:{PHONE_TEL}">{PHONE}</a>
      <a href="index.html#work">See the work</a>
    </div>
  </section>
</main>

{footer('')}"""
    (ROOT / "services.html").write_text(html)


if __name__ == "__main__":
    build_index()
    build_projects()
    build_services()
    print(f"Built index.html, services.html and {len(PROJECTS)} project pages.")
