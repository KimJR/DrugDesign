from functions import *
from pymol import cmd

cmd.reinitialize()

length=5
width=5
height=2
steps=0.5
x=20
y=0
z=0
#___________set Filename______________________
#*********************************************
#Filename1: bottom molecule
#Filename2: halogen molecule
try:
    Filename1 = "imidazol.mol2"
    Filename2 = "ibenz.mol2"
    cmd.load(Filename1)
    cmd.load(Filename2)
    pseudoAtoms()
    orientateHalogen(Filename2[:-5])
    orientateNitrogen(Filename1[:-5])

#*********************************************
#___________set regular grid values___________
#*********************************************
#length z-axis | width x-axis | height y-axis
#x: rotation on x-axis
#y: rotation on y-axis
#z: rotation on z-axis
#set 0 if no rotation on axis is needed
    rotation=[x,y,z]
    rotation2=[-20,0,0]
    rotation3=[120,50,0]
    grid=[length,width,height,steps]
    grid2=[length,width,-2,steps]
#    createGrid(grid,rotation,Filename2[:-5])
#    createGrid(grid,rotation2,Filename2[:-5])
#    createGrid(grid2,rotation3,Filename2[:-5])
    AutomationGrid(grid,rotation,Filename2[:-5],10)
except:
    e = sys.exc_info()[0]
    print "Error: %s" %e
#*********************************************
