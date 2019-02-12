import ply.yacc as yacc
from lexer import tokens

def p_program(p):
  '''
  program : PROGRAM ID DOUBLEDOT program_2nd
  '''
  p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + " "

def p_program_2nd(p):
  '''
  program_2nd : bloque
              | vars bloque
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += p[x] + " "
  p[0]

def p_vars(p):
  '''
  vars : VAR vars_2nd
  '''
  p[0] = p[1] + " " + p[2]

def p_vars_2nd(p):
  '''
  vars_2nd  : ID COMMA vars_2nd
            | ID DOUBLEDOT tipo SEMICOLON vars_3rd
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += p[x] + " "
  p[0]

def p_vars_3rd(p):
  '''
  vars_3rd  : empty
            | vars_2nd
  '''
  p[0] = p[1]

def p_tipo(p):
  '''
  tipo  : INTEGER 
        | FLOATING
  '''
  p[0] = p[1]

def p_bloque(p):
  '''
  bloque  : OPENKEY estatuto CLOSEKEY
          | OPENKEY empty CLOSEKEY
  '''
  p[0] = p[1] + " " + p[2] + " " + p[3]

def p_estatuto(p):
  '''
  estatuto  : estatuto_2nd estatuto_3rd
  '''
  p[0] = p[1] + " " + p[2]

def p_estatuto_2nd(p):
  '''
  estatuto_2nd  : asignacion
                | condicion
                | escritura
  '''
  p[0] = p[1]

def p_estatuto_3rd(p):
  '''
  estatuto_3rd  : empty
                | estatuto
  '''
  p[0] = p[1] + " "

def p_asignacion(p):
  '''
  asignacion  : ID EQUAL expresion SEMICOLON
  '''
  p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4]

def p_expresion(p):
  '''
  expresion :  exp expresion_2nd
  '''
  p[0] = p[1] + " " + p[2]

def p_expresion_2nd(p):
  '''
  expresion_2nd : empty
                  | LESSTHAN exp
                  | MORETHAN exp
                  | DIFFERENT exp
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += p[x] + " "
  p[0][0:-2]

def p_escritura(p):
  '''
  escritura : PRINT OPENPARENTHESIS escritura_2nd CLOSEPARENTHESIS SEMICOLON
  '''
  p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + " " + p[5]

def p_escritura_2nd(p):
  '''
  escritura_2nd : expresion escritura_3rd
                | CTE_STRING escritura_3rd
  '''
  p[0] = p[1] + " " + p[2]

def p_escritura_3rd(p):
  '''
  escritura_3rd : empty
                | COMMA escritura_2nd
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += p[x] + " "
  p[0]

def p_condicion(p):
  '''
  condicion : IF OPENPARENTHESIS expresion CLOSEPARENTHESIS bloque condicion_2nd SEMICOLON
  '''
  p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + " " + p[5] + " " + p[6] + " " + p[7]

def p_condicion_2nd(p):
  '''
  condicion_2nd : empty
                  | ELSE bloque
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += p[x] + " "
  p[0]

def p_exp(p):
  '''
  exp : termino exp_2nd
  '''
  p[0] = p[1] + " " + p[2]

def p_exp_2nd(p):
  '''
  exp_2nd : empty
          | PLUS exp
          | MINUS exp
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += p[x] + " "
  p[0]

def p_termino(p):
  '''
  termino : factor termino_2nd
  '''
  p[0] = p[1] + " " + p[2]

def p_termino_2nd(p):
  '''
  termino_2nd : MULTIPLY termino
              | DIVIDE termino
              | empty
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += p[x] + " "
  p[0]

def p_factor(p):
  '''
  factor  : OPENPARENTHESIS expresion CLOSEPARENTHESIS
          | var_cte
          | PLUS var_cte
          | MINUS var_cte 
  '''
  p[0] = ""
  for x in range(1, len(p)):
    p[0] += p[x] + " "
  p[0]

def p_var_cte(p):
  '''
  var_cte : ID
          | CTE_INT
          | CTE_FLOAT
  '''
  p[0] = str(p[1])

def p_empty(p):
  '''
  empty : 
  '''
  p[0] = ""

def p_error(p):
  print("Error en la gramática")

parser = yacc.yacc()

print("Teclea el nombre del archivo de texto")
name = input('parser >> ')
f = open(name).readlines()
for line in f:
  print("Expresion: " + line)
  result = parser.parse(line)
  print("Parser: " + str(result))
# while True:
#   try:
#     s = f.readline()
#   except EOFError:
#     break
#   if not s: continue
#   result = parser.parse(s)
#   print(result)
# Tarea_3.2/file.txt