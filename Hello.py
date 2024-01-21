from math import sqrt

import streamlit as stl

from calcule import *
from expressions_math import *
import random


def exos():
  cote1, cote2 = random.randint(1,200), random.randint(1,200)
  hypotenus = random.randint(1,200)

  while sqrt(((cote1**2) + (cote2**2))) != hypotenus:
    cote1, cote2 = random.randint(1,200), random.randint(1,200)
    hypotenus = random.randint(1,200)

    stl.session_state["cote1"],stl.session_state["cote2"] = cote1, cote2
    stl.session_state["hypotenus"] = hypotenus


def fun():
  stl.balloons()
  stl.snow()
  

stl.title("All for maths")
stl.button("fun", on_click=fun)

c = stl.sidebar.selectbox(options=[
  
  "Pythagore", 
  "racine carrée", 
  "simplifier", 
  "develloper",
  "résoudre une equation", 
  "factoriser une expression",
  "calculer une aire (en developpement)",
  "racine cube",
  "calculer un volume (en developpement)",
  "chatons mignon",
  "map",
  "pourcentage",
  "Fonctions trigonométriques",
  "comparer deux textes",
  "exercices sur Pythagore"
  
], label='**choisissez svp**, vous pouvez recherchez')

if c == "Pythagore":
  
  st = stl.container()
  st.subheader("Pythagore")

  side1 = st.text_input("Enter side 1", key="side1")
  side2 = st.text_input("Enter side 2", key="side2")

  result = st.write(f"**hypoténuse** : **{first(side1, side2)}**")


elif c == "racine carrée":
  
  st2 = stl.container()
  st2.subheader("racine carrée ")

  side3 = st2.text_input("Enter side 1", key="side3")

  st2.write(
      f'racine carré : {sqrt(float(side3)) if side3.isdigit() else "nan"}')



elif c == "simplifier":
  
  st3 = stl.container()
  st3.title("simplifier")
  side4 = st3.text_input("Entrer une expression a simplifier ", key="side4")
  st3.write(f"expression simplifiée : {simplifi(side4)}")



elif c == "develloper":
  
  st4 = stl.container()
  st4.subheader("Develloper")
  side5 = st4.text_input("Entrer une expression a develloper ", key="side5")
  st4.write(f"expression develloper : {devellope(side5)}")



elif c == "résoudre une equation":
  
  st5 = stl.container()
  st5.subheader("Résoudre une équation")
  side6 = st5.text_input("Entrer une équation ", key="side6")
  st5.write(f"solution : {solve(side6)}")



elif c == "factoriser une expression":
  
  st6 = stl.container()
  st6.subheader("Factoriser une expression")
  side7 = st6.text_input("Entrer une expression a factoriser ", key="side7")
  st6.write(f"expression factorisée : {factorize(side7)}")



elif c == "calculer une aire (en devellopement)":
  
  st7 = stl.container()
  st7.subheader("Calculer une aire")
  value = st7.selectbox("Choisir une forme",
                        ["cercle", "rectangle", "triangle", "carré"])
  
  if value == "cercle":
    
    side8 = st7.text_input("Entrer le rayon du cercle ", key="side8")
    st7.write(cercle(side8))
    
  elif value == "rectangle":
    
    side9 = st7.text_input("Entrer la longueur du rectangle ", key="side9")
    side10 = st7.text_input("Entrer la largeur du rectangle ", key="side10")
    st7.write(rectangle(side9, side10))
    
  elif value == "triangle":
    
    side11 = st7.text_input("Entrer la longueur du triangle ", key="side11")
    side12 = st7.text_input("Entrer la largeur du triangle ", key="side12")
    st7.write(triangle(side11, side12))

  elif value == "carré":
    side13 = st7.text_input("Entrer la longueur du carré ", key="side13")
    st7.write(carre(side13))


elif c == "racine cube":

  container6 = stl.container()
  container6.subheader("Racine cube")
  number = container6.text_input("Entrer un nombre", key="racine_cube")
  container6.write(racine_cube(number))


elif c == "calculer un volume (en devellopement)":

  st8 = stl.container()
  st8.subheader("Calculer un volume")

  value = st8.selectbox("Choisir une forme",[
    
    "cube", "pavé droit", "boule", "cylindre"
    
  ])
  
  if value == "cube":
    side14 = st8.text_input("Entrer la longueur du cube ", key="side14")
    st8.write(cube(side14))

  elif value == "pavé droit":
    side15 = st8.text_input("Entrer la longueur du pavé droit ", key="side15")
    side16 = st8.text_input("Entrer la largeur du pavé droit ", key="side16")
    side17 = st8.text_input("Entrer la hauteur du pavé droit ", key="side17")
    st8.write(pave_droit(side15, side16, side17))

  elif value == "boule":
    
    side18 = st8.text_input("Entrer le rayon de la boule ", key="side18")
    st8.write(boule(side18))

  elif value == "cylindre":
    side19 = st8.text_input("Entrer le rayon du cylindre ", key="side19")
    side20 = st8.text_input("Entrer la hauteur du cylindre ", key="side20")

    st8.write(cylindre(side19, side20))



elif c == "chatons mignon":
  stl.balloons()
  last_container = stl.container()
  last_container.subheader("chatons mignon")
  last_container.image("chaton2.png")
  last_container.image("chaton1.png")

elif c == "map":
  tlc = stl.container()
  tlc.subheader("map")
  tlc.map()

elif c == "pourcentage":
  container7 = stl.container()
  container7.subheader("pourcentage")
  mode = container7.selectbox("Choisir une mode", ["calculer", "trouver"])
  
  if mode == "calculer":
    number = container7.text_input("Entrer un nombre", key="number")
    number2 = container7.text_input("Entrer un pourcentage", key="number2")
    container7.write(percent(number, number2))

  elif mode == "trouver":
    number = container7.text_input("Entrer un nombre", key="number")
    number2 = container7.text_input("Entrer un deuxieme nombre", key="number2")
    container7.write(percent_find(number, number2))

elif c == "Fonctions trigonométriques":
  container8 = stl.container()
  container8.subheader("Fonctions trigonométriques")
  mode = container8.selectbox("Choisir une mode", ["sinus", "cosinus", "tangente"])
  
  if mode == "sinus":
    number = container8.text_input("Entrer un nombre", key="number")
    container8.write(sinus(number))

  elif mode == "cosinus":
    number = container8.text_input("Entrer un nombre", key="number")
    container8.write(cosinus(number))

  elif mode == "tangente":
    number = container8.text_input("Entrer un nombre", key="number")
    container8.write(tangente(number))
    
  else:
    container8.write("vous pouvez chercher dans la box de selections ;)")


elif c == "comparer deux textes":
  container9 = stl.container()
  container9.subheader("comparer deux textes")
  text1 = container9.text_input("Entrer un texte", key="text1")
  text2 = container9.text_input("Entrer un texte", key="text2")
  if text1 == text2:
    container9.write("les deux textes sont égaux")
  else:
    container9.write("les deux textes sont différents")



elif c == "exercices sur Pythagore":
  container10 = stl.container()
  exos()
  st.button("reset ...", on_click=exos)
  a, b = stl.session_state["cote1"], stl.session_state["cote2"] 
  

  container10.write(f"si mon premier cote est de {a} et que mon deuxieme cote est de {a}, alors de combien est mon hypotenus ?")
  saucisse = container10.text_input("valeur de l'hypotenus")
  if saucisse == stl.session_state["hypotenus"]:
    container10.write("vous avez reussi !")
    container10.balloons()
