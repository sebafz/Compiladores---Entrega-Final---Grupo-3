from ply import yacc
from AL import *
import AL
from Traductor import *

primer_pin=False
primer_mov=False


def p_INICIO(p):
  '''INICIO : begin LIBRERIAS CUERPO end'''
  pass

def p_LIBRERIAS(p):
  '''LIBRERIAS : LIBRERIASP
  | EMPTY'''
  pass

def p_LIBRERIASP(p):
  '''LIBRERIASP : lib parAb nomLib parCerr finLinea LIBRERIAS'''
  traductor(p,trad_librerias)
  pass

def p_CUERPO(p):
  '''CUERPO : VAR CUERPO
        | ASIGN CUERPO
        | FUNC CUERPO
        | COMENTARIO CUERPO
        | SI CUERPO
        | SINO CUERPO
        | MIENTRAS CUERPO
        | PIN CUERPO
        | MOV CUERPO
        | EMPTY'''
  pass

def p_VAR(p):
  '''VAR : var palResString dosPuntos nomVar finLinea
  | var palResInt dosPuntos nomVar finLinea
  | var palResFloat dosPuntos nomVar finLinea
  | var palResBool dosPuntos nomVar finLinea'''
  traductor(p,trad_var)
  pass

def p_ASIGN(p):
  '''ASIGN : nomVar igual string finLinea
        | nomVar igual int finLinea
        | nomVar igual float finLinea
        | nomVar igual true finLinea
        | nomVar igual false finLinea
        | nomVar igual nomVar finLinea'''
  traductor(p,trad_asign)
  pass

def p_FUNC(p):
  '''FUNC : proc nomVar parAb PARAM parCerr corchAb CUERPO corchCerr finLinea
        | proc nomVar parAb PARAM parCerr dosPuntos TIPODATO corchAb CUERPO corchCerr finLinea'''
  traductor(p,trad_func)
  pass

def p_PARAM(p):
  '''PARAM : TIPODATO dosPuntos nomVar
        | TIPODATO dosPuntos nomVar coma PARAM
        | EMPTY'''
  pass

def p_TIPODATO(p):
  '''TIPODATO : palResInt
        | palResString
        | palResFloat
        | palResBool'''
  pass

def p_COMENTARIO(p):
  '''COMENTARIO : comBloque
        | comLinea'''
  pass

def p_SI(p):
  '''SI : si parAb COMPARACION parCerr entonces corchAb CUERPO corchCerr finLinea'''
  traductor(p,trad_si)
  pass

def p_SINO(p):
  '''SINO : si parAb COMPARACION parCerr entonces corchAb CUERPO corchCerr sino corchAb CUERPO corchCerr finLinea'''
  pass

def p_MIENTRAS(p):
  '''MIENTRAS : mientras parAb COMPARACION parCerr corchAb CUERPO corchCerr sino finLinea'''
  pass

def p_COMPARACION(p):
  '''COMPARACION : VALORVAR comp VALORVAR
        | nomVar comp VALORVAR
        | nomVar comp nomVar
        | false
        | true
        | nomVar'''
  pass

def p_VALORVAR(p):
  '''VALORVAR : string
        | true
        | false
        | int
        | float'''
  pass

def p_PIN(p):
  '''PIN : pin parAb pinEnt dosPuntos nomVar parCerr finLinea
        | pin parAb pinSal dosPuntos nomVar parCerr finLinea'''
  primer_pin = True if p_PIN.counter <= 0 else False
  p_PIN.counter += 1
  traductor(p, trad_pin, primer_pin=primer_pin, pin=True)
  pass

p_PIN.counter = 0


def p_MOV(p):
  '''MOV : adel parAb parCerr finLinea
        | atras parAb parCerr finLinea
        | izq parAb parCerr finLinea
        | der parAb parCerr finLinea
        | stop parAb parCerr finLinea
        | esp parAb int parCerr finLinea
        | esp parAb float parCerr finLinea'''
  primer_mov = True if p_MOV.counter <= 0 else False
  p_MOV.counter += 1
  traductor(p,trad_mov,primer_mov=primer_mov, mov=True)
  pass

p_MOV.counter=0

def p_EMPTY(p):
  '''EMPTY : '''
  pass

def p_error(p):
  print("Error sintáctico en la línea: " + str(p.lineno)
              + ". No se esperaba el token: " + str(p.value))        
  raise Exception('syntax', 'error') 
    
parser = yacc.yacc()
AL.lexer.lineno=0