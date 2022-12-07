from ply import lex

tokens = ["nomLib","int","float","string","nomVar","finLinea","coma","igual","comp","parAb","parCerr","corchAb","corchCerr","dosPuntos","comBloque","comLinea"]

reservadas = {
  'BEGIN' : 'begin',
  'END': 'end',
  'VAR': 'var',
  'INCL': 'lib',
  'PROC': 'proc',
  'PIN': 'pin',
  'SAL' : 'pinSal',
  'ENT' : 'pinEnt',
  'ADEL' : 'adel',
  'ATRAS' : 'atras',
  'IZQUIERDA' : 'izq',
  'DERECHA' : 'der',
  'ESP' : 'esp',
  'STOP' : 'stop',
  'texto' : 'palResString',
  'entero' : 'palResInt',
  'decimal' : 'palResFloat',
  'logico' : 'palResBool',
  'SI' : 'si',
  'ENTONCES' : 'entonces',
  'SINO' : 'sino',
  'MIENTRAS' : 'mientras',
  'true' : 'true',
  'false' : 'false'
}

tokens += reservadas.values()

t_finLinea=r';'
t_coma=r','
t_igual=r'='
t_comp=r'(>|<|==|!=|<=|>=)'
t_parAb=r'\('
t_parCerr=r'\)'
t_corchAb=r'\['
t_corchCerr=r'\]'
t_dosPuntos=r':'
t_comBloque=r'//\*(.|\n)*\*//'
t_comLinea=r'//.*'
t_string=r'".+"'
t_ignore=r' '
t_float=r'\b(-|\+){0,1}[0-9]+\.[0-9]+\b'
t_int=r'(-|\+){0,1}[0-9]+'

def t_nomLib(t):
    r'[A-Za-z0-9_-]+\.[a-z]+'
    if t.value in reservadas:
        t.type = reservadas[ t.value ]
    return t

def t_nomVar(t):
    r'[A-Za-z][A-Za-z0-9_-]*'
    if t.value in reservadas:
        t.type = reservadas[ t.value ]
    return t

def t_error(t):
    print("__________________")
    print("Error: %s en linea %s" % (repr(t.value[0]), lexer.lineno))
    t.lexer.skip(1)
 
def t_newline(t):
  r'\n'
  t.lexer.lineno+=1

lexer = lex.lex()