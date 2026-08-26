# Programma Mesocicli

Programma di cut open source. Inserisci eta, peso, altezza, sesso e attivita quotidiana: ottieni le calorie della definizione, i macro e il mesociclo completo di allenamento. 5 sedute a settimana con esercizi intercambiabili, volumi confrontati con MEV/MAV/MRV, striscia delle settimane con gli scarichi.

**Sito e app:** https://programma-mesocicli.vercel.app/

## Il metodo in breve

- **Specializzazione:** due distretti target per mesociclo. Il loro volume sale verso il massimo produttivo, tutto il resto scende a mantenimento. Ogni target si allena due volte a settimana.
- **Ruoli:** ogni seduta apre con un esercizio madre (4×6-8, ER 20, recupero 1,5-3′), prosegue con i meccanici (3×8-10, ER 15) e chiude con gli isolamenti (3×10-12, recupero 60-90″, SQUEEZE).
- **Progressione:** double progression sul log. Si registrano carico, ripetizioni totali e RPE; la settimana dopo si batte il log: prima più ripetizioni, poi più carico.
- **Nutrizione:** metabolismo basale con Mifflin-St Jeor, dispendio totale dal fattore di attivita, deficit di riferimento di circa 625 kcal (perdita attesa ~0,55 kg a settimana). Il target non scende mai sotto il metabolismo basale: su soggetti leggeri il deficit viene ridotto e l'app lo dichiara. Feriali 170 kcal piu bassi, weekend a compensare, proteine 2 g/kg, grassi 0,75 g/kg, 15.000 passi al giorno.
- **In deficit non si cresce ovunque:** il volume alto va su due distretti perche il recupero e la risorsa scarsa. Per chi si allena da anni l'obiettivo del blocco e conservare la massa magra.

## Uso

Nessuna build, nessuna dipendenza:

```
git clone https://github.com/uppifyagency/programma-mesocicli.git
open programma-mesocicli/index.html      # landing con il calcolatore
open programma-mesocicli/app/index.html  # il generatore
```

La landing passa i dati del calcolatore all'app in querystring, e l'app li applica sopra lo stato salvato:

```
app/?sesso=F&eta=27&peso=61.5&alt=168&mult=1.375&target=glutei,femorali&dur=16
```

Parametri accettati: `sesso` (M/F), `eta`, `peso`, `alt`, `mult` (1.2-1.9), `target` (due distretti separati da virgola), `dur` (8, 12 o 16). Ogni valore viene limitato al suo intervallo valido, i valori non validi sono ignorati.

Oppure servi la cartella con un qualunque static server (`python3 -m http.server`).

I dati (configurazione, dati corporei, scelte esercizio) vivono solo nel `localStorage` del browser, chiave `mesocicli.v1`. Niente backend, niente tracker.

## Struttura

```
index.html        landing page (hub)
app/index.html    l'app, file unico (HTML + CSS + JS vanilla)
strumenti/        sorgenti delle pagine strumento (build.py + contenuti.py)
calcolo-fabbisogno-calorico/  GENERATA
deficit-calorico/             GENERATA
calcolo-macronutrienti/       GENERATA
scheda-definizione/           GENERATA
assets/           favicon e immagine social
robots.txt, sitemap.xml, llms.txt
vercel.json       header e cache per il deploy su Vercel
```

## SEO e indicizzazione

Impostata sullo stato dell'arte 2026 (skill `seo-2026-sota`). Le scelte che non
vanno rotte per sbaglio:

- **Titoli in forma di domanda con risposta atomica** nella prima riga sotto. E il
  pattern che AI Overviews e gli LLM estraggono come citazione: se un H2 torna a
  essere uno slogan, quella sezione smette di essere citabile.
- **Un solo `@graph` JSON-LD** per pagina (Organization, WebSite, WebPage,
  BreadcrumbList, SoftwareApplication, HowTo, FAQPage). Le FAQ nello schema sono
  **generate dal DOM**: se aggiungi un `<details>` alla FAQ, rigenera il blocco
  invece di scriverlo a mano, altrimenti schema e pagina divergono.
- **Font self-hosted** in `assets/fonts/` con `@font-face` inline nella pagina.
  Non rimettere il `<link>` a fonts.googleapis.com: era l'unica risorsa
  render-blocking rimasta (-300ms) e l'unica richiesta a terzi, che contraddiceva
  il claim "zero tracker" scritto in pagina.
- **Il contenuto statico su `/app/` sta nel primo response.** I crawler dei motori
  generativi non eseguono JavaScript: senza quel blocco la pagina del generatore
  e praticamente vuota per ChatGPT, Claude e Perplexity. La scheda generata dal JS
  non li raggiunge.
- **`robots.txt` ammette i crawler AI** di proposito (GPTBot, ClaudeBot,
  PerplexityBot, Google-Extended, OAI-SearchBot, Applebot-Extended). Il sito e
  open source e non contiene dati personali: essere citati e l'obiettivo.
- **La sezione Metodologia cita fonti primarie** con margine di errore dichiarato
  e un elenco di cosa lo strumento non fa. Dal Core Update di marzo 2026
  l'esperienza dimostrata pesa piu della pagina generalista perfetta.
- **IndexNow**: la chiave sta nel file `<chiave>.txt` alla root, che deve restare
  raggiungibile. Dopo un deploy che cambia il contenuto:

  ```
  KEY=$(ls *.txt | grep -Ev 'llms|robots' | sed 's/.txt$//')
  curl -X POST https://api.indexnow.org/IndexNow -H 'Content-Type: application/json' \
    -d "{\"host\":\"programma-mesocicli.vercel.app\",\"key\":\"$KEY\",\"urlList\":[\"https://programma-mesocicli.vercel.app/\"]}"
  ```

  Notifica Bing, DuckDuckGo, Yandex e Perplexity. **Non Google**: per Google
  contano sitemap, Search Console e i link interni.
- `sitemap.xml` e `llms.txt` vanno aggiornati quando cambia il contenuto: `llms.txt`
  contiene la tabella dei volumi e le fonti in forma leggibile da un LLM.

## Le pagine strumento (generate)

Le quattro cartelle `calcolo-fabbisogno-calorico/`, `deficit-calorico/`,
`calcolo-macronutrienti/` e `scheda-definizione/` sono **generate**. Non
modificarle a mano: si cambia `strumenti/contenuti.py` e si rilancia

```
python3 strumenti/build.py
```

- Il builder riusa **CSS, header e footer della landing**: se cambia lo stile di
  `index.html`, basta rigenerare e le pagine seguono invece di divergere.
- L'aritmetica del calcolo sta in un punto solo (`CALCOLATORE_JS` in
  `contenuti.py`) ed e la stessa della landing e del generatore. Se cambi una
  formula, cambiala li: numeri diversi fra due pagine dello stesso sito sono un
  problema di fiducia prima che di SEO. Quello che cambia per pagina e solo
  **quali righe** vengono mostrate (`data-vista`).
- Ogni pagina copre un **intent distinto**. Non aggiungere una pagina su una
  keyword che una pagina esistente gia serve: si canniballizzano. E il motivo
  per cui non esiste `/calcolo-tdee/` nonostante 2.900 ricerche al mese — in
  italiano e la stessa query di "calcolo fabbisogno calorico", e nella SERP
  `projectinvictus.it/calcolo-calorie/` ranka su entrambe con la stessa URL.
  Prima di creare una pagina, guarda se le due SERP si sovrappongono.
- Le domande delle FAQ vengono dai **People Also Ask reali** (DataForSEO,
  `serp/google/organic/live/advanced`, location 2380). Non inventarle: sono
  gratis e sono le domande che Google sta gia mostrando.
- Aggiungendo una pagina vanno aggiornati anche `sitemap.xml`, `llms.txt` e la
  sezione Strumenti della landing, altrimenti la pagina resta senza percorso
  interno.

## Deploy

Il sito e statico: la build su Vercel non fa nulla, carica la root.

- **Online su https://programma-mesocicli.vercel.app** (progetto Vercel `programma-mesocicli`).
  Si pubblica con `npx vercel deploy --prod` dalla cartella del repo.
- `vercel.json` imposta gli header di sicurezza e la cache degli asset.
- Un solo hostname serve il sito. GitHub Pages e stato spento: due copie dello stesso
  contenuto si fanno concorrenza in indicizzazione. Canonical, `og:url`, `sitemap.xml`,
  `robots.txt` e `llms.txt` puntano tutti al dominio Vercel.

## Licenza

[MIT](LICENSE). Non è una prescrizione medica: prima di iniziare un programma di allenamento o una dieta, parlane con un professionista.
