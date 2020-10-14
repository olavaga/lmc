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
                        action='store_const',\
                        const=True,
                        default=False,
                        help="Get a printout of all steps and memory for\
                                each step of lmc.")

    parser.add_argument('-s', '--step', \
                        action='store_const',\
                        const=True,
                        default=False,
                        help="Step through program by hitting enter.")
    return parser

def main():
    parser = make_parser()
    args = parser.parse_args()

    if not args.file:
        parser.parse_args(['-h'])

    program = read_program(args.file)
        
    lmc = Program(program)

    for programteller, instruction_register, address_register, akkumulator in lmc:
        if args.verbose:
            print(lmc)
            print("Program counter:", programteller)
            print("Instruction register:", instruction_register)
            print("Address register:", address_register)
            print("Accumulator:", akkumulator)
        if args.step:
            input()
        pass



if __name__ == '__main__':
    main()
