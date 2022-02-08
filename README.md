# What

Parsing Assembly Source File to Graphs


## Instruction Set

```
cmp      rX, rY     ; compare registers: rX and rY
je       LABEL      ; if, the comparison above equal, jump to LABEL
mov      rX, $r123  ; move value to register
mov      rX, rY     ; move register value to register
jmp      LABEL      ; jmp without condition, just jump
```

## Dependencies

* Python 3.9.10
* PLY (pip install ply)

## Usage

`./main.py -l stam -f examples/code.1.s` or `python3 main.py -l stam -f examples/code.1.s`

## Some Facts about PLY module

* The `lex.py` module is used to break input text into a collection of tokens specified by a collection of regular expression rules.
* `yacc.py` is used to recognize language syntax that has been specified in the form of a context free grammar and also used to parse language syntax.
