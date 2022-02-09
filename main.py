#!/usr/bin/env python3

import ply.lex as lex
import ply.yacc as yacc
import asmrules
import asmparser
import argparse
import sys


tokens = asmrules.tokens

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--asm-file", help="Provide an assembly input file", type=str, required=True)
parser.add_argument("-l", "--start-label", help="Position the program to start from a label", type=str, required=True)
args = parser.parse_args()

print("Building the lexer\n")
lexer = lex.lex(module=asmrules, optimize=1, debug=False, outputdir=r"ply_debug/")


try:
    with open(args.asm_file, "r") as fp:
        data = fp.read()
except FileNotFoundError:
    sys.exit("File Not Found")

# TODO: Check If Label Exist
#start_label = args.start_label


# Give the lexer input
lexer.input(data)

# Tokenize
while data:
    token = lexer.token()
    if not token:
        break
    print(token)
else:
    print("Lexer has done\n")

print("Building the parser\n")
parser = yacc.yacc(module=asmparser, debug=False, outputdir="ply_debug/")
result = parser.parse(data)
print("result of parser =", result)

print("parser has built\n")

