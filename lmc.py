#Dette er en lmc-interpret skrevet i python
# coding=utf-8
import sys

global merkelapper, program, verbose, programteller, akkumulator, kommandoer, koder
merkelapper = {}

program = [0] * 100
verbose = False
programteller = 0
akkumulator = 0

def avslutt(loc):
    if verbose:
        print("%i: avslutter programmet" % (programteller))
    sys.exit()

def adder(loc):
    global program, programteller, akkumulator, verbose
    akkumulator += program[loc]
    programteller += 1
    if verbose:
        print("%i: la til %i i minnelokasjon %i" % (programteller, akkumulator, loc))

def subtraher(loc):
    global program, programteller, akkumulator, verbose
    akkumulator -= program[loc]
    programteller += 1
    if verbose:
        print("%i: trakk fra til %i i minnelokasjon %i" % (programteller, akkumulator, loc))

def lagre(loc):
    global program, programteller, akkumulator, verbose
    program[loc] = akkumulator
    programteller += 1
    if verbose:
        print("%i: Lagret %i i minnelokasjon %i" % (programteller, akkumulator, loc))

def last(loc):
    global program, programteller, akkumulator, verbose
    akkumulator = program[loc]
    programteller += 1
    if verbose:
        print("%i: Lastet verdi %i fra minnelokasjon %i" % (programteller, akkumulator, loc))

def hopp(loc):
    global program, programteller, verbose
    programteller = loc
    if verbose:
        print("%i: Hoppet til programlinje %i" % (programteller, loc))

def hopphvisnull(loc):
    global program, programteller, akkumulator, verbose
    if akkumulator == 0:
        programteller = loc
        if verbose:
            print("%i: Hoppet til programlinje %i" % (programteller, loc))
    else:
        programteller += 1
        if verbose:
            print("%i: Akkumulatoren er =/= 0. Hopper ikke" % (programteller))

def merk(navn, loc):
    global program, programteller, merkelapper, verbose
    merkelapper[navn] = loc

    if verbose:
        print("%i: Lagrer %i som %s" % (programteller, loc, navn))

def hopphvispositiv(loc):
    global program, programteller, akkumulator, verbose
    if int(akkumulator) >= 0:
        programteller = loc
        if verbose:
            print("%i: Hoppet til programlinje %i" % (programteller, loc))
    else:
        programteller += 1
        if verbose:
            print("%i: Akkumulatoren er negativ. Hopper ikke" % (programteller))

def inndata(loc):
    global program, programteller, akkumulator, verbose
    akkumulator = input()
    while not erInt(akkumulator) or -999 > int(akkumulator) > 999:
        akkumulator = input("Vennligst oppgi et tall mellom -1000 og 1000")
    akkumulator = int(akkumulator)
    programteller += 1
    if verbose:
        print("%i: Hentet %s fra bruker og lagret i akkumulator" % (programteller, akkumulator))

def skrivut(loc):
    global program, programteller, akkumulator
    print(akkumulator)
    programteller += 1
    if verbose:
        print("%i: Printet %s til bruker"  % (programteller, akkumulator))

def skrivASCII(loc):
    global program, programteller, akkumulator
    print(chr(akkumulator), end = "")
    programteller += 1
    if verbose:
        print("\n%i: Printet %s til bruker"  % (programteller, chr(akkumulator)))


kommandoer = {'HLT': 0,
              'ADD': 100,
              'SUB': 200,
              'STA': 300,
              'STO': 300,
              'LDA': 500,
              'BRA': 600,
              'BRZ': 700,
              'BRP': 800,
              'INP': 901,
              'OUT': 902,
              'OTC': 922,
              'DAT': -1}

koder = {  0: avslutt,
         100: adder,
         200: subtraher,
         300: lagre,
         500: last,
         600: hopp,
         700: hopphvisnull,
         800: hopphvispositiv,
         901: inndata,
         902: skrivut,
         922: skrivASCII}


def erInt(tekst):
    try:
        int(tekst)
        return True
    except ValueError:
        return False

def kjor():
    global programteller, akkumulator, program, koder
    for _ in range(100):
        data = program[programteller]
        kode = 100 * (data // 100)

        if data == 901 or data == 902 or data == 922:
            kode = data


        funksjon = koder[kode]
        loc = data % 100
        funksjon(loc)

def main():
    if (len(sys.argv) == 1):
        print("Dette programmet tar et filnavn som argument")
        sys.exit()


    linjeteller = 0

    with open(sys.argv[1]) as file:
        for line in file:
            merkelapp = ""
            for k in kommandoer.keys():
                if k in line:
                    if 0 < line.find(k):
                        merkelapp = line[:line.find(k)]
                        merkelapp=merkelapp.strip(' \n\r')
                        break

            if merkelapp:
                merkelapper[merkelapp] = linjeteller
            linjeteller += 1

        file.seek(0,0)
        linjeteller = 0

        for line in file:
            kommando, loc = "",""
            line = line[0:line.find("//")]
            for k in kommandoer.keys():
                if k in line:
                    if len(line[line.rfind(k):line.rfind(k) + len(k)+1].strip(' \n\r')) != len(k):
                        continue
                    slutt = line.rfind(k) + len(k)

                    kommando=k
                    if slutt < len(line):
                        loc = line[slutt:]

                    kommando=kommando.strip(' \n\r')
                    loc=loc.strip(' \n\r')

                    break
            else:
                print("Fant ingen kommando på linje %i" % (linjeteller))

            print(kommando,loc)

            if kommando == 'DAT':
                    if erInt(loc):
                        program[linjeteller] = int(loc)
            elif kommando and loc:

                if erInt(loc):
                    program[linjeteller] = kommandoer[kommando] + int(loc)
                elif loc in merkelapper.keys():
                    program[linjeteller] = kommandoer[kommando] + merkelapper[loc]
                else:
                    program[linjeteller] = kommandoer[kommando]

            elif kommando:
                program[linjeteller] = kommandoer[kommando]

            linjeteller += 1

    print(program)
    print(merkelapper)

    kjor()



if __name__ == '__main__':
    main()
