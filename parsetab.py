
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'adel atras begin comBloque comLinea coma comp corchAb corchCerr der dosPuntos end entonces esp false finLinea float igual int izq lib mientras nomLib nomVar palResBool palResFloat palResInt palResString parAb parCerr pin pinEnt pinSal proc si sino stop string true varINICIO : begin LIBRERIAS CUERPO endLIBRERIAS : LIBRERIASP\n  | EMPTYLIBRERIASP : lib parAb nomLib parCerr finLinea LIBRERIASCUERPO : VAR CUERPO\n        | ASIGN CUERPO\n        | FUNC CUERPO\n        | COMENTARIO CUERPO\n        | SI CUERPO\n        | SINO CUERPO\n        | MIENTRAS CUERPO\n        | PIN CUERPO\n        | MOV CUERPO\n        | EMPTYVAR : var palResString dosPuntos nomVar finLinea\n  | var palResInt dosPuntos nomVar finLinea\n  | var palResFloat dosPuntos nomVar finLinea\n  | var palResBool dosPuntos nomVar finLineaASIGN : nomVar igual string finLinea\n        | nomVar igual int finLinea\n        | nomVar igual float finLinea\n        | nomVar igual true finLinea\n        | nomVar igual false finLinea\n        | nomVar igual nomVar finLineaFUNC : proc nomVar parAb PARAM parCerr corchAb CUERPO corchCerr finLinea\n        | proc nomVar parAb PARAM parCerr dosPuntos TIPODATO corchAb CUERPO corchCerr finLineaPARAM : TIPODATO dosPuntos nomVar\n        | TIPODATO dosPuntos nomVar coma PARAM\n        | EMPTYTIPODATO : palResInt\n        | palResString\n        | palResFloat\n        | palResBoolCOMENTARIO : comBloque\n        | comLineaSI : si parAb COMPARACION parCerr entonces corchAb CUERPO corchCerr finLineaSINO : si parAb COMPARACION parCerr entonces corchAb CUERPO corchCerr sino corchAb CUERPO corchCerr finLineaMIENTRAS : mientras parAb COMPARACION parCerr corchAb CUERPO corchCerr sino finLineaCOMPARACION : VALORVAR comp VALORVAR\n        | nomVar comp VALORVAR\n        | nomVar comp nomVar\n        | false\n        | true\n        | nomVarVALORVAR : string\n        | true\n        | false\n        | int\n        | floatPIN : pin parAb pinEnt dosPuntos nomVar parCerr finLinea\n        | pin parAb pinSal dosPuntos nomVar parCerr finLineaMOV : adel parAb parCerr finLinea\n        | atras parAb parCerr finLinea\n        | izq parAb parCerr finLinea\n        | der parAb parCerr finLinea\n        | stop parAb parCerr finLinea\n        | esp parAb int parCerr finLinea\n        | esp parAb float parCerr finLineaEMPTY : '
    
_lr_action_items = {'begin':([0,],[2,]),'$end':([1,33,],[0,-1,]),'lib':([2,119,],[6,6,]),'var':([2,3,4,5,8,9,10,11,12,13,14,15,16,21,22,93,94,95,96,97,98,112,113,114,115,116,119,120,121,122,123,132,135,136,137,138,141,150,151,153,157,159,161,163,164,167,],[-59,18,-2,-3,18,18,18,18,18,18,18,18,18,-34,-35,-24,-19,-20,-21,-22,-23,-52,-53,-54,-55,-56,-59,-15,-16,-17,-18,18,-57,-58,-4,18,18,-50,-51,18,-25,-36,-38,18,-26,-37,]),'nomVar':([2,3,4,5,8,9,10,11,12,13,14,15,16,20,21,22,47,49,50,59,60,61,62,93,94,95,96,97,98,108,110,111,112,113,114,115,116,119,120,121,122,123,125,132,135,136,137,138,141,150,151,153,157,159,161,163,164,167,],[-59,19,-2,-3,19,19,19,19,19,19,19,19,19,48,-34,-35,63,72,72,89,90,91,92,-24,-19,-20,-21,-22,-23,130,133,134,-52,-53,-54,-55,-56,-59,-15,-16,-17,-18,140,19,-57,-58,-4,19,19,-50,-51,19,-25,-36,-38,19,-26,-37,]),'proc':([2,3,4,5,8,9,10,11,12,13,14,15,16,21,22,93,94,95,96,97,98,112,113,114,115,116,119,120,121,122,123,132,135,136,137,138,141,150,151,153,157,159,161,163,164,167,],[-59,20,-2,-3,20,20,20,20,20,20,20,20,20,-34,-35,-24,-19,-20,-21,-22,-23,-52,-53,-54,-55,-56,-59,-15,-16,-17,-18,20,-57,-58,-4,20,20,-50,-51,20,-25,-36,-38,20,-26,-37,]),'comBloque':([2,3,4,5,8,9,10,11,12,13,14,15,16,21,22,93,94,95,96,97,98,112,113,114,115,116,119,120,121,122,123,132,135,136,137,138,141,150,151,153,157,159,161,163,164,167,],[-59,21,-2,-3,21,21,21,21,21,21,21,21,21,-34,-35,-24,-19,-20,-21,-22,-23,-52,-53,-54,-55,-56,-59,-15,-16,-17,-18,21,-57,-58,-4,21,21,-50,-51,21,-25,-36,-38,21,-26,-37,]),'comLinea':([2,3,4,5,8,9,10,11,12,13,14,15,16,21,22,93,94,95,96,97,98,112,113,114,115,116,119,120,121,122,123,132,135,136,137,138,141,150,151,153,157,159,161,163,164,167,],[-59,22,-2,-3,22,22,22,22,22,22,22,22,22,-34,-35,-24,-19,-20,-21,-22,-23,-52,-53,-54,-55,-56,-59,-15,-16,-17,-18,22,-57,-58,-4,22,22,-50,-51,22,-25,-36,-38,22,-26,-37,]),'si':([2,3,4,5,8,9,10,11,12,13,14,15,16,21,22,93,94,95,96,97,98,112,113,114,115,116,119,120,121,122,123,132,135,136,137,138,141,150,151,153,157,159,161,163,164,167,],[-59,23,-2,-3,23,23,23,23,23,23,23,23,23,-34,-35,-24,-19,-20,-21,-22,-23,-52,-53,-54,-55,-56,-59,-15,-16,-17,-18,23,-57,-58,-4,23,23,-50,-51,23,-25,-36,-38,23,-26,-37,]),'mientras':([2,3,4,5,8,9,10,11,12,13,14,15,16,21,22,93,94,95,96,97,98,112,113,114,115,116,119,120,121,122,123,132,135,136,137,138,141,150,151,153,157,159,161,163,164,167,],[-59,24,-2,-3,24,24,24,24,24,24,24,24,24,-34,-35,-24,-19,-20,-21,-22,-23,-52,-53,-54,-55,-56,-59,-15,-16,-17,-18,24,-57,-58,-4,24,24,-50,-51,24,-25,-36,-38,24,-26,-37,]),'pin':([2,3,4,5,8,9,10,11,12,13,14,15,16,21,22,93,94,95,96,97,98,112,113,114,115,116,119,120,121,122,123,132,135,136,137,138,141,150,151,153,157,159,161,163,164,167,],[-59,25,-2,-3,25,25,25,25,25,25,25,25,25,-34,-35,-24,-19,-20,-21,-22,-23,-52,-53,-54,-55,-56,-59,-15,-16,-17,-18,25,-57,-58,-4,25,25,-50,-51,25,-25,-36,-38,25,-26,-37,]),'adel':([2,3,4,5,8,9,10,11,12,13,14,15,16,21,22,93,94,95,96,97,98,112,113,114,115,116,119,120,121,122,123,132,135,136,137,138,141,150,151,153,157,159,161,163,164,167,],[-59,26,-2,-3,26,26,26,26,26,26,26,26,26,-34,-35,-24,-19,-20,-21,-22,-23,-52,-53,-54,-55,-56,-59,-15,-16,-17,-18,26,-57,-58,-4,26,26,-50,-51,26,-25,-36,-38,26,-26,-37,]),'atras':([2,3,4,5,8,9,10,11,12,13,14,15,16,21,22,93,94,95,96,97,98,112,113,114,115,116,119,120,121,122,123,132,135,136,137,138,141,150,151,153,157,159,161,163,164,167,],[-59,27,-2,-3,27,27,27,27,27,27,27,27,27,-34,-35,-24,-19,-20,-21,-22,-23,-52,-53,-54,-55,-56,-59,-15,-16,-17,-18,27,-57,-58,-4,27,27,-50,-51,27,-25,-36,-38,27,-26,-37,]),'izq':([2,3,4,5,8,9,10,11,12,13,14,15,16,21,22,93,94,95,96,97,98,112,113,114,115,116,119,120,121,122,123,132,135,136,137,138,141,150,151,153,157,159,161,163,164,167,],[-59,28,-2,-3,28,28,28,28,28,28,28,28,28,-34,-35,-24,-19,-20,-21,-22,-23,-52,-53,-54,-55,-56,-59,-15,-16,-17,-18,28,-57,-58,-4,28,28,-50,-51,28,-25,-36,-38,28,-26,-37,]),'der':([2,3,4,5,8,9,10,11,12,13,14,15,16,21,22,93,94,95,96,97,98,112,113,114,115,116,119,120,121,122,123,132,135,136,137,138,141,150,151,153,157,159,161,163,164,167,],[-59,29,-2,-3,29,29,29,29,29,29,29,29,29,-34,-35,-24,-19,-20,-21,-22,-23,-52,-53,-54,-55,-56,-59,-15,-16,-17,-18,29,-57,-58,-4,29,29,-50,-51,29,-25,-36,-38,29,-26,-37,]),'stop':([2,3,4,5,8,9,10,11,12,13,14,15,16,21,22,93,94,95,96,97,98,112,113,114,115,116,119,120,121,122,123,132,135,136,137,138,141,150,151,153,157,159,161,163,164,167,],[-59,30,-2,-3,30,30,30,30,30,30,30,30,30,-34,-35,-24,-19,-20,-21,-22,-23,-52,-53,-54,-55,-56,-59,-15,-16,-17,-18,30,-57,-58,-4,30,30,-50,-51,30,-25,-36,-38,30,-26,-37,]),'esp':([2,3,4,5,8,9,10,11,12,13,14,15,16,21,22,93,94,95,96,97,98,112,113,114,115,116,119,120,121,122,123,132,135,136,137,138,141,150,151,153,157,159,161,163,164,167,],[-59,31,-2,-3,31,31,31,31,31,31,31,31,31,-34,-35,-24,-19,-20,-21,-22,-23,-52,-53,-54,-55,-56,-59,-15,-16,-17,-18,31,-57,-58,-4,31,31,-50,-51,31,-25,-36,-38,31,-26,-37,]),'end':([2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,21,22,34,35,36,37,38,39,40,41,42,93,94,95,96,97,98,112,113,114,115,116,119,120,121,122,123,135,136,137,150,151,157,159,161,164,167,],[-59,-59,-2,-3,33,-59,-59,-59,-59,-59,-59,-59,-59,-59,-14,-34,-35,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-19,-20,-21,-22,-23,-52,-53,-54,-55,-56,-59,-15,-16,-17,-18,-57,-58,-4,-50,-51,-25,-36,-38,-26,-37,]),'parAb':([6,23,24,25,26,27,28,29,30,31,48,],[32,49,50,51,52,53,54,55,56,57,69,]),'corchCerr':([8,9,10,11,12,13,14,15,16,17,21,22,34,35,36,37,38,39,40,41,42,93,94,95,96,97,98,112,113,114,115,116,120,121,122,123,132,135,136,138,141,142,145,148,150,151,153,157,158,159,161,163,164,165,167,],[-59,-59,-59,-59,-59,-59,-59,-59,-59,-14,-34,-35,-5,-6,-7,-8,-9,-10,-11,-12,-13,-24,-19,-20,-21,-22,-23,-52,-53,-54,-55,-56,-15,-16,-17,-18,-59,-57,-58,-59,-59,149,152,155,-50,-51,-59,-25,162,-36,-38,-59,-26,166,-37,]),'palResString':([18,69,139,147,],[43,103,103,103,]),'palResInt':([18,69,139,147,],[44,102,102,102,]),'palResFloat':([18,69,139,147,],[45,104,104,104,]),'palResBool':([18,69,139,147,],[46,105,105,105,]),'igual':([19,],[47,]),'nomLib':([32,],[58,]),'dosPuntos':([43,44,45,46,79,80,100,102,103,104,105,124,],[59,60,61,62,110,111,125,-30,-31,-32,-33,139,]),'string':([47,49,50,107,108,],[64,75,75,75,75,]),'int':([47,49,50,57,107,108,],[65,76,76,86,76,76,]),'float':([47,49,50,57,107,108,],[66,77,77,87,77,77,]),'true':([47,49,50,107,108,],[67,74,74,128,128,]),'false':([47,49,50,107,108,],[68,73,73,129,129,]),'pinEnt':([51,],[79,]),'pinSal':([51,],[80,]),'parCerr':([52,53,54,55,56,58,69,70,72,73,74,75,76,77,78,86,87,99,101,127,128,129,130,131,133,134,140,147,154,],[81,82,83,84,85,88,-59,106,-44,-42,-43,-45,-48,-49,109,117,118,124,-29,-39,-46,-47,-41,-40,143,144,-27,-59,-28,]),'finLinea':([63,64,65,66,67,68,81,82,83,84,85,88,89,90,91,92,117,118,143,144,152,155,156,162,166,],[93,94,95,96,97,98,112,113,114,115,116,119,120,121,122,123,135,136,150,151,157,159,161,164,167,]),'comp':([71,72,73,74,75,76,77,],[107,108,-47,-46,-45,-48,-49,]),'corchAb':([102,103,104,105,109,124,126,146,160,],[-30,-31,-32,-33,132,138,141,153,163,]),'entonces':([106,],[126,]),'coma':([140,],[147,]),'sino':([149,155,],[156,160,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'INICIO':([0,],[1,]),'LIBRERIAS':([2,119,],[3,137,]),'LIBRERIASP':([2,119,],[4,4,]),'EMPTY':([2,3,8,9,10,11,12,13,14,15,16,69,119,132,138,141,147,153,163,],[5,17,17,17,17,17,17,17,17,17,17,101,5,17,17,17,101,17,17,]),'CUERPO':([3,8,9,10,11,12,13,14,15,16,132,138,141,153,163,],[7,34,35,36,37,38,39,40,41,42,142,145,148,158,165,]),'VAR':([3,8,9,10,11,12,13,14,15,16,132,138,141,153,163,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'ASIGN':([3,8,9,10,11,12,13,14,15,16,132,138,141,153,163,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'FUNC':([3,8,9,10,11,12,13,14,15,16,132,138,141,153,163,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'COMENTARIO':([3,8,9,10,11,12,13,14,15,16,132,138,141,153,163,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'SI':([3,8,9,10,11,12,13,14,15,16,132,138,141,153,163,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'SINO':([3,8,9,10,11,12,13,14,15,16,132,138,141,153,163,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'MIENTRAS':([3,8,9,10,11,12,13,14,15,16,132,138,141,153,163,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'PIN':([3,8,9,10,11,12,13,14,15,16,132,138,141,153,163,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'MOV':([3,8,9,10,11,12,13,14,15,16,132,138,141,153,163,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'COMPARACION':([49,50,],[70,78,]),'VALORVAR':([49,50,107,108,],[71,71,127,131,]),'PARAM':([69,147,],[99,154,]),'TIPODATO':([69,139,147,],[100,146,100,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> INICIO","S'",1,None,None,None),
  ('INICIO -> begin LIBRERIAS CUERPO end','INICIO',4,'p_INICIO','AS.py',11),
  ('LIBRERIAS -> LIBRERIASP','LIBRERIAS',1,'p_LIBRERIAS','AS.py',15),
  ('LIBRERIAS -> EMPTY','LIBRERIAS',1,'p_LIBRERIAS','AS.py',16),
  ('LIBRERIASP -> lib parAb nomLib parCerr finLinea LIBRERIAS','LIBRERIASP',6,'p_LIBRERIASP','AS.py',20),
  ('CUERPO -> VAR CUERPO','CUERPO',2,'p_CUERPO','AS.py',25),
  ('CUERPO -> ASIGN CUERPO','CUERPO',2,'p_CUERPO','AS.py',26),
  ('CUERPO -> FUNC CUERPO','CUERPO',2,'p_CUERPO','AS.py',27),
  ('CUERPO -> COMENTARIO CUERPO','CUERPO',2,'p_CUERPO','AS.py',28),
  ('CUERPO -> SI CUERPO','CUERPO',2,'p_CUERPO','AS.py',29),
  ('CUERPO -> SINO CUERPO','CUERPO',2,'p_CUERPO','AS.py',30),
  ('CUERPO -> MIENTRAS CUERPO','CUERPO',2,'p_CUERPO','AS.py',31),
  ('CUERPO -> PIN CUERPO','CUERPO',2,'p_CUERPO','AS.py',32),
  ('CUERPO -> MOV CUERPO','CUERPO',2,'p_CUERPO','AS.py',33),
  ('CUERPO -> EMPTY','CUERPO',1,'p_CUERPO','AS.py',34),
  ('VAR -> var palResString dosPuntos nomVar finLinea','VAR',5,'p_VAR','AS.py',38),
  ('VAR -> var palResInt dosPuntos nomVar finLinea','VAR',5,'p_VAR','AS.py',39),
  ('VAR -> var palResFloat dosPuntos nomVar finLinea','VAR',5,'p_VAR','AS.py',40),
  ('VAR -> var palResBool dosPuntos nomVar finLinea','VAR',5,'p_VAR','AS.py',41),
  ('ASIGN -> nomVar igual string finLinea','ASIGN',4,'p_ASIGN','AS.py',46),
  ('ASIGN -> nomVar igual int finLinea','ASIGN',4,'p_ASIGN','AS.py',47),
  ('ASIGN -> nomVar igual float finLinea','ASIGN',4,'p_ASIGN','AS.py',48),
  ('ASIGN -> nomVar igual true finLinea','ASIGN',4,'p_ASIGN','AS.py',49),
  ('ASIGN -> nomVar igual false finLinea','ASIGN',4,'p_ASIGN','AS.py',50),
  ('ASIGN -> nomVar igual nomVar finLinea','ASIGN',4,'p_ASIGN','AS.py',51),
  ('FUNC -> proc nomVar parAb PARAM parCerr corchAb CUERPO corchCerr finLinea','FUNC',9,'p_FUNC','AS.py',56),
  ('FUNC -> proc nomVar parAb PARAM parCerr dosPuntos TIPODATO corchAb CUERPO corchCerr finLinea','FUNC',11,'p_FUNC','AS.py',57),
  ('PARAM -> TIPODATO dosPuntos nomVar','PARAM',3,'p_PARAM','AS.py',62),
  ('PARAM -> TIPODATO dosPuntos nomVar coma PARAM','PARAM',5,'p_PARAM','AS.py',63),
  ('PARAM -> EMPTY','PARAM',1,'p_PARAM','AS.py',64),
  ('TIPODATO -> palResInt','TIPODATO',1,'p_TIPODATO','AS.py',68),
  ('TIPODATO -> palResString','TIPODATO',1,'p_TIPODATO','AS.py',69),
  ('TIPODATO -> palResFloat','TIPODATO',1,'p_TIPODATO','AS.py',70),
  ('TIPODATO -> palResBool','TIPODATO',1,'p_TIPODATO','AS.py',71),
  ('COMENTARIO -> comBloque','COMENTARIO',1,'p_COMENTARIO','AS.py',75),
  ('COMENTARIO -> comLinea','COMENTARIO',1,'p_COMENTARIO','AS.py',76),
  ('SI -> si parAb COMPARACION parCerr entonces corchAb CUERPO corchCerr finLinea','SI',9,'p_SI','AS.py',80),
  ('SINO -> si parAb COMPARACION parCerr entonces corchAb CUERPO corchCerr sino corchAb CUERPO corchCerr finLinea','SINO',13,'p_SINO','AS.py',84),
  ('MIENTRAS -> mientras parAb COMPARACION parCerr corchAb CUERPO corchCerr sino finLinea','MIENTRAS',9,'p_MIENTRAS','AS.py',88),
  ('COMPARACION -> VALORVAR comp VALORVAR','COMPARACION',3,'p_COMPARACION','AS.py',92),
  ('COMPARACION -> nomVar comp VALORVAR','COMPARACION',3,'p_COMPARACION','AS.py',93),
  ('COMPARACION -> nomVar comp nomVar','COMPARACION',3,'p_COMPARACION','AS.py',94),
  ('COMPARACION -> false','COMPARACION',1,'p_COMPARACION','AS.py',95),
  ('COMPARACION -> true','COMPARACION',1,'p_COMPARACION','AS.py',96),
  ('COMPARACION -> nomVar','COMPARACION',1,'p_COMPARACION','AS.py',97),
  ('VALORVAR -> string','VALORVAR',1,'p_VALORVAR','AS.py',101),
  ('VALORVAR -> true','VALORVAR',1,'p_VALORVAR','AS.py',102),
  ('VALORVAR -> false','VALORVAR',1,'p_VALORVAR','AS.py',103),
  ('VALORVAR -> int','VALORVAR',1,'p_VALORVAR','AS.py',104),
  ('VALORVAR -> float','VALORVAR',1,'p_VALORVAR','AS.py',105),
  ('PIN -> pin parAb pinEnt dosPuntos nomVar parCerr finLinea','PIN',7,'p_PIN','AS.py',109),
  ('PIN -> pin parAb pinSal dosPuntos nomVar parCerr finLinea','PIN',7,'p_PIN','AS.py',110),
  ('MOV -> adel parAb parCerr finLinea','MOV',4,'p_MOV','AS.py',120),
  ('MOV -> atras parAb parCerr finLinea','MOV',4,'p_MOV','AS.py',121),
  ('MOV -> izq parAb parCerr finLinea','MOV',4,'p_MOV','AS.py',122),
  ('MOV -> der parAb parCerr finLinea','MOV',4,'p_MOV','AS.py',123),
  ('MOV -> stop parAb parCerr finLinea','MOV',4,'p_MOV','AS.py',124),
  ('MOV -> esp parAb int parCerr finLinea','MOV',5,'p_MOV','AS.py',125),
  ('MOV -> esp parAb float parCerr finLinea','MOV',5,'p_MOV','AS.py',126),
  ('EMPTY -> <empty>','EMPTY',0,'p_EMPTY','AS.py',135),
]
