import ply.lex as lex
from ply.lex import TOKEN
import inspect


# List of token names
tokens = ( 
    "COMMENT",
    "MOV",
    "CMP",
    "JE",
    "JMP",
    "COMMA",
    "DEC_NUM",
    "REGISTER",
    "LABEL",
    "LABEL_START"
)

t_MOV           = r'[mM][oO][vV]'
t_CMP           = r'[cC][mM][pP]'
t_JE            = r'[jJ][eE]'
t_JMP           = r'[jJ][mM][pP]'
t_COMMA         = r','
t_REGISTER      = r'[rR][0-9]+'
t_DEC_NUM       = r'\$[0-9]+'
t_LABEL         = r'[a-zA-Z]+'
t_LABEL_START   = r'[a-zA-Z]+:'
t_COMMENT       = r';.*'

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

    
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    # No Pass value, thus token is discarded.


# Error handling rule
def t_error(t):
    print("@%s says: Illegal character '%s'" % ((inspect.stack()[0][3], t.value[0])))
    t.lexer.skip(1)

