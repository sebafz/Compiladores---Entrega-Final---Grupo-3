def traductor(p,funcion,primer_pin=False,pin=False,primer_mov=False,mov=False):
  with open("salida.ino","r") as fileRead:
    file_content=fileRead.readlines()
  with open("salida.ino","w") as fileWrite:
    if (p):
      if(pin):
        if(primer_pin):
          file_content+=['void setup(){\n'] + ['\n'] +['}\n']
        index = file_content.index('\n')
        file_content.insert(index, funcion(p))
        fileWrite.write("".join(file_content))
        return
      if(mov):
        if(primer_mov):
          file_content+=['void loop(){\n'] + ['\n'] +['}\n']
        index = file_content.index('\n',file_content.index('\n')+1)
        file_content.insert(index, funcion(p))
        fileWrite.write("".join(file_content))
        return
      file_content.append(funcion(p))
      fileWrite.write("".join(file_content))

def trad_librerias(p):
    list_p = list(p)
    return "".join(["#include <"]+list_p[3:4]+[">"]+["\n"])

def trad_var(p):
    list_p = list(p)
    if list_p[2] == 'entero':
      return 'int  'f'{list_p[4]};'+"\n"
    elif list_p[2] == 'texto':
      return 'string  'f'{list_p[4]};'+"\n"
    elif list_p[2] == 'logico':
      return 'bool  'f'{list_p[4]};'+"\n"
    elif list_p[2] == 'decimal':
      return 'float  'f'{list_p[4]};'+"\n"

def trad_asign(p):
    list_p = list(p)
    return f'{list_p[1]}:{list_p[2]}{list_p[3]};'+"\n"

def trad_pin(p):
    list_p = list(p)
    if list_p[3] == 'SAL':
      return f'pinMode({list_p[5]}, OUTPUT);'+"\n"
    elif list_p[3] == 'ENT':
      return f'pinMode({list_p[5]}, INPUT);'+"\n"

def trad_mov(p):
    list_p = list(p)
    if list_p[1] == 'ADEL':
      return 'avanzar();'+"\n"
    elif list_p[1] == 'ATRAS':
      return 'retroceder();'+"\n"
    elif list_p[1] == 'IZQUIERDA':
      return 'giro_izquierda();'+"\n"
    elif list_p[1] == 'DER':
      return 'giro_derecha();'+"\n"
    elif list_p[1] == 'STOP':
      return 'parar();'+"\n"
    elif list_p[1] == 'ESP':
      return f'esperar({list_p[3]});'+"\n"

def trad_func(p):
    list_p = list(p)
    result = "".join([list_p[2]]+["()"]+["{"]+["\n"]+["}"]+["\n"])
    if(list_p[6]==":"):
      if(list_p[4]==None and list_p[9]==None):
        result = "".join([list_p[7]]+[list_p[2]]+["()"]+["{"]+["\n"]+["}"]+["\n"])
    return result

def trad_si(p):
    result = "".join(["if ("]+[") "] + ["{"]+["\n"]+["}"]+["\n"])
    return result