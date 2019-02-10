import ply.yacc as yacc

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

def p_type(p):
  '''
  type  : INTEGER 
        | FLOATING
  '''
  p[0] = p[1]

def p_expression(p):
  '''
  expression :  exp expression_2nd
  '''

def p_expression_2nd(p):
  '''
  exxpression_2nd : empty
                  | LESSTHAN exp
                  | MORETHAN exp
                  | DIFFERENT exp
  '''

def p_escritura(p):
  '''
  escritura : print OPENPARENTHESIS expression CLOSEPARENTHESIS ;
            | 
  '''
  print(p[2])

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
              | * termino
              | / termino
  '''

def p_factor(p):
  '''
  factor  : OPENPARENTHESIS expression CLOSEPARENTHESIS
          | var_cte
          | PLUS var_cte
          | MINUS var_cte 
  '''

def p_var_cte(p):
  '''
  var_cte : ID
          | CTE_L
          | CTE_F
  '''
  p[0] = p[1]

def p_empty(p):
  '''
  empty : 
  '''

while True:
  try:
    s = input('')
  except EOFError:
    break