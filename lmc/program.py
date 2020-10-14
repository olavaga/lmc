
class Program:
    program = []
    programteller = 0
    akkumulator = 0

    def __init__(self, program):
        self.program = program

    def __iter__(self):
        self.programteller = 0
        self.akkumulator = 0
        return self

    def __next__(self):
        instruction_register = int(self.program[self.programteller]) // 100
        address_register = int(self.program[self.programteller]) % 100

        if instruction_register == address_register == 0:
            raise StopIteration

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
                self.akkumulator = input()
                while not self._erInt(self.akkumulator) or -999 > int(self.akkumulator) > 999:
                    self.akkumulator = input("Vennligst oppgi et tall mellom -1000 og 1000")
                self.akkumulator = int(self.akkumulator)
                self.programteller += 1

            elif address_register == 2: # 902 --> OUT
                print(self.akkumulator)

            elif address_register == 22: # 922 --> OTC
                print(chr(self.akkumulator), end = "")
                self.programteller += 1

            else:
                print("Invalid instruction %i on line %i" \
                        % (self.program[self.programteller], self.programteller))
                raise StopIteration

        else:
            print("Invalid instruction %i on line %i" \
                    % (self.program[self.programteller], self.programteller))
            raise StopIteration
        
        return (self.programteller, instruction_register, address_register, self.akkumulator)

    def __repr__(self):
        tekststreng = ""
        for i in range(10):
            for j in range(10):
                tekststreng += str(self.program[i * 10 + j]).rjust(4, ' ')
            tekststreng += "\n"
        return tekststreng

    
    def _erInt(self, tekst):
        try:
            int(tekst)
            return True
        except ValueError:
            return False
