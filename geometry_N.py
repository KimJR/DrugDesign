from functions import moveOrigin
from functions import getCoords
from functions import rotateZ
from functions import rotateY
from functions import rotateX
from functions import selectNitrogen
from functions import selectHalogen
from functions import move

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
rotateY("current_neighbor","Halogen","ibenz")
print("nach 1. Drehen: "+str(getCoords("current_neighbor")))
rotateZ("current_neighbor","Halogen","ibenz")
print("nach 2. Drehen: "+str(getCoords("current_neighbor")))
