import sys

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

def verbose(string):
    if __name__ == '__main__':
        print(string)
    else:
        pass

def split_instruction(line):
    marker, instruction, location = "", "", ""
    line = line[0:line.find("//")]
    
    words = line.split()

    if 0 < len(words) and words[0] in kommandoer.keys():
        instruction = words[0]
        location = words[1] if 1 < len(words) else ""

    elif 1 < len(words) and words[1] in kommandoer.keys():
        marker = words[0]
        instruction = words[1]
        location = words[2] if 2 < len(words) else ""

    if instruction in ['HLT', 'INP', 'OTC', 'OUT']:
        location = ""
  
    return marker, instruction, location

def find_linemarkers(filename):
    merkelapper = {}
    linjeteller = 0

    with open(filename) as file:
        for line in file:
            marker, instruction, location = split_instruction(line)

            if not instruction:
                continue

            if marker:
                merkelapper[marker] = linjeteller

            linjeteller += 1

    return merkelapper

def read_program(filename):
    merkelapper = find_linemarkers(filename)
    verbose("Found markers: ")
    verbose(merkelapper)
    linjeteller = 0
    program = [0] * 100

    with open(filename) as file:
        for line in file:
            verbose("evaluating " + line)
            
            marker, kommando, loc = split_instruction(line)
            verbose("Found marker %s, instruction %s and location %s" % (marker, kommando, loc))

           
            if kommando == 'DAT':
                program[linjeteller] = int(loc) if loc else 0

            elif kommando and loc:
                if loc in merkelapper.keys():
                    program[linjeteller] = kommandoer[kommando] + merkelapper[loc]

                elif erInt(loc):
                    program[linjeteller] = kommandoer[kommando] + int(loc)

                else:
                    print(str(linjeteller) + ": Merkelapp " + loc + " ikke deklarert")
                    sys.exit(0)

            elif kommando:
                program[linjeteller] = kommandoer[kommando]

            else:
                continue

            linjeteller += 1

    return program

def erInt(tekst):
    try:
        int(tekst)
        return True

    except ValueError:
        return False



if __name__ == '__main__':

    if (len(sys.argv) < 2):
        print("Missing argument. Supply a filename to scan")
        sys.exit()

    program = read_program(sys.argv[1])

    print(program)
