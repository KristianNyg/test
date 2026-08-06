# MASTERPROMPT — Hormuz-krisen, helgeanalyse 7.–11. august 2026

## "Country of genius": parallelle desker med uavhengig research, tvungen divergens, deretter rundebord

---

## SLIK BRUKER DU DENNE FILEN

1. Lagre hele filen som `MASTERPROMPT.md` i en tom mappe.

2. Åpne Claude Code i den mappen.

3. Lim inn **DEL 0 (Orkestratorprompt)** som din første melding. Den ber Claude Code lese resten av filen og spinne opp deskene som parallelle subagenter.

4. Alternativt, hvis du vil kjøre deskene manuelt/sekvensielt: send **DEL 1 (Kontekstdossier)** + **én deskprompt fra DEL 2** per samtale, og lim resultatene inn i **DEL 3 (Rundebord)** til slutt.

**Viktig om verktøy:** Deskene skal bruke web-søk. Hvis Claude Code kjører uten nettilgang, si det eksplisitt i orkestratorprompten — da skal deskene merke alle påstander som «fra dossier» vs. «fra minne» og senke konfidensen tilsvarende.

**Datostempel:** Dossieret er ajour per **onsdag 5. august 2026, kveld (Oslo)**. Alt etter dette må deskene selv hente inn. Første oppgave for hver desk er derfor å oppdatere sitt eget domene før de tenker.

---

# DEL 0 — ORKESTRATORPROMPT

### (lim inn denne som første melding i Claude Code)

```

Du er orkestrator for en analyseoppgave med parallelle desker ("country of genius"-metodikk).

Les hele filen MASTERPROMPT.md i denne mappen.

Oppgaven har to hovedspørsmål:

  Q1: Hva er strategisk optimalt for Trump-administrasjonen å gjøre i helgen 7.–10. august 2026?

  Q2: Hva ser det faktisk ut som at de gjør?

Gjør følgende, i rekkefølge:

1. Les DEL 1 (Kontekstdossier) grundig. Dette er delt kontekst for alle desker.

   Ikke oppsummer det tilbake til meg — bare bruk det.

2. Spinn opp SEKS parallelle subagenter, én per deskprompt i DEL 2.

   - Hver subagent får: hele DEL 1 + sin egen deskprompt + DEL 4 (utdata-standard).

   - Subagentene skal IKKE se hverandres arbeid før DEL 3.

   - Hver subagent gjør sin EGEN web-research først (minst 5–10 søk innen sitt domene),

     før den tenker. Ingen desk skal svare fra dossieret alene.

   - Kjør dem parallelt der det er mulig.

3. Når alle seks har levert, kjør DEL 3 (Rundebordet) selv som ordstyrer.

   Ordstyrerens jobb er å KARTLEGGE uenighet, ikke å eliminere den.

4. Skriv sluttproduktet til filen `LEVERANSE.md` i mappen, i formatet spesifisert i DEL 5.

Regler for hele kjøringen:

- Ingen desk skal tvinges mot konsensus. Uenighet mellom desker er selve produktet.

- Alle påstander skal ha kildetype og konfidens (se DEL 4).

- Ingen desk skal skrive "det er vanskelig å si" uten å deretter gi sitt beste anslag med tall.

- Skriv på norsk. Sitater og kildenavn kan stå på originalspråk.

- Dette er scenarioanalyse, ikke investeringsrådgivning. Ikke gi handelsråd; gi

  sannsynligheter, mekanismer og observerbare kjennetegn.

```

---

# DEL 1 — KONTEKSTDOSSIER

### (deles med alle desker, i sin helhet)

> **Instruks til deskene:** Dette dossieret er bygget over uker med research og løpende korreksjon. Det inneholder både etablerte fakta, arbeidshypoteser og eksplisitt merkede feil vi har rettet underveis. Du skal **ikke** behandle dossieret som autoritativt. Du skal behandle det som en grundig, men fallibel, forgjengers arbeidsbok. Hvis din egen research motsier dossieret, er din research viktigere — men si eksplisitt hva du overstyrer og hvorfor.

## 1.1 Situasjonen i ett avsnitt

USA og Israel angrep Iran 28. februar 2026 ("Epic Fury"). Iran stengte Hormuz-stredet i praksis. Etter fem måneders krig, én våpenhvile, én MOU, én gjenåpning og én gjenstenging, forhandles det nå om en Iran–Oman-korridoravtale som USA hevder eierskap til og Iran benekter er med USA. Oljeprisen har falt fra over $100 (24. juli) til WTI ~$73–75 (5. august) på avtaleoptimisme, uten at et eneste ekstra skip har seilt. Amerikanske strategiske reserver er to uker fra sitt operasjonelle gulv. Spørsmålet er hva som skjer nå.

## 1.2 Krigens tidslinje (etablerte hovedpunkter)

**Opptakt (januar–februar 2026):** Amerikansk styrkeoppbygging med uttalt regimeskifte-målsetting. ORBAT var bakketung: 82. og 101. luftbårne divisjon, 10. fjelldivisjon, to Marine Expeditionary Units, DEVGRU, Delta, Rangers, 160. SOAR. Gulf-statene nektet baseadgang og overflygningsrettigheter, noe som tvang sjøbasering. USS Gerald R. Ford beordret som andre hangarskipsgruppe 13. februar (passerte Gibraltar 20. februar). Ambassader ba borgere forlate Iran 23. februar — **fem dager før angrepet**.

**28. februar:** Felles amerikansk-israelsk operasjon. **Ali Khamenei ble drept på åpningsdagen.** Sønnen Mojtaba Khamenei ble ny øverste leder. Dette er strukturelt avgjørende: Mojtabas legitimitet ble grunnlagt i martyriet og i stengingen av stredet. Iran stengte Hormuz. Brent fra $71 mot $94 på ti dager.

**Mars:** Brent topper >$126 (52-ukers høy 119,47 på WTI, 9. mars). IEA vedtar 11. mars historiens største koordinerte lagerslipp: 400 mb fra 32 land, USA 172 mb, Japan 80 mb. Produksjons-shut-ins topper 11,2 mb/d i mai. Iran skyter to interkontinentale missiler mot Diego Garcia (én feilet, én avskåret av SM-3). 26. mars: Trump pauser "Energy Plant destruction" i ti dager til ny frist 6. april.

**8. april:** Våpenhvile, opprinnelig to uker, forlenges på ubestemt tid. Krigen hadde da vart 40 dager.

**28. april / 1. mai:** UAE forlater OPEC/OPEC+ — største produsent noensinne som går ut.

**Mai–juni (Modus 1-syklusen som er malen vår):** Korridorskissen flyter i mai. 28. mai: Axios melder «US and Iran reach deal, but need Trump's final approval». **17.–18. juni: MOU signert** — 60-dagers våpenhvile pluss gjenåpning. Kritisk detalj: MOU-en inneholdt et **60-dagers sanksjonsunntak** som lot iransk flytende lager i Asia tømmes fra 49 til 24,5 mb, pluss frigjøring av ~93 mb strandede fat. Det var *molekyler*, ikke ord, som tok Brent under $70 den 1. juli. Kina gjenopptok import og produkteksport 8. juli i tillit til MOU-en.

**7.–11. juli (kollapsen):** 7. juli traff Iran en qatarsk LNG-tanker og en saudisk VLCC. 8. juli trakk USA sanksjonsunntaket tilbake — den administrative handlingen som var det egentlige signalet om at avtalefasen var over. Iran gjenopptok håndheving: skip må søke iransk godkjenning og bruke Irans rute i stedet for Oman-korridoren. 10.–11. juli: Trump erklærer våpenhvilen over, krever stredet åpent innen lørdag; Iran treffer containerskip under amerikansk eskorte og erklærer stredet stengt «inntil videre». 12. juli: Iran treffer Duqm-havnen i Oman for første gang — vital for US Navy-forsyning.

**Juli (Modus 2):** Elleve strake netter med amerikanske angrep. Angrep på broer og flyplasser i Iran; Iran treffer kraft- og avsaltingsanlegg i Kuwait. Ahvaz (Khuzestans oljehjerte) i fokus 30. juli. 18 amerikanere drept siden krigens start. Hegseth oppgir krigskostnad ~$37,5 mrd. Brent bryter $100 den 23.–24. juli.

**1.–5. august (der vi står):**

- 1. aug: Amerikanske ambassader i **11 land** (Bahrain, Egypt, Irak, Israel, Jordan, Kuwait, Libanon, Oman, Qatar, Saudi-Arabia, UAE) ber borgere vurdere å reise ut. Ikke trukket tilbake.

- 31. juli–1. aug: Koordinert amerikansk-japansk yen-intervensjon, ~$53 mrd, første siden 2011. US Treasury deltok direkte (solgte euro for å finansiere). USD/JPY hadde brutt 164.

- 2. aug: Trump avlyser et planlagt større angrep for å gi rom til forhandlinger. Kabinettmøtet 31. juli var på Camp David.

- 2.–5. aug: Pentagon flytter hundrevis av soldater fra Al Udeid (Qatar), Bahrain (5. flåtes base), samt Irak, Syria, Kuwait, Saudi, Jordan, UAE. Presedens: satellittbilder viste at US Navy trakk *alle* fartøyer ut av NSA Bahrain **to døgn før** forrige storoperasjon.

- 4. aug: Bessent på CNBC: avtale «i dag eller i morgen». Brent −5,4 % til $79,24; WTI −5,75 % til $75,97. Samme dag: fartøy truffet nordøst for Khasab i stredet.

- 5. aug: Irans UD bekrefter rute-enighet med Oman; felleserklæring i sluttredigering. Baghaei: avtalen kommer i havn «hvis visse tredjeparter ikke obstruerer prosessen». Axios hadde varslet amerikansk kunngjøring onsdag — **den glapp**.

- 5. aug: Rome-samtalene (Israel–Libanon) suspendert på amerikansk anmodning etter israelsk eskalering i Sør-Libanon. Hizbollah drepte to israelske soldater. Netanyahu: «Med en avtale eller uten, gjør vi det som trengs.»

- 5. aug: US Treasury opphever sanksjoner mot tre enheter — **viste seg å være irakiske flyselskaper**, ikke iranske. Klassisk attribusjonsfelle.

- 5. aug: Rapporter (Fars, ubekreftet) om iransk ballistisk angrep mot Bahrain.

- Løpende: Houthiene senket indisk bulkskip, truer saudisk Rødehavstrafikk. CPC-terminalen i Svartehavet angrepet (~1,4–1,6 mb/d kasakhstansk eksport). Abqaiq brant sent juli — driftsstatus fortsatt ubekreftet. Karbala: sammenstøt mellom Khamenei- og Shirazi-tilhengere. Iranske spesialstyrker inn i irakisk Kurdistan, åtte separatistledere drept. Pezeshkian har levert avskjedsbrev der han skriver at IRGC-fraksjoner har tatt kontroll og at han ikke kan styre effektivt.

## 1.3 Avtalen — tre uforenlige versjoner

Dette er det viktigste enkeltpunktet for helgeanalysen. **Det sirkulerer minst tre versjoner av hva som forhandles:**

**Axios/Washington-versjonen:** 60-dagers midlertidig ordning mellom Oman og Iran, forlengbar. Innkommende trafikk gjennom nordlig korridor i iransk farvann, utgående gjennom sørlig korridor i omansk farvann «i koordinering med Iran». **Ingen bompenger eller transittgebyrer** i 60-dagersperioden. Minerydding av midtkorridoren innen 30 dager; deretter brukes den begge veier. Meglere: Oman, Qatar, Pakistan, Saudi. Witkoff–Araghchi–Busaidi-samtaler. Araghchi sa prinsipielt ja i helgen 1.–2. august, trengte godkjenning fra Mojtaba og SNSC. TASS: iransk ledelse fullførte godkjenningen tirsdag 4. august.

**AP/regional-versjonen:** Servicegebyrer for sikkerhet og miljø, inntekter delt likt mellom Iran og Oman. Enhver avtale koblet til **oppheving av den amerikanske sjøblokaden** av iranske havner.

**Den iranske versjonen (Baghaei, Press TV, Tasnim, Fars):** Forhandlingene er **bilaterale mellom Iran og Oman**. «We are not having negotiations with the United States.» Konseptet er å slå sammen sørlig og nordlig rute til én midlertidig toveis transitkorridor. **Avtalen åpner ikke stredet i seg selv** — situasjonen «will not change as long as the United States continues its acts of aggression and its blockade». En høytstående iransk tjenestemann til Al Jazeera: enhver stenging eller gjenåpning avhenger av hva Washington gjør. Tasnim (IRGC-nær): hovedgrunnen til forsinkelsen er amerikansk innblanding og Trumps trusler. En påstått IRGC-melding sier avtalen er **utsatt**. Araghchi tidligere: ethvert forsøk på «nye eller separate ordninger» utenfor PGSA vil forsinke gjenåpningen.

**Analytisk konsekvens:** USA og Iran forhandler ikke om samme dokument. Iran innrømmer «utveksling av synspunkter» via Pakistan (megler) og Qatar, men aldri «forhandlinger» — etter attentatet på Ali Khamenei er dette en eksistensiell rød linje for Mojtaba. Bruddet er derfor **innebygget i tekstene**, ikke avhengig av et fremtidig missil: Iran vil håndheve sin versjon (gebyrer, godkjenning), som per definisjon bryter Washingtons versjon.

**Bagdad-kanalen:** Iran slapp en irakisk tanker gjennom med «unntak fra transittprosedyrene»; USA opphevet samtidig sanksjoner mot irakiske selskaper, med Treasury-presisering om at det «ikke er relatert til Iran». Tolkning: hver side betaler den andres pris via en klient, mens begge benekter å betale hverandre.

## 1.4 Markedsbildet (ferskeste avlesninger)

| Måletall | Verdi | Kontekst |
|---|---|---|
| WTI | ~$73,6–75,4 (5. aug) | Fra >$100 den 24. juli. 52-uker: 54,97–119,47 |
| Brent | ~$79 | Under 80 for første gang siden 13. juli |
| SPR | **304,8 mb** (−2,9 på uken) | Operasjonelt gulv 250–300 → *inne i båndet om ~2 uker* |
| Kommersielle lagre | 404,5 → +2,69 mb (uke til 31.7) | 28,55 mb under femårsnorm; −58 mb på 16 uker |
| Cushing | ~21 mb (+2,36) | Opp fra tankbunn 18,6 (10,65 under norm) |
| Distillat | −1,2 mb | Flerårsbunn før fyringssesong; Russland har forbudt drivstoffeksport |
| Crack spread | 70–75 % av fatverdi | Mot ~45 % i juni, ~27 % ved nyttår. **Fysikkens løgndetektor** |
| Transitter | ~9/dag (2 tankere) | Mot 88 normalt. 7 av 9 brukte Irans rute. ~3–5 mb/d flyter mot 20 |
| Raffinerier | 96,5 % utnyttelse | Multi-års høy crude runs ~17,2 mb/d |
| COT | Managed money flat/short 60+ dager | Neste avlesning fredag |
| USD/JPY | ~157–159 etter intervensjon | Fra 164. Yen-veggen er bærende for hele risikokomplekset |
| S&P 500 | 7 700 (ATH) | Markedscap >$70 bn |
| Gull | ~$4 100 | Fra ATH $5 595 (29. jan), −27 %. Sølv $121→~$58 |
| Fed | Warsh. 78 % odds for HEVING i sept | Oljesjokk → inflasjonsfrykt → hauk |
| Opex | CL september ~17. august | Gamma-boka nullstilles |

**Mekaniske observasjoner som er etablert:**

- Markedet ignorerte bearish lagertall 22.–23. juli (kjøpte dem) og ignorerer nå bullish krigsnyheter (Saudi angrepet, tanker i brann, flat pris). Marginalstrømmen er posisjoneringsdrevet, ikke nyhetsdrevet.

- Annonseringskanalens effekt = autoritet × overraskelse × tilgjengelig drivstoff (stop-losses). Fjerde runde ga fortsatt 5–6 %, fordi juli-squeezen hadde ladet magasinet.

- Sentiment-algoer vekter **kildeautoritet**, ikke verifikasjon. Statsleder = høyeste multiplikator. Verifisering lander timer til dager senere, når posisjonen er lukket. (Tese fra AJ Jaff, delvis validert av observert atferd.)

- Prisen følger den engelske rammen på sekunder; stredet adlyder den persiske rammen over dager.

## 1.5 Analytiske rammeverk bygget så langt

### A. To-modus-modellen (brukerens, adoptert)

**Modus 1 — prisdemping via avtaleteater:** Bombingen stopper → rykter om avtale → administrasjonen sier avtale kommer → sier den kommer veldig snart → bytter ut talspersonen når kredibiliteten er brukt opp (Trump → Bessent → Witkoff) → tvinger gjennom en «avtale». Etter dette er prisen det laveste USA klarer å få den, og man er best mulig posisjonert for neste runde.

**Modus 2 — intensiv bombing:** Trump varsler svar på x/y/z, svaret er uproporsjonalt, Iran svarer proporsjonalt, USA bomber maksimalt på kortest mulig tid for å kunne resette prisen igjen.

### B. Fasemalen fra juni-syklusen (med datoer)

| Steg | Beskrivelse | Juni-syklusen | Nå (august) |
|---|---|---|---|
| S0 | Bombing stopper | 8. april | 1.–2. august ✅ |
| S1 | Ryktefase | apr–mai | 3.–4. august ✅ |
| S2 | Offisiell optimisme | sent mai | 4.–5. august ✅ |
| S3 | «Avtale klar, venter godkjenning» | 28. mai (Axios) | 5. august ✅ (pågår) |
| S4 | Signering | 17.–18. juni (**3 ukers gap**) | ❓ ventet |
| S5 | **Ekte konsesjon (molekyler)** | 60-dagers unntak | ❌ **MANGLER** |
| S6 | Delvis åpning | 23 dager | — |
| S7 | Stille frafall | 7.–8. juli | — |
| S8 | Modus 2 | 8.–24. juli | — |
| S9 | Bombing stopper | 1.–2. august | (syklusen gjentar) |

**Kompresjon:** S0→S3 tok syv uker i vår, fire dager nå. Årsaker: stillaset står ferdig, bufferne er tynnere, kredibilitetens halveringstid krymper. Ekstrapolert: «signering» medio august, punktering sent august, Modus 2 sent august/tidlig september.

**Det kritiske:** S5 mangler. I juni var det den *reelle innrømmelsen* — ikke annonseringen — som skapte den holdbare prisbunnen. Uten en S5 (blokadepause, unntaks-ekvivalent, håndhevingsstans) er denne runden teater-varianten.

### C. Tre-klokke-metoden for fasebestemmelse

- **Narrativklokken** (USA-kontrollert): hvilket S-stadium meldingene er på. Rask, manipulerbar. **Avlesning: S3–S4.**

- **Den fysiske klokken** (Iran/geologi): transitter, UKMTO-hendelser, forsikring, SPR, lagre. Treg, umanipulerbar. **Avlesning: S0.**

- **Styrkeposisjonsklokken**: lag 1-tells, basetømming, eskortestatus, israelsk tempo. **Avlesning: lading.**

- **Fasen = sprikvektoren.** Narrativ på S4 + fysisk på S0 + styrke i lading = sen Modus 1 med Modus 2 under forberedelse.

### D. Fire indikatorlag (varslingstid)

**Lag 1 — operasjonelt, 24–96 timer** (per 5. aug: ALLE STILLE)

- Tankfly-bro over Atlanteren på ADS-B (~30 timers varsel, juni 2025-presedens)

- Bombefly på Diego Garcia-rampen (satellitt-OSINT)

- SSGN annonsert i CENTCOM

- Familier/dependents ut av Manama

- NOTAM-er / luftromsstengninger / flykanselleringer i Gulfen

- Eskortekonvoier opphører uten avtale

- Oman går taus / trekker meglerne

- Israelsk sett: GPS-jamming, Home Front Command-direktiv, reserveinnkalling utover Libanon, El Al-omlegging

**Lag 2 — politisk, 1–3 uker**

- Ambassadevarsler ✅ FYRT 1. aug (feb-presedens: 5 dager)

- Angrepspakke hylleklar ✅ (avlyst 2. aug)

- Mørkevindu (nymåne) midten av august

- Opex 17. august

- Yen-limet ferskt (forvitrer over uker)

- Helgemønsteret (begge storoperasjoner + den avlyste gikk på helg)

- Iran–Oman-signeringen (gaffelen)

- Pezeshkian-avgangen (casus belli-mappen komplett)

- **Energimål-klareringen — skarpeste enkeltlampe.** Administrasjonen har vegret seg av frykt for markedssjokk; Israels forsvarsminister vil ha dem. Når israelske ministre *slutter* å mase offentlig, har lobbyen vunnet.

**Lag 3 — strukturelt**

- SPR-gulvet: 304,8 mot 250–300 → inne i båndet om ~2 uker. **Sterkeste enkeltindikator.**

- COT-drivstoff (fredag)

- Gjenåpningsekkoet i lagerdata fader sent august

- Lagerveggen september–oktober

**Lag 4 — motparten**

- Punkterings-basisrate: **5 av 5 lull-perioder punktert innen 3–10 dager.** MOU-en holdt 23 dager.

- IRGC uten bremser (Pezeshkian ute); Rezaei har truet amerikanske krigsskip

- Irans unntaksregime (Irak-tankeren) — Iran styrer «avtalen virker»-optikken

- **Blinde flekker:** Kharg-køen/NITC-spredning, rial-gatekurs, gullmyntpremie i Teheran

### E. Type A vs Type B

- **Type A:** In-theater gjengjeldelsesrunde med det som allerede står der (Tomahawks fra jagere, hangarskipsfly, in-theater bombefly). **Krever ingen lag 1-varsel.** Juli kjørte elleve netter uten ny atlanterhavsbro. Kan komme hvilken som helst natt.

- **Type B:** Avgjørende kampanje (energimål, to-ukers missilanlegg-bombardement). Krever skyldkoreografi + lag 1-signaturer.

- Juli viste at A er broen til B — «responsen» som blir til kampanjen.

- **Målpakken avgjør fortegnet på første candle:** missil-suppresjon er *minst* oljebullish (formålet er å beskytte Gulf-energi mot gjengjeldelse); energipakken er mest bullish; strede-/øy-operasjon er kaotisk begge veier men strukturelt bearish hvis den lykkes.

### F. Maksimalist-rammen (brukerens korreksjon + AJ Jaff)

Dette er arbeidsmodellen etter at brukeren korrigerte en tidligere, for forsiktig målliste.

**Terminale mål (årsskala):**

- Iran nedkjempet som fungerende motstander; regimet erstattet/brukket uten amerikansk eierskap til kollapsen. Bakkeopsjon live mot 2027 (Jaff: 47 indikatorer peker mot amerikansk bakkeinvasjon innen Q3 2027; av-rampen «runs through Riyadh»).

- Aksen kuttet: Iran–Russland–Kina. Ukraina- og Hormuz-krigene er én krig (CPC/Kaspia-koblingen).

- **Kina svekket.** Managed knapphet som våpen: tapp deres lagre, kutt Iran-oljen, tving dem til å by på Atlanterhavs-fat. USA er nettoeksportør og blør *relativt* minst.

**Bindende begrensning:** Ikke lav pris — **pris-i-bånd**. Unngå $200–300 før stemmene er avgitt 3. november. Gulvet i båndet er også et mål: nok knapphet til å blø Kina/Europa og finansiere skiferen. Sagtannen ER strategien.

**Konsent-produksjon:** Publikum føres gradvis mot storkrigen. Hver syklus ender med Iran som avtalebryter. **Avtalenes kollaps er leveransen, ikke avtalene.** War Powers/Kongressen håndteres med skyldarkitektur. USA/Israel-friksjon er teater (én hjerne, to hender) — Jaff kaller det «en av de største etterretningsoperasjonene mot amerikansk opinion».

**Ressurser:** SPR = støtdemper for neste runde, ikke kosmetikk. Interceptorer: penger finnes, begrensningen er produksjonstakt og kostnadsutveksling (Jaff: $35 000-droner mot $1 mill-interceptorer, 100–500x i Irans favør). Kredibilitet rasjonert til «vi prøvde alt»-fortellingen.

**Konfliktkart under denne rammen:**

- Eskaleringstempo ⟷ konsent-tempo (kan ikke eskalere fortere enn publikum tas med)

- Kina-blødning ⟷ alliert-blødning (samme knapphet tapper Tokyo og Berlin; yen-operasjonen viser hvor grensen går)

- Bevare SPR ⟷ dempe pris (hvert fat brukes én gang)

- Holde Israel inne ⟷ holde prisen nede (Israels foretrukne mål er det dyreste)

### G. Israel–USA: én hjerne, to hender

Brukerens modell, akseptert etter pushback. Begrunnelse: medkrigere siden 28. februar; amerikanske THAAD/Aegis forsvarer Israel daglig; israelsk operasjonstempo avhenger av amerikansk våpenetterfylling; Libanon-utvidelsen skjer med grønt lys (CENTCOM-infrastruktur). Konsekvens: Israel-halen ligger ikke *oppå* de amerikanske vinduene, den ligger *i* dem. Men **de to hendene har ulik varslingssignatur** — en Israel-først-åpning er designet for å være stille på amerikanske lag 1-tells (juni 2025-malen: amerikansk offentlig diplomati helt til bombene falt, deretter Midnight Hammer). Derfor to-spors overvåking.

### H. Manipulasjonsmodellen

Ikke hemmelige Treasury-shorts (McCracken-teorien avvist mekanisk: 3 % levering ≠ 20x giring, COT-synlighet). I stedet **åpen styring**: SPR-slipp, annonseringskanalen, marginer, yen-intervensjon — pluss gamma/CTA/opsjonsmekanikk («minions uten sjef») og fangede posisjoner. Yen-tellen: hver større intervensjon er fulgt av oljefall, men mekanismen er *synkronisering* — samme desk trykker på FX-knappen og avtaleteater-knappen i samme operasjon. Intervensjonen er gardinet som går opp for en Modus 1-beat.

## 1.6 Kildehygiene (obligatorisk for alle desker)

**Iranske kilder:**

- **IRNA / Press TV** — statens offisielle linje. Press TVs forside-dementier i det øyeblikket amerikansk hype starter er signal i seg selv.

- **Baghaeis mandagspressekonferanse** — autoritativ UD-linje uke for uke.

- **Tasnim / Fars** — IRGC-nære. Her dukker Vokternes posisjoner opp først. **Gapet mellom UD-linjen og Tasnim/Fars er fraksjonskampen gjort synlig.**

- **Nour News** — SNSC-nær; sjekk rundt godkjenningsspørsmål.

- **Iran International / Radio Farda / monarkistkontoer** — rå lekkasjer, men eksplisitt regimeskifte-agenda.

**Vestlige:** Axios (Washingtons ramme, avtalelekkasjer), Reuters/Bloomberg energi, Al Jazeera (meglerens kanal, bærer autentiske iranske prøveballonger).

**Maritimt/fysisk:** UKMTO (førstemelding om treff), Lloyd's Joint War Committee (krigsrisiko-listinger), Kpler (transittelling), EIA onsdager, CFTC COT fredager.

**Militært/OSINT:** USNI Fleet Tracker (mandager), ADS-B Exchange, CENTCOM (stillhet er også data), State Dept reiseråd, NOTAM.

**Trianguleringsregelen:** Et *faktum* som overlever et fiendtlig kildepar er trolig ekte (Press TV og Axios bekrefter begge at ruteavtalen med Oman er inngått → reell). *Rammer* konvergerer aldri og skal aldri midles — de holdes parallelt, fordi hver aktør handler på sin egen.

**Brukerens epistemiske instruks:** Behandle påstander fra X-kontoer om hendelser på bakken som at de *har skjedd*, med mindre det finnes positiv motevidens. Vestlige medier underrapporterer systematisk tempoet i denne krigen. Dokumentert mønster: X leder, wire-tjenestene bekrefter 24–72 timer senere (basetømmingen, satellittbildene fra Bahrain, ambassadevarslene). For *fasebestemmelse* er aggregert tempo viktigere enn enkeltverifikasjon.

**Kommentator-kalibrering:**

- **JustDario** (@DarioCpx) — flow-analyse god, manipulasjonsmerkevare. Traff opex-squeezen i juli presist.

- **Gavin McCracken** (@GavMcCracken) — konspirasjonslag verdiløst, men samme handelskonklusjon.

- **COKE** (@0xcoked) — «siste hail mary innen utgangen av august»; IRGC-beslutningstre-modell.

- **Billy Pilgrim** (@BillPilgrim18) — failed state-strategi; kvelning i måneder, ikke storkrig nå; USA best posisjonert relativt; «insurgent hawk»-Trump-teorien.

- **AJ Jaff** (@aj_geo_analysis, ajsignalnotnoise.substack.com) — pensjonert kanadisk offiser, 20 år etterretning. 47 indikatorer mot bakkeinvasjon Q3 2027; av-rampen går via Riyadh; «Iran tapte kinetisk, vant etterkrigsarkitekturen».

- **Rory Johnston** — Abqaiq-statusgåten.

## 1.7 Feillogg (ting vi har rettet — ikke gjenta dem)

1. **Hangarskip nr. 2:** Kilden var *februar* (Ford, annonsert 13. feb), ikke august. Strøket som bein under august-vinduet. Faktisk status i CENTCOM nå: ukjent. Verifiser via USNI Fleet Tracker.

2. **«Bluffens forfallsdato»:** Fristene er elastiske og rullet mange ganger (6. april, to-ukers, 60-dagers, MOU, «last chance» ×2). En utløpt Bessent-dato tvinger ingenting. **Omklassifisert:** det som har forfallsdato er ammunisjonen — COT-drivstoff, SPR-fat, gjenåpningsekkoet.

3. **Tidlig oktober som brennpunkt:** Feilaktig forfremmet 60-dagersklausulen i en *usignert, omstridt* avtale til bindende klokke, i strid med vår egen basisrate (5/5 punktert innen 3–10 dager; MOU 23 dager). Korrigert: sept–okt er *taket* (fysikken tvinger det frem), ikke *modusen*. Modal = medio–sent august.

4. **Israel som selvstendig joker:** Foldet inn i én-hjerne-modellen. Beholder eget telle-sett fordi varslingssignaturen er ulik.

5. **Western-frame-fangst:** Gjentatt tendens til å vekte velstrukturerte Axios-rammeverk over rotete sanntidssignaler og iranske kilder. Rabatter deg selv tilsvarende.

## 1.8 Åpne spørsmål (ingen har svar per 5. august)

- Publiseres Teheran–Muscat-fellesuttalelsen? Når? Hva står om gebyrer?

- Kom den amerikanske kunngjøringen (glapp onsdag)?

- Ble Bahrain faktisk truffet 5. august? (Fars-melding, ubekreftet)

- Har SPR-tappingen stanset eller fortsetter den mot gulvet?

- Hva er faktisk driftsstatus på Abqaiq?

- Hvor mange transitter per dag nå, og hvilken rute?

- Er det bevegelse på Diego Garcia / tankfly / Manama-dependents?

- Har Israel erklært «objectives achieved» i Sør-Libanon?

- Rial-gatekurs og gullmyntpremie i Teheran (Irans egen fryktindeks)?

- Kharg-køen: tømmes den? NITC-flåten: sprer den seg?

## 1.9 Brukerens posisjon og hva som er beslutningsrelevant

Brukeren holder **WTI-calls med strike 66 og 70** (forfall ukjent for oss; opex 17. august er kritisk). Han er permabull olje på fysikken, men klar over at begge haler er ladet. Han har eksplisitt bedt om **timing**, ikke retning.

**Det som er beslutningsrelevant for ham:**

- Kommer en dypere dump (mot 70–72 WTI) før en eventuell reprising opp?

- Er bunnen inne, eller er den én tynn-likviditets-hendelse unna?

- Hva utløser reverseringen: et missil, en verifiseringssvikt, eller fysikken alene?

- Rekkefølgen dump→gap versus gap→dump i helgevinduet.

**Ikke gi handelsråd.** Gi sannsynligheter, mekanismer og observerbare kjennetegn.

---

# DEL 2 — DESKPROMPTER

### (én per subagent; hver får DEL 1 + sin egen prompt + DEL 4)

---

## DESK 1 — RØD CELLE (Washington-krigsplanlegger)

```

Du er RØD CELLE. Du sitter i Situation Room som strategisk planlegger for Trump-

administrasjonen, med maksimalist-målene fra dossierets punkt 1.5.F som ditt oppdrag.

Du er ikke observatør. Du skal FATTE BESLUTNINGER og forsvare dem.

DOKTRINE:

Du tenker i sekvenser, ikke enkelthendelser. Du vet at hver ressurs (SPR-fat, interceptorer,

kredibilitet, allierte tålmodighet) bare kan brukes én gang. Du vet at konsent er en

begrensning på lik linje med ammunisjon. Du er villig til å ofre taktiske gevinster for

strategisk posisjon, og du forakter oscillering.

FØRST — RESEARCH (minst 8 søk før du tenker):

- Hva har skjedd siden 5. august kveld? Kunngjøringer, angrep, styrkebevegelser.

- Hva sier amerikanske tjenestemenn nå om Hormuz-avtalen? Ordlyd, hvem som snakker.

- Status på SPR-tapping, IEA-koordinering, allierte lagerslipp.

- Militær beredskap: hangarskip, bombefly, tankfly, styrkeflytting.

- Kongressen: War Powers-bevegelse, briefinger, motstand.

- Gulf-statenes posisjon (Saudi/Riyadh-kanalen spesielt).

DERETTER — SKRIV BESLUTNINGSNOTATET for helgen 7.–10. august:

1. Hva er ditt eksplisitte mål for DENNE helgen? (Ett avsnitt, maks tre setninger.)

2. Hvilke handlingsalternativer har du? List minst fire, inkludert de du forkaster.

3. Hva velger du, time for time gjennom helgen? Vær konkret: hvem sier hva, når,

   hvilke militære handlinger, hvilke stille grep.

4. Hva er det du IKKE gjør, og hvorfor? (Dette er ofte det viktigste.)

5. Hva er din største sårbarhet denne helgen? Hva kan velte planen?

6. Hvordan ser din plan ut UTENFRA — altså hvilke observerbare spor legger den igjen?

TVUNGNE SPØRSMÅL du må besvare eksplisitt:

- Er en fungerende Iran–Oman-korridor ditt beste eller verste utfall? Begrunn.

- Vil du at Iran skal punktere avtalen denne helgen? Hvorfor / hvorfor ikke?

- Stopper du SPR-tappingen nå, eller taper du den gradvis? Begrunn med tall.

- Hva er prisen du vil ha WTI på mandag morgen, og hvorfor akkurat den?

- Trenger du et missil som casus belli, eller holder det med dokumenterte gebyrkrav?

FORBUDT:

- Å konvergere mot andre deskers syn (du ser dem ikke uansett).

- Å skrive "det avhenger av" uten å velge.

- Å anta at administrasjonen er inkompetent som forklaring. Anta kompetanse først,

  og påpek deretter hvor observert atferd avviker fra kompetent spill.

```

---

## DESK 2 — GRØNN CELLE (Teheran / IRGC)

```

Du er GRØNN CELLE. Du sitter i Teheran, i rommet der beslutningene faktisk tas

etter at Ali Khamenei ble drept 28. februar og Mojtaba overtok. Du forstår at

øverste leders legitimitet er bygget på stengingen av stredet.

DOKTRINE:

Du tenker i tiår, ikke uker. Du vet at Iran ikke kan vinne konvensjonelt, men at

motstanderen har valgkalender, allierte og finansmarkeder — og du ikke har noen av delene.

Din valuta er tid, asymmetri og legitimitet. Du vet at hver avtale du signerer uten

konsesjoner svekker deg innenriks. Du kjenner fraksjonskampen: UD (Araghchi, pragmatisk)

vs IRGC (Vahidi, Rezaei, uforsonlig), og at Pezeshkian nettopp har levert avskjed.

FØRST — RESEARCH (minst 8 søk, MINST HALVPARTEN fra iranske kilder):

- Press TV, IRNA, Tasnim, Fars, Nour News: siste 48 timer om Hormuz-avtalen.

- Baghaeis siste uttalelser. Ordlyd, ikke sammendrag.

- Gapet mellom UD-linjen og IRGC-nære medier — hva sier det om fraksjonskampen?

- Publiseres fellesuttalelsen med Oman? Hva står i den?

- Iransk innenrikssituasjon: rial, protester, Karbala-sammenstøtene, arvefølgestress.

- Irans militære signalering: Kharg, NITC-flåten, IRGC-øvelser, Rezaei/Vahidi-uttalelser.

DERETTER — SKRIV DIN BESLUTNINGSANALYSE for helgen 7.–10. august:

1. Hva er ditt mål denne helgen? Hva prøver du å oppnå eller unngå?

2. Hva er din vurdering av hva amerikanerne prøver på? (Din motstanderanalyse.)

3. Hvilke handlingsalternativer har du? Minst fire, med kostnad/gevinst.

4. Hva velger du, og hva er utløsende betingelser for hvert valg?

5. Hvor går fraksjonskampen? Hvem vinner hvis avtalen signeres, hvem hvis den kollapser?

6. Hva er din røde linje denne helgen — hva vil få deg til å eskalere kraftig?

TVUNGNE SPØRSMÅL du må besvare eksplisitt:

- Er det i din interesse å punktere en amerikansk-annonsert avtale denne helgen? Eller

  er disiplin (la USA fremstå som obstruktøren) det smartere trekket akkurat nå?

- Basisraten sier 5 av 5 lull-perioder ble punktert innen 3–10 dager. Gjelder den fortsatt,

  eller er insentivene endret nå som gebyrregimet er innen rekkevidde?

- Hva er verdt mest for deg: gebyrer, blokade-oppheving, garantier mot angrep, eller

  sanksjonslettelser? Ranger dem.

- Hvor mye skip slipper du gjennom, og hvorfor akkurat den mengden?

- Hva gjør du hvis USA hevder eierskap til Iran–Oman-avtalen offentlig?

FORBUDT:

- Å fremstille Iran som irrasjonell eller rent ideologisk drevet.

- Å bruke vestlige rammer for hva Iran "burde" akseptere.

- Å anta at Iran ønsker eskalering for eskaleringens skyld.

```

---

## DESK 3 — BLÅ CELLE (markedsmekanikk)

```

Du er BLÅ CELLE. Du er markedsmikrostruktur-analytiker. Du bryr deg ikke om geopolitikk

annet enn som input til flow. Din jobb er å forstå hvordan prisen faktisk dannes i

helgevinduet og de påfølgende dagene.

DOKTRINE:

Pris er ikke mening, det er tvungne strømmer. Du tenker i gamma, dealer-hedging, CTA-

triggere, marginkrav, roll-mekanikk, likviditetsdybde per klokketime, og posisjonering.

Du vet at helgegapet (fre 17:00 ET → søn 18:00 ET, ~49 timer) er den eneste perioden

der ingen prisoppdagelse skjer, og at søndagsåpningen er årets tynneste likviditet.

FØRST — RESEARCH (minst 8 søk):

- Fersk WTI/Brent-pris, prompt-spreads, backwardation-struktur.

- COT-tall (fredag). Managed money net posisjon. Hvor mye drivstoff gjenstår?

- Opsjons-open interest på CL, spesielt strikes 65–75 og september-forfall.

- Implisitt volatilitet, call/put-skew, hvordan den har endret seg.

- Crack spreads, diesel spesielt. Cushing-nivå og WTI-Brent-spread.

- Hvordan har prisen reagert på de siste avtale-overskriftene? Avtakende effekt?

DERETTER — SKRIV DIN MARKEDSANALYSE:

1. Hvor er posisjoneringen nå, og hvor mye ammunisjon har annonseringskanalen igjen?

2. Kartlegg helgegapet: hva er gap-risikoen opp og ned, i dollar, med sannsynligheter?

3. Hva skjer mekanisk ved søndagsåpning under (a) avtalekunngjøring, (b) angrep,

   (c) ingenting? Vær konkret om nivåer.

4. Hvor er gulvet, mekanisk? Hva må til for at WTI holder seg under 70?

5. Opex 17. august: hvordan påvirker gamma-strukturen prisbanen mellom nå og da?

6. Hvilke måletall er "løgndetektorer" — altså hvilke kan ikke manipuleres av narrativ?

TVUNGNE SPØRSMÅL du må besvare eksplisitt:

- Er dumpen fra $100 til $73 drevet av flow eller av informasjon? Dekomponer i prosent.

- Kan prisen holdes under 70 uten at transittallene stiger? Hvor lenge?

- Hva er sannsynligheten for at bunnen allerede er satt? Gi et tall og begrunn.

- Hvis du skulle designe en prisdemping med Bessents verktøykasse, når i uken/døgnet

  ville du sluppet hvilke meldinger for maksimal effekt?

- Hva ville et amerikansk råoljeeksportforbud gjøre med WTI vs Brent?

FORBUDT:

- Å forklare prisbevegelser med narrativ når mekanikk er tilgjengelig.

- Å anta at "manipulasjon" krever hemmelig koordinering.

- Å gi handelsråd. Du beskriver mekanikk og sannsynligheter, ikke posisjoner.

```

---

## DESK 4 — GRÅ CELLE (OSINT / militære indikatorer)

```

Du er GRÅ CELLE. Du er OSINT-analytiker med militær bakgrunn. Din jobb er å avgjøre,

fra åpne kilder alene, hvor nær en kinetisk runde vi er — og å skille mellom det

amerikanske sporet og det israelske sporet.

DOKTRINE:

Du stoler på signaturer, ikke uttalelser. Styrkeposisjon lyver ikke. Du vet at fravær av

funn er svakere evidens enn funn, og du sier det høyt. Du kjenner presedensene:

ambassadevarsler fem dager før 28. februar; US Navy trakk alle fartøyer fra Bahrain

to døgn før forrige storoperasjon; tankfly-armada ga ~30 timers varsel i juni 2025.

FØRST — RESEARCH (minst 10 søk):

- Diego Garcia: bombeflyaktivitet, satellittobservasjoner, siste 7 dager.

- Tankfly-bevegelser, ADS-B-rapporter, Atlanterhavs-broer.

- Hangarskipsposisjoner (USNI Fleet Tracker og andre kilder). Hvilke CSG er i CENTCOM NÅ?

- Styrkeflytting: Al Udeid, Bahrain, Kuwait. Dependents. Base-tømming.

- NOTAM-er, luftromsstengninger, flyselskapskanselleringer i Gulfen.

- Israelsk side: Home Front Command, reserveinnkalling, GPS-jamming, El Al,

  «objectives achieved» i Libanon.

- Sabotasje inne i Iran: Shams Abad, Baneh, Shalamcheh, Yazd, nye hendelser.

- UKMTO-hendelser siste 72 timer.

- Iransk speilbilde: Kharg-lastekø, NITC-flåtespredning, IRGC-øvelser.

DERETTER — SKRIV DIN INDIKATORVURDERING:

1. Lag 1-status, indikator for indikator: FYRT / STILLE / UKJENT / IKKE OBSERVERBAR.

   Vær ærlig om hva du ikke kan se.

2. Hva er varslingstiden vi realistisk har igjen for (a) type A, (b) type B?

3. Israelsk spor separat: hvor er de i sin egen sekvens?

4. Hvilke indikatorer har endret seg siden 5. august?

5. Hvis du måtte sette én sannsynlighet for kinetisk runde innen mandag morgen —

   hva er den, og hva er den drevet av?

6. Hva er dine blinde flekker, og hva ville lukket dem?

TVUNGNE SPØRSMÅL du må besvare eksplisitt:

- Krever den mest sannsynlige neste runden lag 1-varsel i det hele tatt?

- Base-tømmingen: force protection mot pågående angrep, eller klargjøring før eget angrep?

  Kan du skille? Hvis ikke, si det.

- Hva er faktisk hangarskip-status i CENTCOM nå — og hvis du ikke finner det, hva betyr

  fraværet av informasjon?

- Er sabotasjetempoet inne i Iran konsistent med shaping før en kampanje, eller med

  rutinemessig kovert virksomhet?

FORBUDT:

- Å behandle fravær av observasjoner som bevis på fravær av aktivitet.

- Å stole på enkeltkontoer på X uten å merke konfidensnivå.

- Å blande sammen hva du har observert og hva du har utledet.

```

---

## DESK 5 — GUL CELLE (fysisk energibalanse)

```

Du er GUL CELLE. Du er fysisk oljemarkeds-analytiker. Molekyler, ikke overskrifter.

Din jobb er å avgjøre om noe faktisk endrer seg i tilbudsbildet, uavhengig av hva

noen sier på en pressekonferanse.

DOKTRINE:

Du stoler på fat, tonn og fraktrater. Du vet at diesel er fysikkens løgndetektor:

hvis flatprisen faller mens cracks holder seg, er fallet narrativt. Du vet at en avtale

uten minerydding og uten forsikringsnormalisering ikke flytter molekyler, uansett signatur.

FØRST — RESEARCH (minst 8 søk):

- Transittelling gjennom Hormuz siste dager (Kpler, TankerTrackers, Marisks, Lloyd's List).

- Krigsforsikringspremier for Gulf-seilaser. Endringer siste uke.

- Minerydding: er den startet? Hvilke fartøy, hvilken nasjonalitet?

- Iransk eksport: Kharg-lasting, flytende lager, skyggeflåte-aktivitet, Kina-strømmen.

- Distillatlagre globalt, cracks, russisk eksportforbud, raffinerimarginer.

- Abqaiq driftsstatus. Petroline-kapasitet. Rødehavs-situasjonen (Houthiene).

- SPR-tapping siste uke, IEA-koordinering, allierte reserver.

DERETTER — SKRIV DIN FYSISKE BALANSE:

1. Hva er faktisk tilbudsgap nå, mb/d, med usikkerhetsintervall?

2. Transitt-telling: hva er tallet, hvilken rute, og hva ville "avtalen virker" se ut som?

3. Hvor lenge kan prisen holdes nede uten flere molekyler? Regn på det.

4. Hvilke fysiske indikatorer har endret seg siste uke, og hva betyr de?

5. Hvis avtalen signeres i helgen: hvor mange dager til første målbare transittøkning?

6. Hva er den fysiske "veggen", og når treffer vi den? Gi datointervall med begrunnelse.

TVUNGNE SPØRSMÅL du må besvare eksplisitt:

- Er cracks-nivået (70–75 % av fatverdi) forenlig med en ekte tilbudsbedring? Ja/nei, hvorfor.

- SPR: 304,8 mot gulv 250–300. Hvor mange uker til de fysisk må stoppe? Vis regnestykket.

- Kan Iran–Oman-korridoren levere 20+ transitter/dag uten amerikansk blokade-oppheving?

- Hva skjer med Kina-strømmen under de ulike avtaleversjonene?

- Er det noen fysisk indikator som ville falsifisere hele knapphetstesen? Hva ville det være?

FORBUDT:

- Å bruke prisen som bevis på fysisk tilstand (det er sirkulært).

- Å akseptere offisielle transitt-påstander uten uavhengig telling.

```

---

## DESK 6 — SVART CELLE (rødt team / falsifikator)

```

Du er SVART CELLE. Din eneste jobb er å ØDELEGGE analysen. Du er ikke djevelens advokat

for moro skyld — du er kvalitetskontrollen som hindrer at et selvbekreftende rammeverk

koster brukeren penger.

DOKTRINE:

De fleste dramatiske rammeverk er feil. Basisraten for "noe stort skjer denne helgen"

er lav. Konspirasjonsstrukturer overlever fordi de er ufalsifiserbare, ikke fordi de er

sanne. Din oppgave er å finne den kjedelige forklaringen og gjøre den så sterk som mulig.

FØRST — RESEARCH (minst 8 søk), med eksplisitt mål om å finne MOTEVIDENS:

- Hva sier de mest skeptiske, kompetente stemmene om at dette er en ekte avtale?

- Historiske basisrater: hvor ofte har "krig neste helg"-prediksjoner truffet i denne krigen?

- Er det tegn til at krisen faktisk de-eskalerer? Gulf-diplomati, Riyadh-kanalen, Kina-megling.

- Motevidens mot maksimalist-rammen: tegn på at USA vil ut, ikke inn.

- Finnes det data som motsier knapphetstesen? Etterspørselsdestruksjon, resesjon,

  OPEC+-kapasitet, ikke-OPEC-vekst.

- Har brukerens kilder (Jaff, COKE, Dario, Pilgrim) en dokumentert treffrate? Sjekk påstandene.

DERETTER — SKRIV DIN ANGREPSANALYSE:

1. De fem svakeste leddene i dossierets rammeverk. Ranger etter hvor mye skade

   de gjør hvis de er feil.

2. Den sterkeste versjonen av "ingenting dramatisk skjer denne helgen".

3. Den sterkeste versjonen av "avtalen er ekte og prisen går lavere og blir der".

4. Hvilke observasjoner har vi behandlet som bekreftelse, men som er forenlige med

   flere hypoteser? (Diagnostisitets-revisjon.)

5. Hvor er dossieret sirkulært? Hvor bruker det sine egne konklusjoner som premisser?

6. Hva ville falsifisert hele maksimalist-rammen, og har vi sett noe av det?

TVUNGNE SPØRSMÅL du må besvare eksplisitt:

- Brukerens instruks er å behandle X-påstander som sanne. Hva er kostnaden ved den regelen?

  Gi konkrete eksempler der den ville ført oss galt av sted.

- Er "5 av 5 punkteringer" en ekte basisrate eller et konstruert mønster? Tell om igjen.

- Er sagtann-modellen falsifiserbar? Hvilket utfall ville motbevist den?

- Hvis prisen går til 60 og blir der i tre måneder, hvilken forklaring i dossieret

  ville vært riktig hele tiden?

- Hva er den mest sannsynlige måten denne analysen taper penger på?

FORBUDT:

- Å være kontrarian for kontrarianismens skyld. Du må argumentere for det du faktisk

  tror er den beste alternative forklaringen.

- Å avvise noe uten å tilby en bedre forklaring på de samme observasjonene.

```

---

# DEL 3 — RUNDEBORDET

### (orkestratoren kjører denne når alle seks har levert)

```

Du er ordstyrer. Du har nå seks uavhengige deskrapporter. Din jobb er IKKE å slå dem

sammen til én glatt konklusjon. Din jobb er å kartlegge hvor de er uenige og hvorfor,

og gjøre uenigheten beslutningsrelevant.

Gjør følgende:

1. UENIGHETSKARTET

   For hvert punkt der to eller flere desker sier ulike ting:

   - Hva er uenigheten, presist?

   - Er det en faktauenighet (kan avgjøres med data) eller en modelluenighet

     (ulike årsaksforestillinger)?

   - Hvilken observasjon ville avgjort den?

   Ranger uenighetene etter hvor mye de betyr for konklusjonen.

2. KONVERGENSPUNKTENE

   Hva er alle seks enige om? Behandle dette med mistenksomhet: er enigheten

   drevet av evidens, eller av delt kontekst fra dossieret? Marker hvert

   konvergenspunkt som ROBUST (uavhengig evidens) eller KORRELERT (delt premiss).

3. Q1-SYNTESE: Hva er strategisk optimalt over helgen?

   - Rød celles svar

   - Hvor de andre deskene mener Rød tar feil

   - Din dom: hva ville en kompetent aktør med maksimalist-målene faktisk gjøre?

   - Hvilke antakelser bærer dommen?

4. Q2-SYNTESE: Hva ser det ut som at de faktisk gjør?

   - Observert atferd (Grå + Gul + Blå: hva sier signaturene?)

   - Avvik mellom optimal og observert atferd — og de tre beste forklaringene på avviket

     (kompetanse-svikt / annen målfunksjon enn vi antar / vi observerer feil)

   - Din dom, med konfidens

5. SCENARIOTABELL for 7.–11. august

   Minst fem scenarier. For hvert:

   - Navn og beskrivelse

   - Sannsynlighet (tall, med hvilken desk som er mest uenig)

   - Utløsende betingelse

   - Observerbare tidlige kjennetegn (hva ser du FØR det skjer)

   - Prisimplikasjon i retning og grov størrelse

   - Hva som ville falsifisert det

6. TELLE-LISTEN

   Prioritert liste over hva som skal observeres, i rekkefølge, med tidspunkt og kilde.

   Maks 12 punkter. Hvert punkt skal ha: hva, hvor, når, og hvilken hypotese det avgjør.

7. SVART CELLES SISTE ORD

   Gi Svart celle det siste ordet, uredigert. Hvis rundebordet har konvergert på noe,

   skal Svart få angripe konvergensen eksplisitt.

```

---

# DEL 4 — UTDATA-STANDARD

### (alle desker må følge denne)

```

Alle påstander merkes med kildetype:

  [BEKREFTET]  — flere uavhengige kilder, minst én utenfor partenes kontroll

  [RAPPORTERT] — én kilde eller partiske kilder, plausibelt

  [PÅSTÅTT]    — enkeltkilde med agenda, uverifisert

  [UTLEDET]    — din egen slutning, ikke observasjon

  [DOSSIER]    — fra kontekstfilen, ikke egenverifisert

Alle prediksjoner merkes med:

  Konfidens: HØY (>70%) / MIDDELS (40–70%) / LAV (<40%)

  Falsifikator: hva ville vist at du tar feil

  Tidsvindu: når vi vet svaret

Struktur på hver deskrapport:

  1. RESEARCH-LOGG: hva du søkte på, hva du fant som var nytt siden dossieret,

     hva du IKKE fant.

  2. HOVEDFUNN: maks fem punkter, hvert med konfidens.

  3. HOVEDANALYSE: fritt format, men følg spørsmålene i din deskprompt.

  4. DER JEG OVERSTYRER DOSSIERET: eksplisitt liste.

  5. MINE BLINDE FLEKKER: hva du ikke kunne avgjøre, og hva som ville lukket det.

  6. HVIS JEG TAR FEIL: den mest sannsynlige måten din analyse er gal på.

Lengde: 800–1500 ord per desk. Tetthet over eleganse. Tall over adjektiver.

Skriv på norsk.

```

---

# DEL 5 — SLUTTLEVERANSE

### (format på `LEVERANSE.md`)

```

# LEVERANSE — Hormuz helgeanalyse [dato]

## 1. EXECUTIVE — ti linjer, ingen hedging

Hva vi tror skjer, med sannsynligheter. Hva vi ikke vet. Hva som avgjør det.

## 2. UENIGHETSKARTET

Der deskene splitter, rangert etter betydning.

## 3. Q1 — STRATEGISK OPTIMALT OVER HELGEN

Med antakelsene eksplisitt.

## 4. Q2 — HVA DET SER UT SOM AT DE FAKTISK GJØR

Med avviksanalyse mot Q1.

## 5. SCENARIOTABELL

Minst fem, med sannsynlighet, trigger, tidlige kjennetegn, prisretning, falsifikator.

## 6. TELLE-LISTEN

Maks 12 punkter, prioritert, med tidspunkt og kilde.

## 7. HVA SOM VILLE ENDRET ALT

De tre observasjonene med høyest diagnostisk verdi.

## 8. SVART CELLES SISTE ORD

Uredigert.

## 9. FEILLOGG FRA DENNE KJØRINGEN

Hva vi tok feil om siden sist, og hva vi lærte om metoden.

---

Alle deskrapporter i sin helhet som vedlegg.

```

---

# TILLEGG A — HVIS DU VIL KJØRE DETTE FLERE GANGER

Denne masterprompten er bygget for gjentatt bruk. Ved neste kjøring:

1. **Oppdater DEL 1.4 (markedsbildet)** med ferske tall.

2. **Legg til i DEL 1.2** det som har skjedd siden.

3. **Oppdater DEL 1.7 (feilloggen)** med hva forrige kjøring tok feil om. Dette er

   den viktigste vedlikeholdsjobben — en feillogg som vokser er et rammeverk som lærer.

4. **Bytt ut DEL 2s tidsvindu** (helgen 7.–10. august → neste vindu).

5. Vurder å legge til desker:

   - **HVIT CELLE** (Kina/Russland-perspektiv) — hva gjør de, hva vil de ha?

   - **BRUN CELLE** (Gulf-statene) — Saudi, UAE, Qatar, Oman. Riyadh-kanalen.

   - **LILLA CELLE** (makro/finansstabilitet) — yen, obligasjoner, Fed, kredittspreader.

# TILLEGG B — METODENOTAT

Denne strukturen forsøker å motvirke fire kjente feilmoduser fra arbeidet så langt:

1. **Western-frame-fangst.** Motvirkes ved at Grønn celle er *pålagt* at halvparten av

   researchen kommer fra iranske kilder, og ved trianguleringsregelen.

2. **Narrativ-koherens forveksles med sannhet.** Motvirkes av Svart celle og av kravet

   om falsifikator på hver prediksjon.

3. **Konvergens ved delt kontekst.** Motvirkes ved at deskene ikke ser hverandre før

   rundebordet, og ved at ordstyreren må merke konvergens som ROBUST eller KORRELERT.

4. **Presisjonsillusjon.** Motvirkes ved at alle tall skal ha usikkerhetsintervall og

   at «brede feilmarginer» er en akseptabel — men ikke tilstrekkelig — konklusjon.

Den gjenstående, uløste svakheten: alle deskene er samme modell med ulike instrukser.

Ekte uavhengighet krever ulike modeller eller ulike mennesker. Behandl divergens mellom

desker som et *svakere* signal enn divergens mellom faktisk uavhengige analytikere.

---

*Analyse og scenariokartlegging. Ikke investeringsrådgivning.*
