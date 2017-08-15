from pymol import cmd
from pymol import math

#------Load File------------------
def loadFile(FileName):
    cmd.reinitialize()
    cmd.load(FileName)

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

#-------- rotate Z axis --------
def rotateZ(AtomName1,AtomName2,FileName):
    cmd.pseudoatom("pseudoY", pos=[0,1,0])
    cmd.color("hotpink", "pseudoY")
    angleZ = cmd.get_angle(AtomName1,AtomName2,"pseudoY",0)
    rotMat=[ math.cos(angleZ),-math.sin(angleZ),0,0,
             math.sin(angleZ),math.cos(angleZ),0,0,
             0,0,1,0,
             0,0,0,1]
    cmd.transform_selection(FileName, rotMat, homogenous=0)
    return(angleZ)

#-------- rotate Y axis --------
def rotateY(AtomName1,AtomName2,FileName):
    cmd.pseudoatom("pseudoX", pos=[1,0,0])
    cmd.color("yellow", "pseudoX")
    angleY = cmd.get_angle(AtomName1,AtomName2,"pseudoX",0)
    rotMat=[math.cos(angleY),0,math.sin(angleY),0,0,1,0,0,
    -math.sin(angleY),0,math.cos(angleY),0,
    0,0,0,1]
    cmd.transform_selection(FileName,rotMat, homogenous=0)
    return(angleY)

def rotateX(AtomName1,AtomName2,FileName):
    cmd.pseudoatom("pseudoZ", pos=[0,0,1])
    angleX = cmd.get_angle(AtomName1,AtomName2,"pseudoZ",0)
    crotMat=[ 1,0,0,0,
             0,math.cos(angleX),-math.sin(angleX),0,
             0,math.sin(angleX),math.cos(angleX),0,
             0,0,0,1]
    cmd.transform_selection(FileName, rotMat, homogenous=0)
    return(angleX)

def moveInXAxis (atomName1,atomName2,FileName):
    #cmd.pseudoatom("pseudoX", pos=[1,0,0])
    #cmd.color("white","pseudoX")
        angleX = cmd.get_angle(atomName1,atomName2,"pseudoX",0)
        cmd.rotate("z", angleX,FileName,0,1,None,"0,0,0")



#-------Move on x-y-z-axis------------------
def move(FileName,AtomName,x,y,z):
    NewCoords = getCoords(AtomName)
    cmd.translate([NewCoords[0]+x,NewCoords[1]+y,NewCoords[2]+z],FileName)
