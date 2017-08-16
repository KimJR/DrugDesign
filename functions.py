from pymol import cmd
from pymol import math

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

#def orientate(AtomName1):
    #first rotation y-axis with 2.atom
    #getCoords(Atomname1)
    #if


#-------- rotateMatrix for Z axis --------
def rotateMatrixZ(FileName,alpha):
    rotMat=[ math.cos(alpha),-math.sin(alpha),0,0,
             math.sin(alpha),math.cos(alpha),0,0,
             0,0,1,0,
             0,0,0,1]
    cmd.transform_selection(FileName, rotMat, homogenous=0)

#-------- rotateMatrix for Y axis --------
def rotateMatrixY(FileName, alpha):
    #cmd.pseudoatom("pseudoX", pos=[1,0,0])
    #color("yellow", "pseudoX")
    #angleY = cmd.get_angle(AtomName1,AtomName2,"pseudoX",0)
    rotMat=[math.cos(alpha),0,math.sin(alpha),0,0,1,0,0,
    -math.sin(alpha),0,math.cos(alpha),0,
    0,0,0,1]
    cmd.transform_selection(FileName,rotMat, homogenous=0)


#-------- rotateMatrix X axis --------
def rotateMatrixX(FileName,alpha):
    crotMat=[ 1,0,0,0,
             0,math.cos(alpha),-math.sin(alpha),0,
             0,math.sin(alpha),math.cos(alpha),0,
             0,0,0,1]
    cmd.transform_selection(FileName, rotMat, homogenous=0)



#---------------------------------------------
#           orientate Nitrogen
#---------------------------------------------
#-------- rotate X axis --------
def moveInXAxis (atomName1,atomName2,FileName):
<<<<<<< HEAD
    cmd.pseudoatom("pseudoX", pos=[1,0,0])
    cmd.color("white","pseudoX")
    angleX = cmd.get_angle(atomName1,atomName2,"pseudoX",0)
    cmd.rotate("z", angleX,FileName,0,1,None,"0,0,0")


#---------------------------------------------
#           create grid
#---------------------------------------------

=======
    #cmd.pseudoatom("pseudoX", pos=[1,0,0])
    #cmd.color("white","pseudoX")
        angleX = cmd.get_angle(atomName1,atomName2,"pseudoX",0)
        cmd.rotate("z", angleX,FileName,0,1,None,"0,0,0")
>>>>>>> 965325e1c8c616d53940654c5a967d566c5c6205
#-------Move on x-y-z-axis------------------
def move(FileName,AtomName,x,y,z):
    NewCoords = getCoords(AtomName)
    cmd.translate([NewCoords[0]+x,NewCoords[1]+y,NewCoords[2]+z],FileName)
