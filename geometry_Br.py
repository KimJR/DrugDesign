# -- coding: cp1252 --
from functions import *
from pymol import cmd

cmd.reinitialize()

#___________set Filename______________________
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


#___________set regular grid values___________
#length z-axis | width x-axis | height y-axis
#x: rotation on x-axis
#y: rotation on y-axis
#z: rotation on z-axis
#set 0 if no rotation on axis is needed
    pathToSave = "/home/kim/save"
    fileType  = "mol2"
    length=2
    width=2
    height=2
    steps=1
    grid=[length,width,height,steps]
    x=20
    y=0
    z=0
    rotation=[x,y,z]
#    createGrid(grid,rotation,Filename2[:-5])
    automationGrid(grid,60,Filename2[:-5],Filename1[:-5],pathToSave,fileType)
    deleteFunction()
except:
    e = sys.exc_info()[0]
#    print "Error: %s and message: %s" %(e,e.message)
