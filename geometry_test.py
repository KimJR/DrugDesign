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
x=20
y=0
z=0
rotation=[x,y,z]
rotation2=[-20,5,0]
grid=[length,width,height,steps]
#*********************************************

#___________functions call____________________
#*********************************************
cmd.load(Filename2)
cmd.load(Filename1)
pseudoAtoms()

try:
    orientateHalogen(Filename2[:-5])
    orientateNitrogen(Filename1[:-5])
    #createGrid(grid,rotation,Filename2[:-5])
    automationGrid(grid,30,Filename2[:-5])


except:
    e = sys.exc_info()[0]
#    print "Error: %s and message: %s" %(e,e.message)
