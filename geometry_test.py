from functions import *
from pymol import cmd

cmd.reinitialize()


#___________set Filename______________________
#*********************************************
#Filename1: bottom molecule
#Filename2: halogen molecule
Filename1="imidazol.mol2"
Filename2="ibenz.mol2"
#*********************************************



#___________set regular grid values___________
#*********************************************
#length z-axis | width x-axis | height y-axis
length=3
width=3
height=2
steps=0.5
#*********************************************

#___________functions call____________________
#*********************************************
cmd.load(Filename1)
cmd.load(Filename2)
pseudoAtoms()

try:
    orientateHalogen(Filename2[:-5])
    orientateNitrogen(Filename1[:-5])
#cmd.copy("cop",Filename2[:-5])
#rotateAll(-50,50,0,cop)
#createGrid(length,width,height,steps,"cop")
#rotateAll(20,0,20,cop)
#createGrid(length,width,height,steps,"cop")
except:
    e = sys.exc_info()[0]
#    print "Error: %s and message: %s" %(e,e.message)
