import sympy as sy

def simplifi(a):
  try:
    a = sy.simplify(a)
  except Exception:
    a = 'nan'

  return a


def devellope(a):
  try:
    return sy.sy.evalf(a)
  except Exception:
    return 'nan'


def solve(a):
  try:
    return sy.solveset(sy.sympify(a))
  except Exception:
    return 'nan'


def factorize(a):
  try:
    return sy.factor(sy.sympify(a))
  except Exception:
    return 'nan'


def racine_cube(a):
  try:
    return f"expression factoriser : {sy.cbrt(int(a))}"
    
  except Exception:
    return 'nan'


def percent(a, b):
  try:
    return f"{b}% de {a} est {(int(a) * int(b)) / 100}"

  except Exception:
    return 'nan :{'

def percent_find(a, b):
  try:
    return f"{b} est {(int(a) * int(b)) / 100} % de {a}"

  except Exception:
    return 'nan : ]'

def sinus(a):
  try:
    return f"sinus de {a} est {sy.N(sy.sin(a))}"
  except Exception:
    return 'nan :['

def cosinus(a):
  try:
    return f"le cosinus de {a} est {sy.N(sy.cos(a))}"
  except Exception:
    return 'nan  +('

def tangente(a):
  try:
    return f"la tengente de {a} est {sy.N(sy.tan(a))}"

  except Exception:
    return 'nan :{'