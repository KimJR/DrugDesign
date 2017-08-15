from functions import selectNitrogen
from functions import selectHalogen
from functions import moveOrigin
from functions import getCoords
from functions import rotateZ
from functions import rotateY
from functions import rotateX
from functions import move
from pymol import cmd

cmd.reinitialize()

#---------------------------------------------
#           load and select
#---------------------------------------------
cmd.load("imidazol.mol2")
selectNitrogen()
cmd.load("ibenz.mol2")
selectHalogen()
#---------------------------------------------
#           move to origin
#---------------------------------------------
moveOrigin("nitrogen_N","imidazol")
moveOrigin("Halogen","ibenz")
print("Halogen: "+str(getCoords("Halogen")))
print("Nitrogen: "+str(getCoords("nitrogen_N")))
#---------------------------------------------
#           rotate
#---------------------------------------------
print("before rotation: "+str(getCoords("current_neighbor")))
rotateY("current_neighbor","Halogen","ibenz")
print("after 1. rotation: "+str(getCoords("current_neighbor")))
rotateZ("current_neighbor","Halogen","ibenz")
print("after 2. rotation: "+str(getCoords("current_neighbor")))
#moveInZMinus("nitrogen_NH","nitrogen_N","imidazol")
#moveInXAxis("newC","nitrogen_N","imidazol")
#---------------------------------------------
#           move in x-y-z-axis
#---------------------------------------------
#move("ibenz","Halogen",4,0,6)
####
###

####
