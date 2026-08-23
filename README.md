# Programma Mesocicli

Generatore open source di mesocicli di specializzazione per l'ipertrofia. Scegli due distretti target e ottieni la settimana completa: 5 sedute con esercizi intercambiabili, volumi confrontati con MEV/MAV/MRV, striscia delle settimane con scarichi e un piano calorico calcolato sui tuoi dati.

**Sito e app:** https://uppifyagency.github.io/programma-mesocicli/

## Il metodo in breve

- **Specializzazione:** due distretti target per mesociclo. Il loro volume sale verso il massimo produttivo, tutto il resto scende a mantenimento. Ogni target si allena due volte a settimana.
- **Ruoli:** ogni seduta apre con un esercizio madre (4×6-8, ER 20, recupero 1,5-3′), prosegue con i meccanici (3×8-10, ER 15) e chiude con gli isolamenti (3×10-12, recupero 60-90″, SQUEEZE).
- **Progressione:** double progression sul log. Si registrano carico, ripetizioni totali e RPE; la settimana dopo si batte il log: prima più ripetizioni, poi più carico.
- **Nutrizione:** deficit calcolato dal TDEE (~625 kcal), feriali più bassi e weekend flessibile, proteine 2 g/kg, 15.000 passi al giorno.

## Uso

Nessuna build, nessuna dipendenza:

```
git clone https://github.com/uppifyagency/programma-mesocicli.git
open programma-mesocicli/app/index.html
```

Oppure servi la cartella con un qualunque static server (`python3 -m http.server`).

I dati (configurazione, dati corporei, scelte esercizio) vivono solo nel `localStorage` del browser, chiave `mesocicli.v1`. Niente backend, niente tracker.

## Struttura

```
index.html        landing page
app/index.html    l'app, file unico (HTML + CSS + JS vanilla)
assets/           favicon e immagine social
robots.txt, sitemap.xml, llms.txt
```

## Licenza

[MIT](LICENSE). Non è una prescrizione medica: prima di iniziare un programma di allenamento o una dieta, parlane con un professionista.
