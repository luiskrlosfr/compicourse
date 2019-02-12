# Luis Carlos Figueroa Rodríguez, A01113431
# 11/02/2019

import ply.lex as lex
import sys

# Define tokens
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

# Define reserved words (terminals) with their respective TOKEN
reserved = {
  'program' : 'PROGRAM',
  'var' : 'VAR',
  'int' : 'INTEGER',
  'float' : 'FLOATING',
  'print' : 'PRINT',
  'if' : 'IF',
  'else' : 'ELSE',
}

# Define simple terminal tokens
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

# Define complex terminal tokens
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

# Combine tokens with reserved words tokens
tokens = tokens + list(reserved.values())

# Build the lexer
lexer = lex.lex()

# Some Tests
# lexer.input("123.45") -> CTE_FLOAT token
# lexer.input("12345") -> CTE_INT token
# lexer.input("'12 3 45'") -> CTE_STRING token
# lexer.input("program test : { }") -> PROGRAM ID DOUBLEDOT OPENKEY CLOSEKEY tokens
# lexer.input("+ - * / = ; ,") -> PLUS MINUS MULTIPLY DIVIDE EQUAL SEMICOLON COMMA tokens