from pymol import cmd
from pymol import math
import numpy
import random
import matplotlib
import matplotlib.pyplot as plt
id=1 #name id


#***********************************************************************
#           helper functions
#***********************************************************************

#___________call functions______________________________________________
#Funktionsaufrufe
def choose(Filename1,Filename2,grid,rotation,pathToSave,fileType, angleSteps,choice):
    loadFiles(Filename1,Filename2)
    if choice==1:
        createGrid(grid,rotation,Filename2[:-5],Filename1[:-5],pathToSave,fileType)
    if choice==2:
        automationGrid(grid,angleSteps,Filename2[:-5],Filename1[:-5],pathToSave,fileType)
    if choice==3:
        analyse(randomGrid(grid,Filename2[:-5],Filename1[:-5],pathToSave,fileType))

    deleteFunction()

#___________load Files__________________________________________________
def loadFiles(FileName1,FileName2):
    cmd.reinitialize()
    cmd.load(FileName1)
    cmd.load(FileName2)
    pseudoAtoms()
    orientateHalogen(FileName2[:-5])
    orientateNitrogen(FileName1[:-5])


#___________get coords from atoms_______________________________________
def getCoords(AtomName):
    model = cmd.get_model(AtomName)
    coords = []
    for atom in model.atom:
        coords = atom.coord
    return coords

#___________move in origin______________________________________________
def moveOrigin(AtomName,FileName):
    NewCoords = getCoords(AtomName)
    cmd.translate([NewCoords[0]*(-1), NewCoords[1]*(-1), NewCoords[2]*(-1)],FileName)

#___________define pseudoatoms__________________________________________
def pseudoAtoms():
    cmd.pseudoatom("pseudoX", pos=[1,0,0])
    cmd.pseudoatom("pseudoY", pos=[0,1,0])
    cmd.pseudoatom("pseudoZ", pos=[0,0,1])
    cmd.pseudoatom("pseudoXZ", pos=[1,0,1])
    cmd.pseudoatom("Oreo", pos=[0,0,0])
    cmd.color("pink", "pseudoX")
    cmd.color("pink", "pseudoY")
    cmd.color("pink", "pseudoZ")

#___________delete all unnecessary_______________________________________
def deleteFunction():
    cmd.delete("pseudoX")
    cmd.delete("pseudoY")
    cmd.delete("pseudoZ")
    cmd.delete("pseudoXZ")
    cmd.delete("Oreo")
    cmd.delete("SecondNeighbor")
    cmd.delete("Nitrogen")
    cmd.delete("Hydr")
    cmd.delete("HydrNeighbor")
    cmd.delete("Halogen")
    cmd.delete("FirstNeighbor")
    cmd.delete("SecondNeighbor")
    cmd.delete("SecondAtom")
    cmd.delete("NitrogenN")
    cmd.delete("NitrogenNH")
    cmd.delete("CAtom")



#***********************************************************************
#           selection and orientation functions
#***********************************************************************

#___________selection of Nitrogen_______________________________________
def selectNitrogen():
    cmd.select ("Nitrogen", "e. N")
    cmd.select("Hydr", "e. H")
    cmd.select("HydrNeighbor", "neighbor Hydr")
    cmd.select("NitrogenNH", "Nitrogen and HydrNeighbor")
    cmd.select("NitrogenN", "Nitrogen and not NitrogenNH")
    cmd.select("CAtom", "(neighbor NitrogenN) and (neighbor NitrogenNH) ")

#___________selection of Halogen________________________________________
def selectHalogen():
    cmd.select("Halogen", "e. Cl or e. Br or e. I")
    cmd.select("FirstNeighbor", "neighbor Halogen")
    cmd.select("SecondNeighbor", "(neighbor FirstNeighbor) and not Halogen")
    model_neighbor=cmd.get_model("SecondNeighbor")
    for atom in model_neighbor.atom:
        cmd.select("SecondAtom", "id %s and ibenz"%(atom.id))

#___________orientate Halogen___________________________________________
def orientateHalogen(FileName):
    selectHalogen()
    moveOrigin("Halogen",FileName)
    cn=getCoords("FirstNeighbor")
    if(cn[0]>0):
        rotateY(FileName,-angleY("FirstNeighbor","pseudoZ"),"FirstNeighbor")
    else:
        rotateY(FileName,angleY("FirstNeighbor","pseudoZ"),"FirstNeighbor")

    rotateX(FileName,-angleX("FirstNeighbor","pseudoY"),"FirstNeighbor")
    sa=getCoords("SecondAtom")
    if(sa[2]>0):
        rotateY(FileName,angleY("SecondAtom","pseudoX"),"SecondAtom")
    else:
        rotateY(FileName,-angleY("SecondAtom","pseudoX"),"SecondAtom")

#___________orientate Nitrogen__________________________________________
def orientateNitrogen(FileName):
    selectNitrogen()
    moveOrigin("NitrogenN",FileName)

    if(getCoords("NitrogenNH")[0]>0):
        rotateY(FileName,-angleY("NitrogenNH","pseudoZ"),"NitrogenNH")
    else:
        rotateY(FileName,angleY("NitrogenNH","pseudoZ"),"NitrogenNH")
    if(getCoords("NitrogenNH")[1]>0):
        rotateX(FileName,angleX("NitrogenNH","pseudoZ"),"NitrogenNH")
    else:
        rotateX(FileName,-angleX("NitrogenNH","pseudoZ"),"NitrogenNH")

    if(getCoords("CAtom")[1]>0):
        rotateZ(FileName,-angleZ("CAtom","pseudoZ"),"CAtom")
    else:
        rotateZ(FileName,angleZ("CAtom","pseudoZ"),"CAtom")

#___________calculate angle for y-rotation______________________________
def angleY(MoleculeName,Axis):
    co=getCoords(MoleculeName)
    name = "pseudo_%s"%(MoleculeName)
    cmd.pseudoatom(name, pos=[co[0],0,co[2]])
    angleY=cmd.get_angle(name,"Oreo",Axis,0)
    cmd.delete(name)
    return(angleY)
#___________calculate angle for z-rotation______________________________
def angleZ(MoleculeName,Axis):
    angleZ = cmd.get_angle("pseudoXZ",Axis,MoleculeName,0)
    return(angleZ)
#___________calculate angle for x-rotation______________________________
def angleX(MoleculeName,Axis):
    angleX = cmd.get_angle(MoleculeName,"Oreo",Axis,0)
    return(angleX)

#___________rotate on y-axis____________________________________________
def rotateY(FileName,Angle,MoleculeName):
    cmd.rotate("y",Angle,FileName,0,1,None,"0,0,0")
#___________rotate on x-axis____________________________________________
def rotateX(FileName,Angle,MoleculeName):
    cmd.rotate("x",Angle,FileName,0,1,None,"0,0,0")
#___________rotate on z-axis____________________________________________
def rotateZ(FileName,Angle,MoleculeName):
    cmd.rotate("z", Angle,FileName,0,1,None,"0,0,0")



#***********************************************************************
#           Grid functions
#***********************************************************************

#___________create Grid_________________________________________________
def createGrid(Grid,Rotation,MoleculeName,BotMol,PathToSave,FileType):
    cmd.copy("copy_%s" %id,MoleculeName)
    rotateAll(Rotation[0],Rotation[1],Rotation[2],"copy_%s" %id)
    for i in numpy.arange(-Grid[1]/float(2),(Grid[1]+Grid[3])/float(2),Grid[3]):
        for j in numpy.arange(-Grid[0]/float(2),(Grid[0]+Grid[3])/float(2),Grid[3]):
            cmd.create("ID_%s_x_%s_y_%s_z_%s_l_%sw_%s"%(id,Rotation[0],Rotation[1],Rotation[2],j,i),"copy_%s" %id)
            cmd.translate([i,Grid[2],j],"ID_%s_x_%s_y_%s_z_%s_l_%sw_%s"%(id,Rotation[0],Rotation[1],Rotation[2],j,i))
            cmd.select("sID_%s_x_%s_y_%s_z_%s_l_%sw_%s"%(id,Rotation[0],Rotation[1],Rotation[2],j,i),"ID_%s_x_%s_y_%s_z_%s_l_%sw_%s %s"%(id,Rotation[0],Rotation[1],Rotation[2],j,i,BotMol))
            cmd.create("mID_%s_x_%s_y_%s_z_%s_l_%sw_%s"%(id,Rotation[0],Rotation[1],Rotation[2],j,i),"sID_%s_x_%s_y_%s_z_%s_l_%sw_%s"%(id,Rotation[0],Rotation[1],Rotation[2],j,i))
            cmd.save("%s/_ID_%s_x_%s_y_%s_z_%s_l_%sw_%s.%s"%(PathToSave,id,Rotation[0],Rotation[1],Rotation[2],j,i,FileType),"mID_%s_x_%s_y_%s_z_%s_l_%sw_%s"%(id,Rotation[0],Rotation[1],Rotation[2],j,i))
            cmd.delete("sID_%s_x_%s_y_%s_z_%s_l_%sw_%s"%(id,Rotation[0],Rotation[1],Rotation[2],j,i))
            cmd.delete("mID_%s_x_%s_y_%s_z_%s_l_%sw_%s"%(id,Rotation[0],Rotation[1],Rotation[2],j,i))
    cmd.delete("copy_%s"%id)
    global id
    id +=1

#___________rotation for Grid___________________________________________
def rotateAll(x,y,z,FileName):
    cmd.rotate("z",z,FileName,0,1,None,"0,0,0")
    cmd.rotate("x",x,FileName,0,1,None,"0,0,0")
    cmd.rotate("y",y,FileName,0,1,None,"0,0,0")

#___________generate automation Grid_____________________________________
def automationGrid(Grid,angleStep,MoleculeName,BotMol,PathToSave,FileType):
    for y in numpy.arange(-90,90+angleStep,angleStep):
        for x in numpy.arange(-60,60+angleStep,angleStep):
            for z in numpy.arange(-60,60+angleStep,angleStep):
                createGrid(Grid,[x,y,z],MoleculeName,BotMol,PathToSave,FileType)

#___________generate random Grid_________________________________________
def randomGrid(Grid,MoleculeName,BotMol,PathToSave,FileType):
    rand = random.randint(10,20)
    randX = []
    randY = []
    randZ = []
    for i in numpy.arange(0,rand):
        x = random.randint(-60,60)
        y = random.randint(-90,90)
        z = random.randint(-60,60)
        createGrid(Grid,[x,y,z],MoleculeName,BotMol,PathToSave,FileType)
        randX.extend([x])
        randY.extend([y])
        randZ.extend([z])
    return([randX,randY,randZ,rand])

#___________generate analyse for random Grid_____________________________
def analyse(values):
    x = numpy.arange(1,values[3]+1)
    mx = [numpy.average(values[0]) for i in values[0]]
    m1 = [0 for i in values[0]]
    fig,ax = plt.subplots()
    plt.xlabel('number of simulations')
    plt.ylabel('rotation degree')
    plt.title('x rotation')
    plt.grid(True)
    plt.text(0.5,61,'mean = %s'%mx[0])
    plt.xticks(numpy.arange(0,values[3]+1,20))
    plt.yticks(numpy.arange(-65,65,5))
    ax.scatter(x,values[0],label='data',marker='o')
    ax.plot(x,mx,label='mean',linestyle='--',c='red')
    ax.plot(x,m1,label='zero',linestyle='solid',linewidth=2.5 ,c='black')
    ax.legend(loc='upper right')
    plt.savefig("xRotation.png")

    my = [numpy.average(values[1]) for i in values[1]]
    fig,ax = plt.subplots()
    plt.xlabel('number of simulations')
    plt.ylabel('rotation degree')
    plt.title('y rotation')
    plt.grid(True)
    plt.text(0.5,91,'mean = %s'%my[0])
    plt.xticks(numpy.arange(0,values[3]+1,20))
    plt.yticks(numpy.arange(-90,90,10))
    ax.scatter(x,values[1],label='data',marker='o')
    ax.plot(x,my,label='mean',linestyle='--',c='red')
    ax.plot(x,m1,label='zero',linestyle='solid',linewidth=2.5 ,c='black')
    ax.legend(loc='upper right')
    plt.savefig("yRotation.png")

    mz = [numpy.average(values[2]) for i in values[2]]
    fig,ax = plt.subplots()
    plt.xlabel('number of simulations')
    plt.ylabel('rotation degree')
    plt.title('z rotation')
    plt.grid(True)
    plt.text(0.5,61,'mean = %s'%mz[0])
    plt.xticks(numpy.arange(0,values[3]+1,20))
    plt.yticks(numpy.arange(-65,65,5))
    ax.scatter(x,values[2],label='data',marker='o')
    ax.plot(x,mz,label='mean',linestyle='--',c='red')
    ax.plot(x,m1,label='zero',linestyle='solid',linewidth=2.5 ,c='black')
    ax.legend(loc='upper right')
    plt.savefig("zRotation.png")
