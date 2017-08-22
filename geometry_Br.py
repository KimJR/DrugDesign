from functions import *
from pymol import cmd

cmd.reinitialize()
try:

#___________set Filename______________________
#*********************************************
#Filename1: bottom molecule
#Filename2: halogen molecule
Filename1="imidazol.mol2"
Filename2="ibenz.mol2"

cmd.load(Filename1)
cmd.load(Filename2)
pseudoAtoms()
orientateHalogen(Filename2[:-5])
orientateNitrogen(Filename1[:-5])

#*********************************************

#___________rotate molecule for grid__________
#*********************************************
#angleX: rotation on x-axis
#angleY: rotation on y-axis
#angleZ: rotation on z-axis
#set 0 if no rotation on axis is needed
angleX=0
angleY=0
angleZ=0

rotateAll(angleX,angleY,angleZ,Filename2[:-5])
#*********************************************

#___________set regular grid values___________
#*********************************************
#length z-axis | width x-axis | height y-axis
length=10
width=10
height=2
steps=0.5

createGrid(length,width,height,steps,Filename2[:-5])
#*********************************************


except:
    e = sys.exc_info()[0]
    print "Error: %s" %e
