from functions import *
from pymol import cmd

cmd.reinitialize()


#___________set Filename______________________
#*********************************************
#Filename1: bottom molecule
#Filename2: halogen molecule
Filename2="imidazol.mol2"
cmd.load(Filename2)
pseudoAtoms()
selectNitrogen()
moveOrigin("nitrogen_N","imidazol")

cmd.rotate("y",-39,"imidazol",0,1,None,"0,0,0")
cmd.rotate("x",33,"imidazol",0,1,None,"0,0,0")
cmd.rotate("z",120,"imidazol",0,1,None,"0,0,0")
orientateNitrogen(Filename2[:-5])
