# Python-interpret for Little Man Computer

Dette er en tolker for LMC-programmer skrevet i python. Programmet er basert på www.peterhigginson.co.uk/LMC. Tolkeren lar deg kjøre lmc-programmer i terminalen. Prøv selv med et av test-programmene. For eksempel "python3 lmc.py velkommen.py"

Programmene velkommen.lmc og multiplikasjon.lmc er hentet fra forelesninger i IN1020 ved Universitetet i Oslo. Se https://www.uio.no/studier/emner/matnat/ifi/IN1020/h20/

## Installasjon

For å innstallere tolkeren må du først laste ned koden, enten gjennom git clone eller som et zip-arkiv. Deretter må du bruke pip install for å installere pakken.

git clone https://github.com/olavaga/lmc.git
cd lmc
pip install .

Etter å ha gjort dette skal du kunne bruke kommandoen "lmc" i terminalen.

## Bruk

Interpreten kan kjøres med "lmc filnavn". Som standard vil kun outputs gitt med OUT og OTC-kommandoene skrives ut i terminalen. Ved INP vil du måtte skrive inn et svar. Hvis du ønsker å få ut hva som ligger i minne og registrene, kan du sette flagget -v. Hvis du ønsker å gå gjennom programmet steg for steg ved å trykke på enter for hver instruksjon, kan du sette flagget -s.

## Inndata fra fil

cat inndata.txt | lmc program.txt

cat inndata.txt | lmc program.txt | diff utdata.txt

## Testing

For å teste at interpreten fungerer som den skal, kan du kjøre skriptet "test" i testdata-mappen. 


