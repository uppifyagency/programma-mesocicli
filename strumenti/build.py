#!/usr/bin/env python3
"""Genera le pagine strumento del cluster SEO.

Riusa CSS, header e footer della landing: se la landing cambia stile, basta
rilanciare questo script e le pagine seguono. Non modificare a mano i file
generati in <slug>/index.html.

    python3 strumenti/build.py
"""
import json, re, os, sys, html

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = os.environ.get('MESOCICLI_DOMINIO', 'https://programma-mesocicli.vercel.app')
GH = 'https://github.com/uppifyagency/programma-mesocicli'
OGGI = '2026-08-26'

sys.path.insert(0, os.path.join(RADICE, 'strumenti'))
from contenuti import PAGINE, CALCOLATORE_JS


def shell():
    """CSS, header e footer presi dalla landing, cosi' non divergono."""
    s = open(os.path.join(RADICE, 'index.html'), encoding='utf-8').read()
    stile = re.search(r'(?s)<style>(.*?)</style>', s).group(1)
    # le url dei font sono relative alla root: dentro una sottocartella servono ../
    stile = stile.replace('url(assets/fonts/', 'url(../assets/fonts/')
    header = re.search(r'(?s)<header class="site">.*?</header>', s).group(0)
    footer = re.search(r'(?s)<footer class="site">.*?</footer>', s).group(0)
    return stile, header, footer


def nav(slug_corrente):
    voci = [(p['slug'], p['nav']) for p in PAGINE]
    out = ['<a href="../">Home</a>']
    for slug, etichetta in voci:
        if slug == slug_corrente:
            out.append(f'<a href="#top" aria-current="page">{etichetta}</a>')
        else:
            out.append(f'<a href="../{slug}/">{etichetta}</a>')
    out.append('<a href="../app/">Generatore</a>')
    return '\n      '.join(out)


def faq_html(faq):
    return '\n'.join(
        f'    <details>\n      <summary>{q}</summary>\n      <div class="a">{a}</div>\n    </details>'
        for q, a in faq)


def testo(x):
    x = re.sub(r'(?s)<[^>]+>', '', x)
    return re.sub(r'\s+', ' ', html.unescape(x)).strip()


def schema(p):
    url = f'{DOMINIO}/{p["slug"]}/'
    g = [
        {"@type": "Person", "@id": f"{DOMINIO}/#autore", "name": "Vlad Vrinceanu",
         "url": f"{DOMINIO}/#autore", "jobTitle": "AI manager",
         "sameAs": ["https://www.linkedin.com/in/vladvrinceanu/",
                    "https://github.com/uppifyagency"],
         "description": "Autore e sviluppatore di Programma Mesocicli, strumento open source per il calcolo delle calorie della definizione e la programmazione dell'allenamento. Non e un professionista sanitario."},
        {"@type": "Organization", "@id": f"{DOMINIO}/#organization",
         "name": "Programma Mesocicli", "url": f"{DOMINIO}/",
         "founder": {"@id": f"{DOMINIO}/#autore"}, "sameAs": [GH]},
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": p['title'],
         "description": p['description'], "inLanguage": "it-IT",
         "isPartOf": {"@id": f"{DOMINIO}/#website"},
         "author": {"@id": f"{DOMINIO}/#autore"},
         "publisher": {"@id": f"{DOMINIO}/#organization"},
         "datePublished": OGGI, "dateModified": OGGI,
         "breadcrumb": {"@id": url + "#breadcrumb"},
         "about": [{"@type": "Thing", "name": n} for n in p['entita']],
         "primaryImageOfPage": {"@type": "ImageObject", "url": f"{DOMINIO}/assets/og.png"},
         "citation": p.get('citazioni', [])},
        {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Programma Mesocicli", "item": f"{DOMINIO}/"},
            {"@type": "ListItem", "position": 2, "name": p['nav'], "item": url}]},
        {"@type": ["SoftwareApplication", "WebApplication"], "@id": url + "#tool",
         "name": p['nome_tool'], "url": url,
         "applicationCategory": "HealthApplication", "applicationSubCategory": "Fitness",
         "operatingSystem": "Qualsiasi browser web", "inLanguage": "it-IT",
         "isAccessibleForFree": True,
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR",
                    "availability": "https://schema.org/InStock"},
         "license": f"{GH}/blob/main/LICENSE", "codeRepository": GH,
         "publisher": {"@id": f"{DOMINIO}/#organization"},
         "author": {"@id": f"{DOMINIO}/#autore"},
         "description": p['description']},
        {"@type": "FAQPage", "@id": url + "#faq", "inLanguage": "it-IT",
         "isPartOf": {"@id": url + "#webpage"},
         "mainEntity": [{"@type": "Question", "name": testo(q),
                         "acceptedAnswer": {"@type": "Answer", "text": testo(a)}}
                        for q, a in p['faq']]},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": g},
                      ensure_ascii=False, indent=2)


TEMPLATE = '''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<meta name="author" content="Programma Mesocicli">
<link rel="alternate" hreflang="it-IT" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta name="theme-color" media="(prefers-color-scheme: light)" content="#F1F3F5">
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="#13171C">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Programma Mesocicli">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{dominio}/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="it_IT">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{dominio}/assets/og.png">
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="../assets/apple-touch-icon.png">
<link rel="preload" href="../assets/fonts/barlow-condensed-700-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="../assets/fonts/barlow-400-latin.woff2" as="font" type="font/woff2" crossorigin>
<script type="application/ld+json">
{schema}
</script>
<style>{stile}</style>
</head>
<body>
<a class="skip" href="#contenuto">Salta al contenuto</a>
{header}
<div class="wrap" id="top">
  <div class="hero" style="padding-top:26px">
    <div>
      <div class="kicker">{kicker}</div>
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
      <div class="cta">
        <a class="btn" href="#strumento">{cta}</a>
        <a class="btn ghost" href="../app/">Genera la scheda</a>
      </div>
      <p class="micro">Gratis · nessun account · i dati restano nel tuo browser</p>
    </div>
  </div>
</div>

<main id="contenuto">
<div class="wrap">
  <section id="strumento" aria-labelledby="h-strumento">
    <h2 id="h-strumento" class="sr-only">{nome_tool}</h2>
    {calcolatore}
  </section>

{corpo}

  <section aria-labelledby="h-firma">
    <div class="eyebrow">Chi l'ha fatto</div>
    <h2 id="h-firma">Chi c'è dietro questo calcolo?</h2>
    <p class="lead-a">Vlad Vrinceanu, AI manager. Non sono un medico né un nutrizionista: per questo ogni formula usata qui è dichiarata con la sua fonte primaria e il suo margine di errore, invece di chiederti di fidarti.</p>
    <p style="color:var(--ink2); max-width:70ch; margin-top:12px">Il codice è pubblico con licenza MIT, quindi le formule si possono leggere e verificare riga per riga. Se hai una patologia, sei in gravidanza o hai avuto disturbi del comportamento alimentare, la persona da sentire è un professionista sanitario, non un calcolatore. <a href="../#autore">Di più sull'autore</a> · <a href="https://www.linkedin.com/in/vladvrinceanu/" rel="noopener author">LinkedIn</a> · <a href="{gh}" rel="noopener">Codice sorgente</a></p>
  </section>

  <section id="faq" class="faq" aria-labelledby="h-faq">
    <div class="eyebrow">FAQ</div>
    <h2 id="h-faq">Domande frequenti</h2>
{faq}
  </section>

  <section aria-labelledby="h-altri">
    <div class="eyebrow">Gli altri strumenti</div>
    <h2 id="h-altri">Che altro c'è da calcolare?</h2>
    <p class="lead-a">Ogni strumento risponde a una domanda diversa dello stesso percorso: quanto consumi, quanto tagliare, come dividere le calorie, come allenarti.</p>
    <div class="grid3" style="margin-top:20px">
{correlate}
    </div>
  </section>
</div>
</main>
{footer}
<script>{js}</script>
</body>
</html>
'''


def correlate_html(slug):
    out = []
    for p in PAGINE:
        if p['slug'] == slug:
            continue
        out.append(f'''      <div class="card">
        <h3 style="margin-top:0"><a href="../{p['slug']}/" style="color:inherit">{p['nav']}</a></h3>
        <p style="color:var(--ink2)">{p['occhiello']}</p>
      </div>''')
    out.append('''      <div class="card">
        <h3 style="margin-top:0"><a href="../app/" style="color:inherit">Il generatore di schede</a></h3>
        <p style="color:var(--ink2)">Due distretti target, cinque sedute a settimana, volumi confrontati con MEV, MAV e MRV.</p>
      </div>''')
    return '\n'.join(out)


def main():
    stile, header, footer = shell()
    # nella nav della landing i link sono ancore: dentro una sottocartella vanno riscritti
    for p in PAGINE:
        h = re.sub(r'(?s)<nav aria-label="Navigazione principale">.*?</nav>',
                   f'<nav aria-label="Navigazione principale">\n      {nav(p["slug"])}\n      <a href="{GH}" rel="noopener">GitHub</a>\n    </nav>',
                   header)
        h = h.replace('<a class="brand" href="#"', '<a class="brand" href="../"')
        out = TEMPLATE.format(
            title=p['title'], description=p['description'], og_title=p['og_title'],
            url=f'{DOMINIO}/{p["slug"]}/', dominio=DOMINIO,
            schema=schema(p), stile=stile, header=h, footer=footer,
            kicker=p['kicker'], h1=p['h1'], lead=p['lead'], cta=p['cta'],
            nome_tool=p['nome_tool'], calcolatore=p['calcolatore'],
            corpo=p['corpo'], faq=faq_html(p['faq']),
            correlate=correlate_html(p['slug']), js=CALCOLATORE_JS, gh=GH)
        d = os.path.join(RADICE, p['slug'])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(out)
        print(f'  {p["slug"]}/index.html · {len(out):>6} byte · {len(p["faq"])} FAQ')
    print(f'{len(PAGINE)} pagine generate.')


if __name__ == '__main__':
    main()
