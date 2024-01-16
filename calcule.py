import socket as sk
from math import sqrt, pi
import sympy as sy

def first(a, b):
  try:
    return sqrt(float(a)**2 + float(b)**2)
  except Exception:
    return "nan"


def saucisse(a, b):
  try:
    sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    sock.connect(("127.0.0.1", 1234))
    sock.sendall("data = {a:b}".encode("utf-8"))
    return sock.recv(1024).decode("utf-8")
  except Exception as e:
    return e


def cercle(side8):
  try:
    return f"aire du cercle : {sy.pi * (float(side8)**2)} ou environ {3.14*(float(side8)**2)}"
  except Exception:
    return 'nan'


def rectangle(a, b):
  try:
    return f"aire du rectangle : {float(a)*float(b)}"
  except Exception:
    return 'nan'


def triangle(a, b):
  try:
    return f"aire du triangle : {float(a)*float(b)/2}"
  except Exception:
    return 'nan'

def carre(a):

  try: 
    return f"aire du carré : {float(a)**2}"

  except Exception:
    return 'nan :)'


def cube(a):

  try:
    return f"volume du cube : {float(a)**3}"
  except Exception:
    return 'nan ;)'

def pave_droit(a, b, c):
  try:
    return f"volume du pavé droit : {float(a)*float(b)*float(c)}"

  except Exception:
    return 'nan :('

def boule(a):
  try:
    return f"volume de la boule : {4/3 * (pi*(float(a)**3))}"

  except Exception:
    
    return 'nan °_°'

def cylindre(a, b):
  try:
    return f"volume du cylindre : {pi*(float(a)**2)*float(b)}"

  except Exception:
    return 'nan +_+'

