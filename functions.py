from pymol import cmd
from pymol import math
import numpy

id=1
#---------------------------------------------
#           variablen
#---------------------------------------------
def pseudoAtoms():
    cmd.pseudoatom("pseudoX", pos=[1,0,0])
    cmd.pseudoatom("pseudoY", pos=[0,1,0])
    cmd.pseudoatom("pseudoZ", pos=[0,0,1])
    cmd.pseudoatom("oreo", pos=[0,0,0])
    cmd.color("pink", "pseudoX")
    cmd.color("pink", "pseudoY")
    cmd.color("pink", "pseudoZ")

#------Load File------------------
def loadFile(FileName):
    cmd.reinitialize()
    cmd.load(FileName)

#---------------------------------------------
#           selections
#---------------------------------------------

#-----select Nitrogen ring---------
def selectNitrogen():
    cmd.select ("Nitrogen", "e. N",1)
    cmd.select("Hydr", "e. H")
    cmd.select("Hydr_neighbor", "neighbor Hydr")
    cmd.select("nitrogen_NH", "Nitrogen and Hydr_neighbor")
    cmd.select("nitrogen_N", "Nitrogen and not nitrogen_NH")
    cmd.select("newC", "(neighbor nitrogen_N) and (neighbor nitrogen_NH) ")

#-----select Halogen --------------
def selectHalogen():
    cmd.select("Halogen", "e. Cl or e. Br or e. I")
    cmd.select("current_neighbor", "neighbor Halogen")
    cmd.select("second_neighbor", "(neighbor current_neighbor) and not Halogen")
    model_neighbor=cmd.get_model("second_neighbor")
    for atom in model_neighbor.atom:
        cmd.select("second_atom", "id %s and ibenz"%(atom.id))

#---------------------------------------------
#           orientate
#---------------------------------------------

#------get Coords from Atoms--------
def getCoords(AtomName):
    model = cmd.get_model(AtomName)
    coords = []
    for atom in model.atom:
        coords = atom.coord
    return coords

#-------- move in Origin-----------
def moveOrigin(AtomName,FileName):
    execfile("axes.py")
    NewCoords = getCoords(AtomName)
    cmd.translate([NewCoords[0]*(-1), NewCoords[1]*(-1), NewCoords[2]*(-1)],FileName)

#---------------------------------------------
#           orientate Halogen
#---------------------------------------------
def orientateHalogen(FileName):
    selectHalogen()
    moveOrigin("Halogen",FileName)
    rotateY(FileName,angleY("current_neighbor","pseudoX"),"current_neighbor")
    rotateZ(FileName,angleZ("current_neighbor","pseudoY"),"current_neighbor")
    rotateY(FileName,angleY("second_atom","pseudoX"),"second_atom")
#---------------------------------------------
#           orientate Nitrogen
#---------------------------------------------
def orientateNitrogen(FileName):
    selectNitrogen()
    moveOrigin("nitrogen_N",FileName)
    rotateY(FileName,angleY("nitrogen_NH","pseudoZ"),"nitrogen_NH")
    rotateX(FileName,angleX("nitrogen_NH"),"nitrogen_NH")
    rotateZ(FileName,angleZ("newC","pseudoX"),"newC")

#---------------------------------------------
#           calculate angle
#---------------------------------------------
#-------- calculate angle for Y rotation -----
def angleY(MoleculeName,axis):
    co=getCoords(MoleculeName)
    name = "pseudo_%s"%(MoleculeName)
    cmd.pseudoatom(name, pos=[co[0],0,co[2]])
    angleY=cmd.get_angle(name,"oreo",axis,0)
    if co[2]<0:
        return(-angleY)
    else:
        return(angleY)


    return(cmd.get_angle(name,"oreo",axis,0))

#-------- calculate angle for Z rotation ------
def angleZ(MoleculeName,axis):
    angleZ = cmd.get_angle(MoleculeName,"oreo",axis,0)
    return(angleZ)

#-------- calculate angle for X rotation --------
def angleX(MoleculeName):
    co=getCoords(MoleculeName)
    angleX = cmd.get_angle(MoleculeName,"oreo","pseudoZ",0)
    if co[1]<0:
        return(-angleX)
    else:
        return(angleX)

#---------------------------------------------
#           rotate on axis
#---------------------------------------------
#--------rotate on y axis -------
def rotateY(FileName,angle,MoleculeName):
    cmd.rotate("y",angle,FileName,0,1,None,"0,0,0")

#-------- rotate for x axis -------
def rotateX(FileName,angle,MoleculeName):
    cmd.rotate("x",angle,FileName,0,1,None,"0,0,0")

#-------- rotate for y axis -------
def rotateZ(FileName,angle,MoleculeName):
    co=getCoords(MoleculeName)
    if co[0]<0:
        cmd.rotate("z", -angle,FileName,0,1,None,"0,0,0")
    else:
        cmd.rotate("z", angle,FileName,0,1,None,"0,0,0")

#---------------------------------------------
#           orientate Nitrogen
#---------------------------------------------
#-------- rotate X axis --------
def moveInXAxis (atomName1,atomName2,FileName):
    cmd.pseudoatom("pseudoX", pos=[1,0,0])
    cmd.color("white","pseudoX")
    angleX = cmd.get_angle(atomName1,atomName2,"pseudoX",0)
    cmd.rotate("z", angleX,FileName,0,1,None,"0,0,0")


#---------------------------------------------
#           create grid
#---------------------------------------------
def createGrid(length,width,height,steps,moleculeName):
    for i in numpy.arange(-width/float(2),(width+steps)/float(2),steps):
        for j in numpy.arange(-length/float(2),(length+steps)/float(2),steps):
            cmd.copy("ID:%s_l:%sw:%s"%(id,j,i),moleculeName)
            cmd.translate([i,height,j],"ID:%s_l:%sw:%s"%(id,j,i))
    global id
    id +=1
#---------------------------------------------
#           rotation for grid
#---------------------------------------------
def rotateAll(x,y,z,FileName):
    cmd.rotate("x",x,FileName,0,1,None,"0,0,0")
    cmd.rotate("y",y,FileName,0,1,None,"0,0,0")
    cmd.rotate("z",z,FileName,0,1,None,"0,0,0")
