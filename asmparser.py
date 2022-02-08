import ply.yacc as yacc
from asmrules import tokens

def p_assembly_line(p: yacc.YaccProduction):
    '''assembly_line : mov
                     | start_label
                     | jmp
                     | je
                     | cmp
                     | empty'''
    print(f"[*] Instruction => {p[1]}")
    p[0] = p[1]


def p_jmp(p: yacc.YaccProduction) -> None:
    'jmp : JMP label'
    print(f"[*] @p_expression_jmp: {jmp} {p[2]}")
    p[0] =  p[1]

def p_mov(p: yacc.YaccProduction) -> None:
    '''mov : MOV register COMMA register
           | MOV register COMMA dec_num'''
    print(f"[*] @p_expression_mov: mov {p[2]}, {p[4]}")
    p[0] = ('assign', p[2], p[4])


def p_cmp(p: yacc.YaccProduction) -> None:
    '''cmp : CMP register COMMA register
           | CMP register COMMA dec_num'''
    print("[*] @p_expression_cmp:", end=" ")
    print("CMP ", p[2], ",", p[4])


def p_je(p: yacc.YaccProduction) -> None:
    'je : JE label'
    print("[*] @p_expression_je:", end=" ")
    print("JE ", p[1])
    p[0] = p[1]


def p_register(p: yacc.YaccProduction):
    'register : REGISTER'
    print(f"[*] @p_expression_register: {p[1]}")
    p[0] = ("register", p[1])


def p_dec_num(p: yacc.YaccProduction):
    'dec_num : DEC_NUM'
    decimal_number = int(int(p[1][1:]))
    print(f"[*] @p_expression_dec_num: {decimal_number}")
    p[0] = ("dec_num", decimal_number)


def p_label(p: yacc.YaccProduction):
    'label : LABEL'
    print(f"[*] @p_expression_label : label => {p[1]}")
    p[0] = ("LABEL", p[1])

def p_label_start(p: yacc.YaccProduction):
    'start_label : LABEL_START'
    print(f"[*] @p_expression_label_start => start_label {p[1]}")
    p[0] = ("start_label", p[1])


def p_empty(p: yacc.YaccProduction):
    'empty : '
    p[0] = None


# Syntax Error Handling
def p_error(p: yacc.YaccProduction) -> None:
    print("Syntax error at '%s'" % p.value)
    return
