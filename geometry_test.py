from functions import *
from pymol import cmd

cmd.reinitialize()


#---------------------------------------------
#           load and select
#---------------------------------------------
cmd.load("ibenz.mol2")
selectHalogen()
#-------- move in Origin and orientate-----------
orientate()
#print("nach 1. Drehen: "+str(getCoords("current_neighbor")))
#rotateMatrixZ("ibenz",69.799999999)
#print("nach 2. Drehen: "+str(getCoords("current_neighbor")))
#-------- rotate second atom-----------
#rotateMatrixY("ibenz",41.82)
#print("nach 3. Drehen: "+str(getCoords("second_atom")))
