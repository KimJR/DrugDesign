from functions import *
from pymol import cmd

cmd.reinitialize()


#---------------------------------------------
#           load and select
#---------------------------------------------
cmd.load("ibenz.mol2")
selectHalogen()
#-------- move in Origin-----------
moveOrigin("Halogen","ibenz")
#-------- rotate-----------
rotateMatrixY("ibenz",138.351031052)
#138.351031052
print("nach 1. Drehen: "+str(getCoords("current_neighbor")))
rotateMatrixZ("ibenz",140)
print("nach 2. Drehen: "+str(getCoords("current_neighbor")))
