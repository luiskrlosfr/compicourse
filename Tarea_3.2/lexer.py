import ply.lex as lex
import sys

tokens = [
  'ID',
  'SEMICOLON',
  'COMMA',
  'DOUBLEDOT',
  'CTE_INT',
  'CTE_FLOAT',
  'CTE_STRING',
  'OPENKEY',
  'CLOSEKEY',
  'EQUAL',
  'DIFFERENT',
  'LESSTHAN',
  'MORETHAN',
  'OPENPARENTHESIS',
  'CLOSEPARENTHESIS',
  'PLUS',
  'MINUS',
  'MULTIPLY',
  'DIVIDE'
]

reserved = {
  'program' : 'PROGRAM',
  'var' : 'VAR',
  'int' : 'INTEGER',
  'float' : 'FLOATING',
  'print' : 'PRINT',
  'if' : 'IF',
  'else' : 'ELSE',
}

t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_DOUBLEDOT = r'\:'
t_OPENKEY = r'\{'
t_CLOSEKEY = r'\}'
t_EQUAL = r'\='
t_DIFFERENT = r'\<\>'
t_LESSTHAN = r'\<'
t_MORETHAN = r'\>'
t_OPENPARENTHESIS = r'\('
t_CLOSEPARENTHESIS = r'\)'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'

t_ignore = r' '

def t_CTE_FLOAT(t):
  r'\d+\.\d+'
  t.value = float(t.value)
  return t

def t_CTE_INT(t):
  r'\d+'
  t.value = int(t.value)
  return t

def t_CTE_STRING(t):
  r"\'[^']*\'"
  t.type = reserved.get(t.value, 'CTE_STRING')
  t.value = t.value[1:-1]
  return t

def t_ID(t):
  r'[a-z]+'
  t.type = reserved.get(t.value, 'ID')
  return t

def t_error(t):
  print("Esos caracteres no forman parte del lenguaje")
  t.lexer.skip(1)

tokens = tokens + list(reserved.values())

lexer = lex.lex()

# lexer.input("123.45")
# lexer.input("12345")
# lexer.input("'12 3 45'")

# while True:
#   tok = lexer.token()
#   if not tok:
#     break
#   print(tok)