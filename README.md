# Python-interpret for Little Man Computer

Dette er en tolker for LMC-programmer skrevet i python. Programmet er basert på Peter Higginsons Little Man Computer (se: https://www.peterhigginson.co.uk/LMC ). Denne tolkeren lar deg kjøre lmc-programmer i terminalen. 

## Installasjon

For å innstallere tolkeren må du først laste ned koden, enten gjennom git clone eller som et zip-arkiv. Deretter kan du bruke pip install for å installere pakken.

```
git clone https://github.com/olavaga/lmc.git
cd lmc
pip install .
```

Etter å ha gjort dette skal du kunne bruke kommandoen "lmc" i terminalen.

## Bruk

Interpreten kan kjøres med "lmc filnavn". Som standard vil kun outputs gitt med OUT og OTC-kommandoene skrives ut i terminalen. Ved INP vil du måtte skrive inn et svar. Oversikt for alle flagg får du med --help eller bare -h.

Med flagget -e vil du få ut en forklaring for hvert trinn tolkeren utfører. Hvis du ønsker å gå gjennom programmet steg for steg ved å trykke på enter for hver instruksjon, kan du sette flagget -s.

Hvis du ønsker å få ut hva som ligger i minne og registrene, kan du sette flagget -v. Da vil dette printes for alle trinn. Ønsker du kun å se tilstanden på slutten kan du angi dette med -m. Du kan også få ut antall operasjoner med --count. 

## Inndata fra fil

Bruk kommandoene under dersom du ønsker å mate test-data fra en annen fil.

```
cat inndata.txt | lmc program.txt
```
Eller hvis du ønsker å sammenligne med en tredje fil utdata.txt.
```
cat inndata.txt | lmc program.txt | diff utdata.txt
```

## Testing

For å teste at interpreten fungerer som den skal, kan du kjøre skriptet "test" i testdata-mappen. De er bygd opp basert på kommandoene over. 

## Kredit

Programmene velkommen.lmc og multiplikasjon.lmc er hentet fra forelesninger i IN1020 ved Universitetet i Oslo. Se https://www.uio.no/studier/emner/matnat/ifi/IN1020/h20/
