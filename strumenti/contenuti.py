# -*- coding: utf-8 -*-
"""Contenuti delle pagine strumento.

Le keyword e le domande vengono da dati DataForSEO del 26/08/2026 (location 2380,
lingua it): volumi da keywords_data/google_ads/search_volume, domande prese
verbatim dai People Also Ask di serp/google/organic/live/advanced.

Non esiste una pagina separata per "calcolo tdee": in italiano e' la stessa query
di "calcolo fabbisogno calorico" — projectinvictus.it/calcolo-calorie/ ranka su
entrambe con la stessa URL. Due pagine si canniballizzerebbero, quindi TDEE e'
una sezione della pagina del fabbisogno.
"""

FORM = '''<form class="calc" id="strumento-form" onsubmit="return false">
      <div class="mk-head"><b>{titolo}</b><span>{formula}</span></div>
      <div class="crow">
        <div class="fld"><label for="c-sesso">Sesso</label>
          <select id="c-sesso"><option value="M">Uomo</option><option value="F">Donna</option></select></div>
        <div class="fld"><label for="c-eta">Età</label>
          <input type="number" id="c-eta" value="30" min="16" max="80" step="1" inputmode="numeric"></div>
      </div>
      <div class="crow">
        <div class="fld"><label for="c-peso">Peso kg</label>
          <input type="number" id="c-peso" value="75" min="40" max="150" step="0.5" inputmode="decimal"></div>
        <div class="fld"><label for="c-alt">Altezza cm</label>
          <input type="number" id="c-alt" value="175" min="140" max="210" step="1" inputmode="numeric"></div>
      </div>
      <div class="fld"><label for="c-mult">Attività quotidiana</label>
        <select id="c-mult">
          <option value="1.2">Sedentario, lavoro da fermo</option>
          <option value="1.375">Poco attivo, cammino qualche volta</option>
          <option value="1.55" selected>Attivo, cammino ogni giorno</option>
          <option value="1.725">Molto attivo, lavoro in movimento</option>
          <option value="1.9">Attività fisica pesante tutti i giorni</option>
        </select>
      </div>
      <div class="cout" id="cout" data-vista="{vista}" aria-live="polite"></div>
      <a class="btn go" id="c-go" href="../app/">Genera la scheda</a>
      <p class="fine">Nessun dato lascia il browser. I numeri sono una stima da formula: vanno corretti sul peso reale dopo due settimane.</p>
    </form>'''

TAB_LAF = '''<figure style="margin:22px 0 0">
      <figcaption class="eyebrow" style="margin-bottom:8px">I fattori di attività (LAF)</figcaption>
      <table class="params">
        <caption class="sr-only">Fattori di attività fisica e moltiplicatore corrispondente</caption>
        <thead><tr><th scope="col">Stile di vita</th><th scope="col">Fattore</th><th scope="col">Chi ci rientra</th></tr></thead>
        <tbody>
          <tr><td>Sedentario</td><td class="mono">1,2</td><td>Lavoro da fermo, nessun allenamento</td></tr>
          <tr><td>Poco attivo</td><td class="mono">1,375</td><td>Allenamento leggero 1-3 volte a settimana</td></tr>
          <tr><td>Attivo</td><td class="mono">1,55</td><td>Allenamento 3-5 volte a settimana, cammini ogni giorno</td></tr>
          <tr><td>Molto attivo</td><td class="mono">1,725</td><td>Allenamento 6-7 volte a settimana o lavoro in movimento</td></tr>
          <tr><td>Estremamente attivo</td><td class="mono">1,9</td><td>Lavoro fisico pesante più allenamento quotidiano</td></tr>
        </tbody>
      </table>
      <p style="color:var(--ink3); font-size:.85rem; margin-top:10px">Il fattore è la parte meno precisa del calcolo: sovrastimarlo è l'errore più comune, e produce un fabbisogno più alto del reale. Nel dubbio scegli il gradino più basso e correggi dopo due settimane di pesate.</p>
    </figure>'''

PAGINE = [
{
 'slug': 'calcolo-fabbisogno-calorico',
 'nav': 'Fabbisogno calorico',
 'occhiello': 'Metabolismo basale e fabbisogno giornaliero (TDEE) dai tuoi dati, con il fattore di attività spiegato.',
 'title': 'Calcolo fabbisogno calorico giornaliero e metabolismo basale',
 'og_title': 'Calcolo del fabbisogno calorico giornaliero',
 'description': 'Calcola il fabbisogno calorico giornaliero e il metabolismo basale da età, peso, altezza, sesso e attività, con Mifflin-St Jeor. Gratis.',
 'kicker': 'Calcolatore · Mifflin-St Jeor',
 'h1': 'Calcolo del fabbisogno<br>calorico giornaliero',
 'lead': 'Quante calorie consumi in una giornata, contando tutto: il metabolismo basale, il movimento, l\'allenamento e la digestione. Metti i tuoi dati e il numero esce subito, con il basale separato dal totale così vedi da dove viene.',
 'cta': 'Calcola il fabbisogno',
 'nome_tool': 'Calcolatore del fabbisogno calorico giornaliero',
 'entita': ['Fabbisogno calorico giornaliero', 'Metabolismo basale', 'Equazione di Mifflin-St Jeor',
            'Total Daily Energy Expenditure', 'Fattore di attività fisica'],
 'citazioni': [{"@type": "ScholarlyArticle",
                "name": "A new predictive equation for resting energy expenditure in healthy individuals",
                "datePublished": "1990",
                "isPartOf": {"@type": "Periodical", "name": "American Journal of Clinical Nutrition"}}],
 'calcolatore': FORM.format(titolo='Calcola il fabbisogno calorico', formula='Mifflin-St Jeor', vista='fabbisogno'),
 'corpo': '''  <section aria-labelledby="h-cos">
    <div class="eyebrow">La definizione</div>
    <h2 id="h-cos">Che cos'è il fabbisogno calorico giornaliero?</h2>
    <p class="lead-a">È l'energia totale che il tuo corpo consuma in ventiquattr'ore. In inglese si chiama TDEE, Total Daily Energy Expenditure: è lo stesso numero, con un altro nome.</p>
    <div class="split" style="margin-top:22px">
      <div>
        <h3>Da che cosa è composto?</h3>
        <p style="color:var(--ink2)">Da quattro voci. Il <b>metabolismo basale</b> (BMR) è quello che bruci da fermo per tenere in funzione cuore, respiro, cervello e temperatura: da solo vale il 60-70% del totale. Poi c'è la <b>termogenesi indotta dalla dieta</b>, l'energia spesa per digerire, intorno al 10%. Poi l'<b>attività fisica strutturata</b>, cioè l'allenamento. E infine il <b>NEAT</b>, tutto il movimento non sportivo della giornata: camminare, stare in piedi, gesticolare. Il NEAT è la voce che varia di più fra due persone dello stesso peso, e la ragione per cui il fattore di attività è la parte più imprecisa del calcolo.</p>
      </div>
      <div>
        <h3>Come si calcola il metabolismo basale?</h3>
        <p style="color:var(--ink2)">Con l'equazione di Mifflin-St Jeor, che nel 1990 ha sostituito la vecchia Harris-Benedict perché sbaglia meno sulle popolazioni moderne:</p>
        <p class="mono" style="background:var(--surface2); padding:12px 14px; font-size:.88rem; overflow-x:auto">Uomini: 10×peso(kg) + 6,25×altezza(cm) − 5×età + 5<br>Donne: 10×peso(kg) + 6,25×altezza(cm) − 5×età − 161</p>
        <p style="color:var(--ink2)">Il risultato si moltiplica poi per il fattore di attività, e quello è il fabbisogno giornaliero. È esattamente ciò che fa il calcolatore qui sopra.</p>
      </div>
    </div>
''' + '    ' + TAB_LAF + '''
  </section>

  <section aria-labelledby="h-uso">
    <div class="eyebrow">Come si usa</div>
    <h2 id="h-uso">A che cosa serve conoscere il fabbisogno calorico?</h2>
    <p class="lead-a">È il punto di partenza di qualsiasi obiettivo: si dimagrisce mangiando sotto quel numero, si mette peso mangiando sopra, si mantiene restandoci intorno.</p>
    <div class="cards" style="margin-top:20px">
      <div class="card">
        <div class="num">01</div>
        <h3>Per dimagrire</h3>
        <p>Si sottrae un deficit, tipicamente il 15-25% del fabbisogno. <a href="../deficit-calorico/">Il calcolatore del deficit</a> fa il conto e ti dice la perdita attesa a settimana.</p>
      </div>
      <div class="card">
        <div class="num">02</div>
        <h3>Per dividere le calorie</h3>
        <p>Una volta fissato il totale, va ripartito fra proteine, grassi e carboidrati. <a href="../calcolo-macronutrienti/">Il calcolatore dei macronutrienti</a> lo fa in grammi.</p>
      </div>
      <div class="card">
        <div class="num">03</div>
        <h3>Per allenarti di conseguenza</h3>
        <p>Quante calorie mangi decide quanto volume riesci a recuperare. <a href="../scheda-definizione/">La scheda di definizione</a> parte da lì.</p>
      </div>
    </div>
  </section>

  <section aria-labelledby="h-limiti">
    <div class="eyebrow">Precisione</div>
    <h2 id="h-limiti">Quanto è preciso questo calcolo?</h2>
    <p class="lead-a">Sbaglia di circa ±10% sulla maggior parte delle persone, e di più su chi sta agli estremi di peso o composizione corporea. È una stima statistica, non una misura.</p>
    <p style="color:var(--ink2); max-width:70ch">L'equazione è costruita su medie di popolazione: due persone con gli stessi peso, altezza, età e sesso possono avere fabbisogni diversi di parecchie centinaia di calorie, per massa magra, genetica, tiroide, farmaci e soprattutto NEAT. La misura vera si fa con la calorimetria indiretta, che richiede un laboratorio. Per questo il numero che leggi qui va trattato come un punto di partenza: mangi a quel livello per due settimane, pesi il risultato e correggi. Il dato reale è la variazione sulla bilancia, non l'output della formula.</p>
  </section>
''',
 'faq': [
  ("Qual è la differenza tra BMR e TDEE?",
   "Il BMR è quello che consumi da fermo, il TDEE è quello che consumi vivendo la tua giornata. Il metabolismo basale (BMR) è l'energia minima per tenere in funzione l'organismo a riposo assoluto, e vale il 60-70% del totale. Il fabbisogno calorico giornaliero (TDEE) è il BMR moltiplicato per un fattore che aggiunge movimento, allenamento e digestione. Il calcolatore mostra entrambi: il deficit per dimagrire si sottrae sempre dal TDEE, mai dal BMR."),
  ("Come faccio a calcolare il mio fabbisogno calorico giornaliero?",
   "Calcoli prima il metabolismo basale con Mifflin-St Jeor (10×peso in kg + 6,25×altezza in cm − 5×età, più 5 per gli uomini o meno 161 per le donne), poi lo moltiplichi per il fattore di attività che corrisponde al tuo stile di vita, da 1,2 se sei sedentario a 1,9 se fai un lavoro fisico pesante. Il calcolatore in cima alla pagina fa entrambi i passaggi e ti mostra i due numeri separati."),
  ("Come posso calcolare il fabbisogno calorico in base al mio peso?",
   "Il peso da solo non basta: la stessa equazione ha bisogno anche di altezza, età e sesso, perché a parità di peso una persona alta e giovane consuma più di una bassa e anziana. Esistono regole spannometriche del tipo 30-33 kcal per kg di peso corporeo, ma hanno un margine di errore molto più largo. Se vuoi un numero utile, servono i quattro dati."),
  ("Perché il mio fabbisogno calorico sembra troppo alto?",
   "Quasi sempre perché il fattore di attività scelto è troppo generoso. \"Attivo\" non significa allenarsi tre volte a settimana stando poi seduto tutto il giorno: quella è una giornata da 1,375. La differenza fra 1,55 e 1,725 su un basale di 1.700 kcal vale quasi 300 kcal, cioè la differenza fra dimagrire e stare fermi. Nel dubbio scendi di un gradino."),
  ("Il fabbisogno calorico cambia mentre dimagrisco?",
   "Sì, e scende. Perdendo peso il metabolismo basale cala perché c'è meno massa da mantenere, e in deficit prolungato tende a calare anche il NEAT: ci si muove meno senza accorgersene. È il motivo per cui un deficit che funzionava all'inizio smette di funzionare dopo qualche settimana. Il calcolo va rifatto ogni 4-5 kg persi, o quando il peso si ferma per due settimane di fila."),
  ("Il calcolo vale anche per le donne?",
   "Sì. L'equazione di Mifflin-St Jeor ha un coefficiente diverso per sesso (−161 per le donne invece di +5), quindi il risultato esce già tarato. A parità di peso e altezza il fabbisogno femminile è più basso, perché in media la massa magra è inferiore."),
 ],
},
{
 'slug': 'deficit-calorico',
 'nav': 'Deficit calorico',
 'occhiello': 'Quanto tagliare per dimagrire senza perdere muscolo, con la perdita attesa a settimana.',
 'title': 'Deficit calorico: che cos\'è, come si calcola e quanto farlo',
 'og_title': 'Deficit calorico: come si calcola',
 'description': 'Calcola il deficit calorico dai tuoi dati e scopri quante calorie mangiare per dimagrire, con la perdita di peso attesa a settimana. Gratis.',
 'kicker': 'Calcolatore · deficit',
 'h1': 'Deficit calorico:<br>quanto tagliare<br><span style="color:var(--accent)">senza perdere muscolo.</span>',
 'lead': 'Il deficit è la differenza fra quello che consumi e quello che mangi. Qui lo calcoli dai tuoi dati e vedi subito la perdita attesa a settimana, con il limite oltre il quale smetti di perdere solo grasso.',
 'cta': 'Calcola il deficit',
 'nome_tool': 'Calcolatore del deficit calorico',
 'entita': ['Deficit calorico', 'Perdita di peso', 'Metabolismo basale', 'Massa magra'],
 'citazioni': [{"@type": "ScholarlyArticle",
                "name": "Effect of two different weight-loss rates on body composition and strength and power-related performance in elite athletes",
                "datePublished": "2011",
                "isPartOf": {"@type": "Periodical", "name": "International Journal of Sport Nutrition and Exercise Metabolism"}}],
 'calcolatore': FORM.format(titolo='Calcola il tuo deficit', formula='deficit 15-25%', vista='deficit'),
 'corpo': '''  <section aria-labelledby="h-cos">
    <div class="eyebrow">La definizione</div>
    <h2 id="h-cos">Che cos'è il deficit calorico?</h2>
    <p class="lead-a">È mangiare meno calorie di quante ne consumi, così il corpo copre la differenza attingendo alle riserve. È l'unica condizione necessaria perché il grasso scenda: nessun alimento, orario o integratore la sostituisce.</p>
    <p style="color:var(--ink2); max-width:70ch; margin-top:14px">Il punto di partenza è il <a href="../calcolo-fabbisogno-calorico/">fabbisogno calorico giornaliero</a>: da lì si sottrae il deficit. Un chilo di tessuto adiposo contiene circa 7.700 kcal, quindi un deficit di 500 kcal al giorno vale in teoria poco meno di mezzo chilo a settimana. "In teoria", perché il corpo si adatta: il metabolismo cala insieme al peso e il movimento spontaneo si riduce, quindi il ritmo reale è quasi sempre più lento di quello aritmetico.</p>
  </section>

  <section aria-labelledby="h-quanto">
    <div class="eyebrow">La dose</div>
    <h2 id="h-quanto">Qual è il deficit calorico consigliato per dimagrire?</h2>
    <p class="lead-a">Fra il 15% e il 25% del fabbisogno, che per la maggior parte delle persone significa 400-700 kcal al giorno e una perdita fra lo 0,5% e lo 0,8% del peso corporeo a settimana.</p>
    <figure style="margin:22px 0 0">
      <figcaption class="eyebrow" style="margin-bottom:8px">Quanto deficit, e che cosa comporta</figcaption>
      <table class="params">
        <caption class="sr-only">Intensità del deficit calorico e conseguenze</caption>
        <thead><tr><th scope="col">Deficit</th><th scope="col">Perdita a settimana</th><th scope="col">Che cosa aspettarsi</th></tr></thead>
        <tbody>
          <tr><td>10-15%</td><td class="mono">0,3-0,5%</td><td>Lento, molto sostenibile. Adatto a chi è già magro o ha molto tempo.</td></tr>
          <tr><td>15-25%</td><td class="mono">0,5-0,8%</td><td>La fascia di riferimento: buon compromesso fra velocità e massa magra difesa.</td></tr>
          <tr><td>25-35%</td><td class="mono">0,8-1,2%</td><td>Aggressivo. Fame, carichi in calo, va tenuto per periodi brevi.</td></tr>
          <tr><td>oltre il 35%</td><td class="mono">oltre 1,2%</td><td>Massa magra a rischio, prestazioni giù, aderenza bassa. Raramente conviene.</td></tr>
        </tbody>
      </table>
      <p style="color:var(--ink3); font-size:.85rem; margin-top:10px">Su atleti allenati, un ritmo intorno allo 0,7% del peso a settimana conserva la massa magra molto meglio di uno intorno all'1,4% a parità di grasso perso (Garthe et al., 2011). Il calcolatore usa circa 625 kcal come riferimento e non lascia mai il target sotto il metabolismo basale.</p>
    </figure>
  </section>

  <section aria-labelledby="h-come">
    <div class="eyebrow">In pratica</div>
    <h2 id="h-come">Come si fa ad andare in deficit calorico?</h2>
    <p class="lead-a">Si calcola il fabbisogno, si sottrae il deficit e si verifica il risultato sulla bilancia dopo due settimane. Se il peso non scende, il deficit non c'è: conta il dato, non il calcolo.</p>
    <div class="cards" style="margin-top:20px">
      <div class="card">
        <div class="num">01</div>
        <h3>Fissa il numero</h3>
        <p>Fabbisogno meno deficit. Poi dividi le calorie in <a href="../calcolo-macronutrienti/">proteine, grassi e carboidrati</a>: le proteine alte sono ciò che protegge la massa magra mentre il peso scende.</p>
      </div>
      <div class="card">
        <div class="num">02</div>
        <h3>Muoviti più che tagliare</h3>
        <p>Aumentare i passi crea deficit senza togliere altro cibo, e costa molto meno recupero del cardio strutturato. Il riferimento è 15.000 passi al giorno.</p>
      </div>
      <div class="card">
        <div class="num">03</div>
        <h3>Allena la forza</h3>
        <p>Senza uno stimolo allenante il corpo non ha motivo di tenere il muscolo. <a href="../scheda-definizione/">Una scheda pensata per il deficit</a> difende i carichi invece di inseguire la fatica.</p>
      </div>
    </div>
  </section>

  <section aria-labelledby="h-errori">
    <div class="eyebrow">Attenzione</div>
    <h2 id="h-errori">Si può esagerare con il deficit?</h2>
    <p class="lead-a">Sì, e i segnali arrivano prima sulla prestazione che sulla bilancia: i carichi crollano su tutti gli esercizi insieme, la fame diventa ingestibile, il sonno peggiora.</p>
    <p style="color:var(--ink2); max-width:70ch">Il target calorico non dovrebbe mai finire sotto il metabolismo basale: per questo il calcolatore riduce il deficit quando succede, invece di tagliare comunque, e lo dichiara in pagina. Un deficit troppo profondo non fa perdere grasso più in fretta in proporzione a quello che costa: fa perdere massa magra, abbassa il dispendio e rende il recupero impossibile. Se ti riconosci in quei segnali, la risposta non è tagliare ancora, è risalire per qualche giorno e poi ripartire più piano. In presenza di patologie, gravidanza o disturbi del comportamento alimentare, un deficit va impostato con un medico, non con un calcolatore.</p>
  </section>
''',
 'faq': [
  ("Come si fa ad andare in deficit calorico?",
   "Si calcola il fabbisogno calorico giornaliero e si mangia stabilmente sotto quel numero, verificando il risultato sulla bilancia. In pratica: calcoli il fabbisogno dai tuoi dati, sottrai il 15-25%, distribuisci le calorie in macronutrienti tenendo alte le proteine, e dopo due settimane confronti la variazione di peso con quella attesa. Se il peso non si muove, il deficit reale non c'è: si corregge sul dato, non sulla formula."),
  ("Qual è il deficit calorico consigliato per dimagrire?",
   "Fra il 15% e il 25% del fabbisogno giornaliero, cioè 400-700 kcal al giorno per la maggior parte delle persone. Corrisponde a una perdita fra lo 0,5% e lo 0,8% del peso corporeo a settimana: su 80 kg significa 0,4-0,65 kg. Deficit più profondi accelerano la bilancia ma costano massa magra, fame e prestazioni in palestra."),
  ("Quanto tempo ci vuole per vedere i risultati?",
   "Sulla bilancia la prima settimana si vede quasi sempre un calo marcato, ma è in gran parte acqua e glicogeno e non va letto come grasso perso. Il dato affidabile arriva dalla media di due settimane. Allo specchio, i cambiamenti visibili richiedono di solito 4-6 settimane di deficit costante, perché la differenza percettibile arriva dopo qualche chilo, non dopo qualche etto."),
  ("Cosa succede se mangio troppo poco?",
   "Il peso scende, ma scende male: insieme al grasso se ne va la massa magra, il dispendio energetico si abbassa, i carichi in palestra crollano e la fame diventa difficile da gestire. Sul medio periodo l'aderenza si rompe e si torna indietro. Il segnale d'allarme più affidabile è il log dell'allenamento: se i chili calano su tutti gli esercizi contemporaneamente, il problema è il deficit o il sonno, non la scheda."),
  ("Il deficit calorico va tenuto anche nel weekend?",
   "La media della settimana è ciò che conta, non il singolo giorno. Si può tenere il deficit più profondo nei feriali e lasciare il weekend più alto, purché la media settimanale resti quella prescritta: è l'approccio che il calcolatore applica di default, perché regge socialmente molto meglio di sette giorni identici. Quello che non funziona è compensare un weekend fuori controllo con feriali da fame."),
  ("Serve fare cardio per andare in deficit?",
   "No, non è necessario: il deficit si può creare interamente con la dieta. Il cardio è uno strumento in più, utile quando tagliare ancora il cibo diventa insostenibile, ma compete con l'allenamento coi pesi per lo stesso recupero. A parità di calorie bruciate, aumentare i passi quotidiani costa molto meno recupero di una sessione di cardio strutturata."),
 ],
},
{
 'slug': 'calcolo-macronutrienti',
 'nav': 'Macronutrienti',
 'occhiello': 'Proteine, grassi e carboidrati in grammi e in g/kg, calcolati sulle tue calorie.',
 'title': 'Calcolo macronutrienti: proteine, grassi e carboidrati',
 'og_title': 'Calcolo dei macronutrienti',
 'description': 'Calcola proteine, grassi e carboidrati in grammi e in g/kg dalle tue calorie e dal tuo peso, con la logica che decide quale macro si muove.',
 'kicker': 'Calcolatore · macro',
 'h1': 'Calcolo dei<br>macronutrienti',
 'lead': 'Fissate le calorie, resta da dividerle. Qui vedi proteine, grassi e carboidrati in grammi e in grammi per chilo di peso, con la logica che decide quale dei tre si muove quando cambia il totale.',
 'cta': 'Calcola i macro',
 'nome_tool': 'Calcolatore dei macronutrienti',
 'entita': ['Macronutrienti', 'Proteine', 'Carboidrati', 'Grassi', 'Ripartizione calorica'],
 'citazioni': [{"@type": "ScholarlyArticle",
                "name": "A systematic review, meta-analysis and meta-regression of the effect of protein supplementation on resistance training-induced gains in muscle mass and strength",
                "datePublished": "2018",
                "isPartOf": {"@type": "Periodical", "name": "British Journal of Sports Medicine"}}],
 'calcolatore': FORM.format(titolo='Calcola i tuoi macro', formula='2 g/kg · 0,75 g/kg', vista='macro'),
 'corpo': '''  <section aria-labelledby="h-cos">
    <div class="eyebrow">La definizione</div>
    <h2 id="h-cos">Quali sono i macronutrienti?</h2>
    <p class="lead-a">Proteine, carboidrati e grassi: i tre nutrienti che forniscono energia. Le calorie di una giornata sono la somma di quei tre, in proporzioni che decidi tu.</p>
    <figure style="margin:22px 0 0">
      <figcaption class="eyebrow" style="margin-bottom:8px">Quanto rende un grammo</figcaption>
      <table class="params">
        <caption class="sr-only">Macronutrienti, calorie per grammo e funzione</caption>
        <thead><tr><th scope="col">Macronutriente</th><th scope="col">kcal per grammo</th><th scope="col">A cosa serve</th></tr></thead>
        <tbody>
          <tr><td>Proteine</td><td class="mono">4</td><td>Costruiscono e difendono il tessuto muscolare. In deficit sono il macro che protegge la massa magra.</td></tr>
          <tr><td>Carboidrati</td><td class="mono">4</td><td>Alimentano le sedute e riempiono le scorte di glicogeno. Sono la variabile di aggiustamento.</td></tr>
          <tr><td>Grassi</td><td class="mono">9</td><td>Servono agli ormoni e all'assorbimento delle vitamine liposolubili. Hanno un pavimento sotto cui non conviene scendere.</td></tr>
          <tr><td>Alcol</td><td class="mono">7</td><td>Fornisce calorie senza funzione nutrizionale, e peggiora il recupero.</td></tr>
        </tbody>
      </table>
    </figure>
  </section>

  <section aria-labelledby="h-come">
    <div class="eyebrow">Il metodo</div>
    <h2 id="h-come">Come si calcolano i macronutrienti?</h2>
    <p class="lead-a">Prima si fissano proteine e grassi sul peso corporeo, poi i carboidrati riempiono le calorie che restano. Non si parte da percentuali: si parte da grammi per chilo.</p>
    <div class="split" style="margin-top:22px">
      <div>
        <h3>Perché non con le percentuali?</h3>
        <p style="color:var(--ink2)">Perché una percentuale fissa dà risultati assurdi agli estremi. Il 30% di proteine su 1.400 kcal sono 105 g, troppo pochi per un uomo di 90 kg; lo stesso 30% su 3.500 kcal sono 262 g, molto più del necessario. Il fabbisogno di proteine e grassi dipende dal <b>corpo</b>, non dalle calorie: per questo si fissano in grammi per chilo di peso, e sono i carboidrati ad assorbire la differenza.</p>
      </div>
      <div>
        <h3>I riferimenti usati qui</h3>
        <p class="mono" style="background:var(--surface2); padding:12px 14px; font-size:.88rem; overflow-x:auto">Proteine = peso × 2,0 g<br>Grassi&nbsp;&nbsp;&nbsp;= peso × 0,75 g<br>Carboidrati = (kcal − prot×4 − gras×9) ÷ 4</p>
        <p style="color:var(--ink2)">Due grammi di proteine per chilo stanno nella fascia in cui i guadagni di massa e forza smettono di aumentare aggiungendone altre (Morton et al., 2018), con un margine di sicurezza utile in deficit. I grassi a 0,75 g/kg restano sopra il minimo ormonale senza rubare troppo spazio ai carboidrati.</p>
      </div>
    </div>
  </section>

  <section aria-labelledby="h-cambia">
    <div class="eyebrow">Gli aggiustamenti</div>
    <h2 id="h-cambia">Che cosa cambia fra massa e definizione?</h2>
    <p class="lead-a">Cambiano quasi solo i carboidrati. Proteine e grassi restano ancorati al peso corporeo, mentre il totale calorico sale o scende.</p>
    <p style="color:var(--ink2); max-width:70ch">In <a href="../deficit-calorico/">deficit</a> le proteine se mai salgono leggermente, perché il rischio di perdere massa magra aumenta quando l'energia scarseggia, e i grassi tengono il loro pavimento: la riduzione la assorbono i carboidrati. In surplus succede il contrario. È il motivo per cui, mentre un blocco di definizione avanza e le calorie scendono, il numero che vedi cambiare settimana dopo settimana è quasi sempre quello dei carboidrati — e con esso l'energia che hai a disposizione per allenarti, che è la ragione per cui il volume di allenamento va gestito di conseguenza.</p>
  </section>
''',
 'faq': [
  ("Come si calcolano i macronutrienti?",
   "Prima si fissano proteine e grassi in base al peso corporeo, poi i carboidrati riempiono le calorie che restano. Qui le proteine stanno a 2 g per kg di peso e i grassi a 0,75 g per kg: moltiplicando le proteine per 4 kcal al grammo e i grassi per 9, e sottraendo il risultato dal totale calorico, quello che avanza diviso 4 dà i grammi di carboidrati. È il motivo per cui i carboidrati sono il macro che si muove quando cambiano le calorie."),
  ("Quali sono i macronutrienti?",
   "Proteine, carboidrati e grassi. Sono i nutrienti che forniscono energia: le proteine e i carboidrati rendono 4 kcal per grammo, i grassi 9. Si chiamano macro per distinguerli dai micronutrienti — vitamine e minerali — che sono indispensabili ma non apportano calorie. Anche l'alcol fornisce energia, 7 kcal per grammo, senza però avere una funzione nutrizionale."),
  ("Quante proteine servono al giorno?",
   "Intorno a 1,6-2,2 g per kg di peso corporeo per chi si allena con i pesi; il calcolatore usa 2,0 g/kg. Oltre quella fascia i guadagni di massa e forza smettono di aumentare in modo apprezzabile. In deficit calorico conviene stare nella parte alta dell'intervallo, perché è la quota proteica che difende la massa magra mentre il peso scende."),
  ("Quanti grassi al minimo?",
   "Sotto circa 0,5 g per kg di peso corporeo la produzione ormonale e l'assorbimento delle vitamine liposolubili iniziano a risentirne. Il riferimento di 0,75 g/kg usato qui tiene un margine sopra quel pavimento, lasciando comunque spazio ai carboidrati. Tagliare i grassi all'osso per fare posto ai carboidrati è un errore frequente nelle diete di definizione fai-da-te."),
  ("Bisogna pesare tutto quello che si mangia?",
   "All'inizio conviene farlo per due o tre settimane, non per sempre: serve a costruire il riferimento visivo di quanto sono davvero cento grammi di riso o venti di olio. Dopo, la maggior parte delle persone riesce a stimare con un errore accettabile. Quello che non funziona è stimare fin dal primo giorno: l'errore medio delle autovalutazioni è nell'ordine del 20-30%, abbastanza da annullare un deficit intero."),
  ("Contano di più le calorie o i macronutrienti?",
   "Le calorie decidono se il peso sale o scende; i macronutrienti decidono in gran parte da cosa è fatto quel cambiamento. Puoi dimagrire con qualsiasi ripartizione, purché il totale sia in deficit, ma con proteine basse una parte di quel peso sarà muscolo. Prima si sistema il totale, poi la divisione."),
 ],
},
{
 'slug': 'scheda-definizione',
 'nav': 'Scheda definizione',
 'occhiello': 'Come si struttura l\'allenamento quando le calorie sono basse, e il generatore che la scrive.',
 'title': 'Scheda definizione: allenarsi in deficit calorico',
 'og_title': 'Scheda per la definizione muscolare',
 'description': 'Come si costruisce una scheda di definizione: volume su due distretti, carichi difesi, cinque sedute. Con il generatore che la scrive. Gratis.',
 'kicker': 'Scheda · definizione',
 'h1': 'Scheda definizione:<br>il volume dove serve,<br><span style="color:var(--accent)">i carichi difesi.</span>',
 'lead': 'In definizione il recupero è la risorsa scarsa, quindi una scheda che spinge su tutto non funziona. Qui trovi come si struttura il blocco, e il generatore che lo scrive sui tuoi dati con serie, ripetizioni e recuperi.',
 'cta': 'Calcola le calorie',
 'nome_tool': 'Generatore di schede di definizione',
 'entita': ['Definizione muscolare', 'Volume di allenamento', 'Mesociclo di specializzazione',
            'Volume minimo efficace', 'Volume massimo recuperabile'],
 'citazioni': [{"@type": "ScholarlyArticle",
                "name": "Dose-response relationship between weekly resistance training volume and increases in muscle mass",
                "datePublished": "2017",
                "isPartOf": {"@type": "Periodical", "name": "Journal of Sports Sciences"}}],
 'calcolatore': FORM.format(titolo='Le calorie della tua definizione', formula='Mifflin-St Jeor', vista='fabbisogno'),
 'corpo': '''  <section aria-labelledby="h-principio">
    <div class="eyebrow">Il principio</div>
    <h2 id="h-principio">Come deve cambiare l'allenamento in definizione?</h2>
    <p class="lead-a">Meno di quanto si crede sul come, molto sul dove. Gli esercizi e i carichi restano quelli della massa: quello che cambia è la distribuzione del volume, perché mangiando meno se ne recupera meno.</p>
    <p style="color:var(--ink2); max-width:70ch; margin-top:14px">L'errore più diffuso è il contrario di quello che serve: si alzano le ripetizioni, si accorciano i recuperi e si trasforma la palestra in cardio con i manubri, nella convinzione che così "si definisca". Il risultato è che si perde lo stimolo che dice al corpo di tenere il muscolo, proprio quando l'energia scarseggia. Il carico pesante è il segnale che difende la massa magra: si difende, non si abbandona. Quello che va ridotto è la quantità totale di lavoro, e va concentrata dove conta.</p>
  </section>

  <section aria-labelledby="h-volume">
    <div class="eyebrow">Il volume</div>
    <h2 id="h-volume">Quante serie a settimana per ogni distretto?</h2>
    <p class="lead-a">Fra il minimo che mantiene e il tetto che riesci a recuperare, e in deficit quel tetto si abbassa. Ecco le tacche di riferimento, in serie allenanti a settimana.</p>
    <figure style="margin:22px 0 0">
      <figcaption class="eyebrow" style="margin-bottom:8px">Serie a settimana per distretto</figcaption>
      <table class="params">
        <caption class="sr-only">Volumi settimanali di riferimento per distretto: MEV, MAV e MRV</caption>
        <thead><tr><th scope="col">Distretto</th><th scope="col">MEV</th><th scope="col">MAV</th><th scope="col">MRV</th></tr></thead>
        <tbody>
          <tr><td>Petto</td><td class="mono">8</td><td class="mono">15</td><td class="mono">22</td></tr>
          <tr><td>Dorso</td><td class="mono">10</td><td class="mono">16</td><td class="mono">25</td></tr>
          <tr><td>Delt laterali/posteriori</td><td class="mono">6</td><td class="mono">13</td><td class="mono">26</td></tr>
          <tr><td>Bicipiti</td><td class="mono">6</td><td class="mono">13</td><td class="mono">26</td></tr>
          <tr><td>Tricipiti</td><td class="mono">6</td><td class="mono">13</td><td class="mono">20</td></tr>
          <tr><td>Quadricipiti</td><td class="mono">8</td><td class="mono">15</td><td class="mono">20</td></tr>
          <tr><td>Femorali</td><td class="mono">4</td><td class="mono">10</td><td class="mono">20</td></tr>
          <tr><td>Glutei</td><td class="mono">0</td><td class="mono">10</td><td class="mono">20</td></tr>
          <tr><td>Polpacci</td><td class="mono">10</td><td class="mono">22</td><td class="mono">26</td></tr>
          <tr><td>Addome</td><td class="mono">0</td><td class="mono">25</td><td class="mono">28</td></tr>
        </tbody>
      </table>
      <p style="color:var(--ink3); font-size:.85rem; margin-top:10px"><b>MEV</b> è il volume minimo efficace, il minimo che mantiene quello che hai. <b>MAV</b> è la fascia più produttiva. <b>MRV</b> è il tetto oltre il quale accumuli fatica senza ricavarne stimolo. Sono riferimenti di partenza, non prescrizioni: il tuo numero si trova alzando il volume finché il log smette di migliorare, poi tornando indietro.</p>
    </figure>
  </section>

  <section aria-labelledby="h-struttura">
    <div class="eyebrow">La struttura</div>
    <h2 id="h-struttura">Come si distribuisce il lavoro sulla settimana?</h2>
    <p class="lead-a">Due distretti target tengono il volume alto e si allenano due volte a settimana; tutti gli altri restano al volume che mantiene. Cinque sedute, ognuna con esercizi che hanno un ruolo preciso.</p>
    <figure style="margin:22px 0 0">
      <figcaption class="eyebrow" style="margin-bottom:8px">Parametri per ruolo</figcaption>
      <table class="params">
        <caption class="sr-only">Serie, ripetizioni, ripetizioni efficaci e recupero per ruolo</caption>
        <thead><tr><th scope="col">Ruolo</th><th scope="col">Serie × reps</th><th scope="col">ER</th><th scope="col">Recupero</th><th scope="col">Tecnica</th></tr></thead>
        <tbody>
          <tr><td>Esercizio madre</td><td class="mono">4 × 6-8</td><td class="mono">20</td><td class="mono">1,5-3′</td><td>—</td></tr>
          <tr><td>Meccanici</td><td class="mono">3 × 8-10</td><td class="mono">15</td><td class="mono">1,5-3′</td><td>—</td></tr>
          <tr><td>Isolamenti</td><td class="mono">3 × 10-12</td><td class="mono">15</td><td class="mono">60-90″</td><td>SQUEEZE</td></tr>
        </tbody>
      </table>
      <p style="color:var(--ink3); font-size:.85rem; margin-top:10px">La progressione è double progression sul log: si registrano carico, ripetizioni totali e RPE, e la settimana dopo si batte il log — prima più ripetizioni dentro il range, poi più carico. <a href="../app/">Il generatore</a> scrive tutto questo sui tuoi dati, con alternative per ogni esercizio.</p>
    </figure>
  </section>

  <section aria-labelledby="h-durata">
    <div class="eyebrow">La durata</div>
    <h2 id="h-durata">Quanto deve durare un blocco di definizione?</h2>
    <p class="lead-a">Da 8 a 16 settimane, scarichi inclusi. Meno non basta perché la specializzazione si veda, di più accumula fatica più in fretta di quanto il deficit permetta di smaltirla.</p>
    <p style="color:var(--ink2); max-width:70ch">Finito il blocco si cambiano i due distretti target, così nell'arco di un anno ognuno ha il suo turno di volume alto. Le calorie seguono lo stesso arco: si parte dal <a href="../calcolo-fabbisogno-calorico/">fabbisogno calcolato</a>, si applica il <a href="../deficit-calorico/">deficit</a> e si aggiusta sul peso reale. Quello che non va fatto è tenere il deficit aperto a tempo indeterminato: a un certo punto conviene risalire, non perché il grasso sia finito, ma perché il recupero e la testa hanno un limite.</p>
  </section>
''',
 'faq': [
  ("Come si fa una scheda per la definizione?",
   "Si concentra il volume alto su due distretti e si tiene tutto il resto al volume di mantenimento, distribuendo il lavoro su cinque sedute a settimana. Gli esercizi e i carichi restano quelli di un blocco di massa: quello che cambia è quanto lavoro totale ti puoi permettere, perché in deficit calorico il recupero è ridotto. Ogni seduta apre con un esercizio pesante, prosegue con i multiarticolari e chiude con gli isolamenti."),
  ("Quanti kg si perdono in definizione?",
   "Dipende dalla durata del blocco e da quanto grasso c'è da perdere, ma il ritmo sostenibile è intorno allo 0,5-0,8% del peso corporeo a settimana. Su 80 kg significa 0,4-0,65 kg a settimana, cioè 5-10 kg in un blocco di 12-16 settimane. La prima settimana il calo è quasi sempre più marcato per acqua e glicogeno, e non va contato come grasso perso."),
  ("Bisogna alzare le ripetizioni e accorciare i recuperi?",
   "No, ed è l'errore più diffuso. Alzare le ripetizioni e togliere recupero riduce il carico che riesci a muovere, cioè proprio il segnale che dice al corpo di conservare il muscolo mentre l'energia scarseggia. Il grasso lo perde il deficit calorico, non la sensazione di fatica in palestra. In definizione i carichi si difendono: quello che si riduce è la quantità totale di lavoro."),
  ("Si può mettere massa mentre si è in definizione?",
   "Per chi si allena da anni, quasi mai: in deficit la crescita rallenta o si ferma, e l'obiettivo realistico è conservare la massa magra. Chi si allena da poco, riparte dopo una lunga pausa o ha molto grasso da perdere può ancora guadagnare qualcosa, ed è il motivo per cui il volume alto va comunque messo da qualche parte invece che spalmato su tutto il corpo."),
  ("Quanti giorni a settimana allenarsi in definizione?",
   "Cinque sedute è la frequenza su cui è costruito il generatore: consente di allenare i due distretti target due volte ciascuno e di tenere tutti gli altri sopra il volume di mantenimento. Con meno sedute un cut resta possibile, ma il volume si comprime in sessioni più lunghe, che in deficit sono più difficili da recuperare."),
  ("Serve il cardio in una scheda di definizione?",
   "Non è obbligatorio: il deficit si crea con la dieta. Il cardio serve quando tagliare ancora il cibo diventa insostenibile, ma consuma lo stesso recupero dell'allenamento coi pesi. A parità di calorie, aumentare i passi quotidiani è più efficiente: il riferimento è 15.000 passi al giorno, che muovono più energia di una sessione di cardio e costano molto meno."),
 ],
},
]

CALCOLATORE_JS = r'''
/* Stessa aritmetica della landing e del generatore: i numeri devono combaciare
   fra le pagine, quindi la formula sta in un punto solo. La vista cambia solo
   quali righe vengono mostrate. */
(function(){
  var F = {sesso:"c-sesso", eta:"c-eta", peso:"c-peso", alt:"c-alt", mult:"c-mult"};
  Object.keys(F).forEach(function(k){ F[k] = document.getElementById(F[k]); });
  var out = document.getElementById("cout"), go = document.getElementById("c-go");
  if(!out || !go || Object.keys(F).some(function(k){ return !F[k]; })) return;
  var vista = out.getAttribute("data-vista") || "fabbisogno";
  var LIM = {eta:[16,80,30], peso:[40,150,75], alt:[140,210,175]};
  var nf = new Intl.NumberFormat("it-IT");
  var n1 = new Intl.NumberFormat("it-IT", {minimumFractionDigits:1, maximumFractionDigits:1});
  var n2 = new Intl.NumberFormat("it-IT", {minimumFractionDigits:2, maximumFractionDigits:2});
  var n3 = new Intl.NumberFormat("it-IT", {minimumFractionDigits:0, maximumFractionDigits:3});

  function val(k){
    var lim = LIM[k], v = parseFloat(F[k].value);
    return isFinite(v) ? Math.min(lim[1], Math.max(lim[0], v)) : lim[2];
  }
  function row(k, v, cls){
    return '<div class="r'+(cls?" "+cls:"")+'"><span class="k">'+k+'</span><span class="v">'+v+'</span></div>';
  }
  function calc(){
    var sesso = F.sesso.value === "F" ? "F" : "M";
    var mult = parseFloat(F.mult.value) || 1.55;
    var peso = val("peso"), eta = val("eta"), alt = val("alt");
    var bmr = 10*peso + 6.25*alt - 5*eta + (sesso === "M" ? 5 : -161);
    var tdee = bmr*mult;
    var grezzo = Math.round(tdee - 625);
    var media = Math.max(grezzo, Math.round(bmr));
    var deficit = Math.round(tdee) - media;
    var ridotto = media > grezzo;
    var feriali = media - 170;
    var weekend = Math.round((media*7 - feriali*5)/2);
    var P = Math.round(peso*2.0), G = Math.round(peso*0.75);
    var C = Math.max(0, Math.round((media - P*4 - G*9)/4));
    var kgSett = deficit*7/7700;
    var pctPeso = kgSett/peso*100;
    var h = "";

    if(vista === "fabbisogno"){
      h += row("Fabbisogno giornaliero (TDEE)", nf.format(Math.round(tdee))+" kcal", "big");
      h += row("Metabolismo basale (BMR)", nf.format(Math.round(bmr))+" kcal");
      h += row("Fattore di attività", "× "+n3.format(mult));
      h += row("Quota da movimento", nf.format(Math.round(tdee-bmr))+" kcal");
      h += row("Per mantenere il peso", nf.format(Math.round(tdee))+" kcal al giorno");
      h += row("Per dimagrire (−15%)", nf.format(Math.round(tdee*0.85))+" kcal al giorno");
      h += row("Per dimagrire (−25%)", nf.format(Math.round(tdee*0.75))+" kcal al giorno");
    } else if(vista === "deficit"){
      h += row("Calorie in deficit", nf.format(media)+" kcal", "big");
      h += row("Fabbisogno giornaliero", nf.format(Math.round(tdee))+" kcal");
      h += row("Deficit applicato", "−"+nf.format(deficit)+" kcal al giorno");
      h += row("In percentuale", "−"+n1.format(deficit/tdee*100)+"% del fabbisogno");
      h += row("Perdita attesa", "−"+n2.format(kgSett)+" kg a settimana");
      h += row("Sul peso corporeo", "−"+n2.format(pctPeso)+"% a settimana");
      h += row("Feriali / weekend", nf.format(feriali)+" / "+nf.format(weekend)+" kcal");
      h += row("Pavimento (BMR)", nf.format(Math.round(bmr))+" kcal, da non superare in basso");
    } else {
      h += row("Calorie di riferimento", nf.format(media)+" kcal", "big");
      h += row("Proteine", nf.format(P)+" g · 2,0 g/kg · "+nf.format(P*4)+" kcal");
      h += row("Grassi", nf.format(G)+" g · 0,75 g/kg · "+nf.format(G*9)+" kcal");
      h += row("Carboidrati", nf.format(C)+" g · "+n1.format(C/peso)+" g/kg · "+nf.format(C*4)+" kcal");
      h += row("Ripartizione", n1.format(P*4/media*100)+"% / "+n1.format(G*9/media*100)+"% / "+n1.format(C*4/media*100)+"%");
      h += row("Fabbisogno giornaliero", nf.format(Math.round(tdee))+" kcal");
    }

    if(ridotto && vista !== "fabbisogno"){
      h += '<p class="fine" style="color:var(--crit); margin:8px 0 0">Il deficit pieno di 625 kcal ti porterebbe sotto il metabolismo basale, quindi è stato ridotto a '+nf.format(deficit)+' kcal. Con numeri così bassi vale la pena farsi seguire da un professionista.</p>';
    }
    out.innerHTML = h;
    go.setAttribute("href", "../app/?sesso="+sesso+"&eta="+eta+"&peso="+peso+"&alt="+alt+"&mult="+mult);
  }
  Object.keys(F).forEach(function(k){
    F[k].addEventListener("input", calc);
    F[k].addEventListener("change", calc);
  });
  calc();
})();
'''
