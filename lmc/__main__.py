#Dette er en lmc-interpret skrevet i python
# coding=utf-8
from argparse import ArgumentParser
from lmc.scanner import read_program
from lmc.program import Program
import sys

def make_parser():
    parser = ArgumentParser(description="Run lmc programs from the terminal")

    parser.add_argument('file', \
                        metavar='FILENAME', \
                        help="Specify an UTF-8 formatted file to run")

    parser.add_argument('-v', '--verbose', \
                        action='store_true',\
                        help="Get a printout of all steps and memory for\
                                each step of lmc.")

    parser.add_argument('-e', '--explain', \
                        action='store_true',\
                        help="Provide a sentence explaining each step.")

    parser.add_argument('-s', '--step', \
                        action='store_true',\
                        help="Step through program by hitting enter.")

    parser.add_argument('-c', '--count', \
                        action='store_true',\
                        help="Count the number of instructions executed.")

    parser.add_argument('-m', '--memory', \
                        action='store_true',\
                        help="Print memory and registers on exit.")
    return parser

def explain(line, myProgram):
    instruksjon = myProgram.program[line]
    acc = myProgram.akkumulator
    inst = int(instruksjon) // 100
    add = int(instruksjon) % 100

    if instruksjon == 0:
        print("%i: HLT - Stopped running. Accumulator: %i" % (line, acc))

    elif inst == 1:
        print("%i: ADD - Adding register %i to the accumulator. %i + %i = %i"\
                % ( line, add, acc - myProgram.program[add], myProgram.program[add], acc))

    elif inst == 2:
        print("%i: SUB - Subtracting register %i from the accumulator. %i - %i = %i"\
                % ( line, add, acc + myProgram.program[add], myProgram.program[add], acc))

    elif inst == 3:
        print("%i: STA - Writing %i to register %i." % ( line, acc, add))

    elif inst == 5:
        print("%i: LDA - Loading %i from register %i." % (line, acc, add))

    elif inst == 6:
        print("%i: BRA - Jumping to %i. Fetching the next instruction from that register" % (line, add))

    elif inst == 7:
        if acc == 0:
            print("%i: BRZ - Jumping to %i because %i == 0." % (line, add, acc))
        else:
            print("%i: BRZ - Not jumping to %i because %i =/= 0." % (line, add, acc))

    elif inst == 8:
        if acc >= 0:
            print("%i: BRP - Jumping to %i, because %i is positive." % (line, add, acc))
        else: 
            print("%i: BRP - Not jumping because %i is negative." % (line, acc))

    elif inst == 9:
        if add == 1:
            print("%i: INP - Received input \"%i\" from standard in." % (line, acc))
        elif add == 2:
            print(myProgram.output)
            print("\n%i: OUT - Wrote the number \"%i\" to standard out." % (line, acc))
        elif add == 22:
            print(myProgram.output)
            print("\n%i: OTC - Wrote the character \"%s\" to standard out." % (line, chr(acc)))

def main():
    parser = make_parser()
    args = parser.parse_args()

    program = read_program(args.file)
        
    myProgram = Program(program)

    if args.verbose:
        print(myProgram)

    line = 0
    steps = 0

    while not myProgram.isHalted():
        myProgram.step()

        if args.verbose:
            print(myProgram)

        if args.explain:
            explain(line, myProgram)

        if args.step:
            input()

        line = myProgram.programteller
        steps += 1

    if args.memory:
        print(myProgram)

    if args.count:
        print("Finished execution in %i steps" % steps)

    if not args.memory and not args.verbose and not args.explain:
        print(myProgram.output, end="")


if __name__ == '__main__':
    main()
