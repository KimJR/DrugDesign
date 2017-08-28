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
    cmd.pseudoatom("pseudoXZ", pos=[1,0,1])
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
    cn=getCoords("current_neighbor")
    if(cn[0]>0):
        rotateY(FileName,-angleY("current_neighbor","pseudoZ"),"current_neighbor")
    else:
        rotateY(FileName,angleY("current_neighbor","pseudoZ"),"current_neighbor")

    rotateX(FileName,-angleX("current_neighbor","pseudoY"),"current_neighbor")
    sa=getCoords("second_atom")
    if(sa[2]>0):
        rotateY(FileName,angleY("second_atom","pseudoX"),"second_atom")
    else:
        rotateY(FileName,-angleY("second_atom","pseudoX"),"second_atom")
#---------------------------------------------
#           orientate Nitrogen
#---------------------------------------------
def orientateNitrogen(FileName):
    selectNitrogen()
    moveOrigin("nitrogen_N",FileName)

    if(getCoords("nitrogen_NH")[0]>0):
        rotateY(FileName,-angleY("nitrogen_NH","pseudoZ"),"nitrogen_NH")
    else:
        rotateY(FileName,angleY("nitrogen_NH","pseudoZ"),"nitrogen_NH")
    if(getCoords("nitrogen_NH")[1]>0):
        rotateX(FileName,angleX("nitrogen_NH","pseudoZ"),"nitrogen_NH")
    else:
        rotateX(FileName,-angleX("nitrogen_NH","pseudoZ"),"nitrogen_NH")

    if(getCoords("newC")[1]>0):
        rotateZ(FileName,-cmd.get_angle("pseudoXZ","pseudoZ","newC",0),"newC")
    else:
        rotateZ(FileName,cmd.get_angle("pseudoXZ","pseudoZ","newC",0),"newC")
#---------------------------------------------
#           calculate angle
#---------------------------------------------
#-------- calculate angle for Y rotation -----
def angleY(MoleculeName,axis):
    co=getCoords(MoleculeName)
    name = "pseudo_%s"%(MoleculeName)
    cmd.pseudoatom(name, pos=[co[0],0,co[2]])
    angleY=cmd.get_angle(name,"oreo",axis,0)
    return(angleY)
#-------- calculate angle for Z rotation ------
def angleZ(MoleculeName,axis):
    angleZ = cmd.get_angle(MoleculeName,"oreo",axis,0)
    return(angleZ)
#-------- calculate angle for X rotation --------
def angleX(MoleculeName,axis):
    angleX = cmd.get_angle(MoleculeName,"oreo",axis,0)
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
    cmd.rotate("z", angle,FileName,0,1,None,"0,0,0")
#---------------------------------------------
#           create grid
#---------------------------------------------
def createGrid(grid,rotation,moleculeName):
    cmd.copy("copy_%s" %id,moleculeName)
    rotateAll(rotation[0],rotation[1],rotation[2],"copy_%s" %id)
    for i in numpy.arange(-grid[1]/float(2),(grid[1]+grid[3])/float(2),grid[3]):
        for j in numpy.arange(-grid[0]/float(2),(grid[0]+grid[3])/float(2),grid[3]):
            cmd.copy("ID:%s_x_%s_y_%s_z_%s_l:%sw:%s"%(id,rotation[0],rotation[1],rotation[2],j,i),"copy_%s" %id)
            cmd.translate([i,grid[2],j],"ID:%s_x_%s_y_%s_z_%s_l:%sw:%s"%(id,rotation[0],rotation[1],rotation[2],j,i))
    cmd.delete("copy_%s" %id)
    global id
    id +=1

#---------------------------------------------
#           rotation for grid
#---------------------------------------------
def rotateAll(x,y,z,FileName):
    cmd.rotate("z",z,FileName,0,1,None,"0,0,0")
    cmd.rotate("x",x,FileName,0,1,None,"0,0,0")
    cmd.rotate("y",y,FileName,0,1,None,"0,0,0")



#---------------------------------------------
#           create automate grid
#---------------------------------------------
def automationGrid(grid,step,moleculeName):
    for y in numpy.arange(-90,90+step,step):
        for x in numpy.arange(-60,60+step,step):
            for z in numpy.arange(-60,60+step,step):
                createGrid(grid,[x,y,z],moleculeName)

#---------------------------------------------
#           delete function
#---------------------------------------------
def deleteFunction():
    cmd.delete("pseudoX")
    cmd.delete("pseudoY")
    cmd.delete("pseudoZ")
    cmd.delete("pseudoXZ")
    cmd.delete("oreo")
