from functions import selectNitrogen
from functions import selectHalogen
from functions import moveOrigin
from functions import getCoords
from functions import rotateZ
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
#rotateZ("current_neighbor","Halogen","ibenz")
#print("atom2: "+str(getCoords("current_neighbor")))
#print("atom1: "+str(getCoords("Halogen")))
#rotateY("second_atom","current_halogen","ibenz")
#rotateX("second_atom","current_neighbor","ibenz")
#print("atom2: "+str(getCoords("current_neighbor")))
#print("atom1: "+str(getCoords("second_atom")))
#moveInZMinus("nitrogen_NH","nitrogen_N","imidazol")
#moveInXAxis("newC","nitrogen_N","imidazol")
#---------------------------------------------
#           move in x-y-z-axis
#---------------------------------------------
#move("ibenz","Halogen",4,0,6)
####
###

####
