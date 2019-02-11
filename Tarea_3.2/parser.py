import ply.yacc as yacc
from lexer import tokens

def p_program(p):
  '''
  program : PROGRAM ID DOUBLEDOT program_2nd
  '''

def p_program_2nd(p):
  '''
  program_2nd : bloque
              | vars bloque
  '''

def p_vars(p):
  '''
  vars : VAR vars_2nd
  '''

def p_vars_2nd(p):
  '''
  vars_2nd  : ID COMMA vars_2nd
            | ID DOUBLEDOT tipo SEMICOLON vars_3rd
  '''

def p_vars_3rd(p):
  '''
  vars_3rd  : empty
            | vars_2nd
  '''

def p_tipo(p):
  '''
  tipo  : INTEGER 
        | FLOATING
  '''

def p_bloque(p):
  '''
  bloque  : OPENKEY estatuto CLOSEKEY
  '''

def p_estatuto(p):
  '''
  estatuto  : estatuto_2nd estatuto_3rd
  '''

def p_estatuto_2nd(p):
  '''
  estatuto_2nd  : asignacion
                | condicion
                | escritura
  '''

def p_estatuto_3rd(p):
  '''
  estatuto_3rd  : empty
                | estatuto
  '''

def p_asignacion(p):
  '''
  asignacion  : ID EQUAL expresion SEMICOLON
  '''

def p_expresion(p):
  '''
  expresion :  exp expresion_2nd
  '''

def p_expresion_2nd(p):
  '''
  expresion_2nd : empty
                  | LESSTHAN exp
                  | MORETHAN exp
                  | DIFFERENT exp
  '''

def p_escritura(p):
  '''
  escritura : PRINT OPENPARENTHESIS escritura_2nd CLOSEPARENTHESIS SEMICOLON
  '''

def p_escritura_2nd(p):
  '''
  escritura_2nd : expresion escritura_3rd
                | CTE_STRING escritura_3rd
  '''

def p_escritura_3rd(p):
  '''
  escritura_3rd : empty
                | COMMA escritura_2nd
  '''

def p_condicion(p):
  '''
  condicion : IF OPENPARENTHESIS expresion CLOSEPARENTHESIS bloque condicion_2nd SEMICOLON
  '''

def p_condicion_2nd(p):
  '''
  condicion_2nd : empty
                  | ELSE bloque
  '''

def p_exp(p):
  '''
  exp : termino exp_2nd
  '''

def p_exp_2nd(p):
  '''
  exp_2nd : empty
          | PLUS exp
          | MINUS exp
  '''

def p_termino(p):
  '''
  termino : factor termino_2nd
  '''

def p_termino_2nd(p):
  '''
  termino_2nd : empty
              | MULTIPLY termino
              | DIVIDE termino
  '''

def p_factor(p):
  '''
  factor  : OPENPARENTHESIS expresion CLOSEPARENTHESIS
          | var_cte
          | PLUS var_cte
          | MINUS var_cte 
  '''

def p_var_cte(p):
  '''
  var_cte : ID
          | CTE_INT
          | CTE_FLOAT
  '''

def p_empty(p):
  '''
  empty : 
  '''
  pass

def p_error(p):
  print("Syntax error")

parser = yacc.yacc()

while True:
  try:
    s = input('parser: ')
  except EOFError:
    break