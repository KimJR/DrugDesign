from functions import *
from pymol import cmd
cmd.reinitialize()

#___________set Filename______________________
#Filename1: bottom molecule
#Filename2: halogen molecule
#pathToSave
#fileType
Filename1 = "Mol2/imidazol.mol2"
Filename2 = "Mol2/ibenz.mol2"
fileType  = "mol2"
pathToSave = "Results"

#___________choose the function_____________
# |1|: own Grid with own angles
#-> you need to set GRID AND ROTATION values!
#
# |2|: automate Grid
#-> you need to set GRID and ANGLESTEP values!
#
# |3|: random Grid with random angles
#-> you don't need to set values!
choice=1

#___________set regular grid values___________
#length: z-axis
#width:  x-axis
#height: y-axis
#x: rotation on x-axis
#y: rotation on y-axis
#z: rotation on z-axis
#set 0 if no rotation on axis is needed

#-Grid-:
length=7
width=7
height=3
gridSteps=2

#-Rotation-:
x=0
y=0
z=0

angleSteps=30 # Grad

#___________functions call____________________
try:
    grid=[length,width,height,gridSteps]
    rotation=[x,y,z]
    cmd.load(Filename1)
    choose(Filename1,Filename2,grid,rotation,pathToSave,fileType, angleSteps,choice)
except:
    e = sys.exc_info()[0]
    print("Error: %s and message: %s" %(e,e.message))
