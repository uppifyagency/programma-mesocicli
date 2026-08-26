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
index.html        landing page
app/index.html    l'app, file unico (HTML + CSS + JS vanilla)
assets/           favicon e immagine social
robots.txt, sitemap.xml, llms.txt
vercel.json       header e cache per il deploy su Vercel
```

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
