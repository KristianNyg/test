# PROMPT — Strategisk lagerregnskap (lim inn hele filen i en ny sesjon)

Du skal lage et **tallregnskap over verdens strategiske petroleumslagre** per dags dato, regnet om til **antall dager gjenværende ved dagens faktiske slipprate**. Best effort: der data mangler, estimér åpent og vis intervall. «Det er vanskelig å si» er forbudt uten et påfølgende beste anslag med range.

## Kontekst (verifisér selv, ikke stol på meg)

Hormuz-krigen har pågått siden 28. februar 2026. Stredet er de facto stengt (transitter ~8–13/dag mot 88–140 førkrig, iransk tillatelses- og gebyrregime). IEA-estimert 3Q-underskudd ~1,8 mb/d. Kumulativt krigstrekk på lagre ~410 mb per medio august (IEA OMR 12.8). USAs SPR sto ved siste avlesning jeg kjenner (uke t.o.m. 14.8) på 293,4 mb med uttak 5–6 mb/uke, laveste nivå siden 1982. Uttaket skjer som **exchange** (170+ mb, levering primært april–august 2026, tilbakebetaling 2026–2029 med 18–24 % premie in natura) — sjekk om leveringsplanen faktisk er i ferd med å tørke inn nå. IEA koordinerte et 400 mb kollektivt slipp tidligere i krigen — finn ut hvor mye av det som er levert og hva som gjenstår.

## Oppgaven

For hvert lager under: **(a) nivå nå, (b) faktisk slipprate nå, (c) dager igjen til relevant gulv ved dagens rate, (d) hva «gulvet» faktisk er (juridisk, operasjonelt, politisk), (e) datakvalitet.**

1. **USA SPR** — nivå (DOE ukentlig + EIA WPSR), rate, dager til EPCA-gulvet 252,4 mb (grense for ikke-nød-salg), dager til operasjonelt minimum (~70 mb iht. DOE), og hva som kreves for å gå under hvert gulv (presidentiell «severe energy supply interruption»-erklæring gir ubegrenset uttak). Skill salg fra exchanges. Merk: USA er nettoeksportør — diskuter kort hva reserven faktisk beskytter.
2. **USA NEHHR** (Northeast Home Heating Oil Reserve) og bensinreserven hvis den finnes fortsatt — små, men politisk synlige inn mot fyringssesong.
3. **IEA-medlemmenes samlede offentlige lagre** — hvor mye av 90-dagerskravet er reelt tilgjengelig, hvor mye er allerede sluppet i krigen, og hvor mye «headroom» gjenstår for et nytt koordinert slipp. GAO/IEA-forbehold om tilgjengelighet skal med.
4. **Japan** — statlige + private pliktlagre, nivå og dager. Japan importerer ~90 % fra Midtøsten; regn deres dager mot *deres* importbortfall, ikke mot globalt.
5. **Sør-Korea** — samme øvelse.
6. **Kina SPR + kommersielle** — offisielle tall finnes ikke; bruk satellitt-/tankfarm-estimater (Kayrros, Vortexa, Kpler o.l. via siteringslag). Oppgi intervall ærlig (estimatene har historisk sprikt med ±3 måneder i dagers dekning: ~140 dager til ~6 måneder). Regn mot Kinas faktiske importbortfall fra Gulfen nå, ikke mot normalimport.
7. **India** — ISPR-kavernene (Visakhapatnam, Mangalore, Padur) + planlagte fase 2. Små i dager — vis det.
8. **EU/Europa** — medlemslandenes 90-dagers pliktlagre (EU-direktivet), hvem som har trukket, og tysk EBV/nasjonale særordninger. Ta med **gasslagre** som egen linje (EU-snitt, Tyskland spesifikt) målt i dager av vinterforbruk — det er samme knapphetsregnskap i en annen molekyl.
9. **Saudi-Arabia og Gulf-produsentenes egne lagre/ledig kapasitet** — ledig produksjonskapasitet er den egentlige «reserven» deres; anslå hvor mye som er reell og *tilgjengelig gitt at eksportrutene er skadet* (Abqaiq truffet 27.7, Yanbu degradert, Jizan forsinket — verifiser status).

## Metodekrav

- **Datér alt.** Hvert tall skal ha kildedato. Udaterte tall merkes [UDATERT] og vektes ned.
- **Merk hver størrelse:** [BEKREFTET] (offisiell publisering), [RAPPORTERT] (én god kilde), [ESTIMAT] (ditt eget, med intervall og metode).
- **Sjekk resirkulering aktivt.** Denne krigen har produsert 24+ tilfeller av gamle tall servert som ferske (COT-tall fra 2024, IEA-tall fra 2025, øvelser fra feil år). Søkemotor-sammendrag blander årganger — verifiser årstall på alt.
- **Skill tre gulv-begreper konsekvent:** juridisk gulv (f.eks. EPCA 252,4), operasjonelt gulv (pumpe-/kaverneteknisk), politisk gulv (nivået der fortsatt slipp blir uholdbart å forsvare). De gir svært ulike «dager igjen».
- **Regn dager på to måter der det gir mening:** (i) ved dagens faktiske slipprate, (ii) ved raten som ville trengs for å dekke det faktiske underskuddet (~1,8 mb/d globalt). Differansen er selve historien.
- **Interessekonflikt-varsel:** DOE/EIA-tall brukes i aktiv prisdemping av en interessert part; IEA koordinerte selv slippet; kinesiske tall er inferens. Si fra der tallet kommer fra noen med insentiv.
- Egress kan være blokkert for enkelte primærkilder — si eksplisitt når du leser gjennom siteringslag i stedet for primærkilden.

## Leveranse

1. **Én hovedtabell:** lager | nivå (dato) | rate | dager til juridisk gulv | dager til operasjonelt gulv | intervall | datakvalitet.
2. **En rangert liste over hvilke klokker som ringer først**, med kalenderdatoer og intervall.
3. **De tre største usikkerhetene** og hva som ville avgjort dem.
4. **Falsifikatorer:** for hver hoveddato, hva som ville bevist at den er feil.
5. Kort — maks en halv side — om hva regnskapet betyr: hvor lenge kan strategiske lagre i sum fortsette å maskere underskuddet på ~1,8 mb/d, med intervall.

Skriv på norsk. Tabeller og kildenavn kan stå på engelsk. Dette er scenarioanalyse, ikke investeringsrådgivning — men vær konkret med tall.
