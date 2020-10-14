
class Program:

    def __init__(self, program):
        self.load(program)

    def load(self, program):
        self.program = program
        self.reset()

    def reset(self):
        self.programteller = 0
        self.akkumulator = 0
        self.output = ""
        self.inputs = []
        self.halted = False

    def isHalted(self):
        return self.halted

    def step(self):
        instruction_register = int(self.program[self.programteller]) // 100
        address_register = int(self.program[self.programteller]) % 100

        if self.halted:
            pass

        elif self.program[self.programteller] == 0: #HLT
            self.halted = True

        elif instruction_register == 1: #ADD
            self.akkumulator += self.program[address_register]
            self.programteller += 1
            
        elif instruction_register == 2: #SUB
            self.akkumulator -= self.program[address_register]
            self.programteller += 1

        elif instruction_register == 3: #STA
            self.program[address_register] = self.akkumulator
            self.programteller += 1

        elif instruction_register == 5: #LDA
            self.akkumulator = self.program[address_register]
            self.programteller += 1

        elif instruction_register == 6: #BRA
            self.programteller = address_register

        elif instruction_register == 7: #BRZ
            if self.akkumulator == 0:
                self.programteller = address_register
            else:
                self.programteller += 1

        elif instruction_register == 8: #BRP
            if self.akkumulator >= 0:
                self.programteller = address_register
            else:
                self.programteller += 1

        elif instruction_register == 9: 
            if address_register == 1: # 901 --> INP
                self.akkumulator = self.input()
                self.programteller += 1

            elif address_register == 2: # 902 --> OUT
                self.output += str(self.akkumulator) + "\n"
                self.programteller += 1

            elif address_register == 22: # 922 --> OTC
                self.output += chr(self.akkumulator)
                self.programteller += 1

            else:
                print("Invalid instruction %i on line %i" \
                        % (self.program[self.programteller], self.programteller))

        else:
            print("Invalid instruction %i on line %i" \
                    % (self.program[self.programteller], self.programteller))
        
    def input(self):
        if self.inputs:
            return int(self.inputs.remove(0))

        else:
            tall = input()
            while not self.erInt(tall) or -999 > int(self.akkumulator) > 999:
                tall = input("Vennligst oppgi et tall mellom -1000 og 1000: ")

            return int(tall)

    def erInt(self, tekst):
        try:
            int(tekst)
            return True

        except ValueError:
            return False

    def run(self):
        self.halted = False
        self.step()
        while self.program[self.programteller] != 0:
            self.step()

    def __repr__(self):
        tekststreng = ""
        instruction_register = int(self.program[self.programteller]) // 100
        address_register = int(self.program[self.programteller]) % 100

        for i in range(10):
            for j in range(10):
                tekststreng += str(self.program[i * 10 + j]).rjust(4, ' ')
            tekststreng += "\n"
        
        tekststreng += "\nProgram counter: " + str(self.programteller) + "\n"
        tekststreng += "Instruction register: " + str(instruction_register) + "\n"
        tekststreng += "Address register: " + str(address_register) + "\n"
        tekststreng += "Accumulator: " + str(self.akkumulator) + "\n"
        tekststreng += "\nOutput: " + str(self.output) + "\n"

        return tekststreng
