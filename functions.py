# -- coding: cp1252 --
from pymol import cmd
from pymol import math
import numpy
import random
import matplotlib
import matplotlib.pyplot as plt
#matplotlib.use('TkAgg')
#from matplotlib.backends import backend_tkagg
#matplotlib.get_backend()
#'Qt4Agg'

id=1
#---------------------------------------------
#           variablen
#---------------------------------------------
def pseudoAtoms():
    cmd.pseudoatom("pseudoX", pos=[1,0,0])
    cmd.pseudoatom("pseudoY", pos=[0,1,0])
    cmd.pseudoatom("pseudoZ", pos=[0,0,1])
    cmd.pseudoatom("pseudoXZ", pos=[1,0,1])
    cmd.pseudoatom("Oreo", pos=[0,0,0])
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
    cmd.select ("Nitrogen", "e. N")
    cmd.select("Hydr", "e. H")
    cmd.select("HydrNeighbor", "neighbor Hydr")
    cmd.select("NitrogenNH", "Nitrogen and HydrNeighbor")
    cmd.select("NitrogenN", "Nitrogen and not NitrogenNH")
    cmd.select("CAtom", "(neighbor NitrogenN) and (neighbor NitrogenNH) ")
#-----select Halogen --------------
def selectHalogen():
    cmd.select("Halogen", "e. Cl or e. Br or e. I")
    cmd.select("FirstNeighbor", "neighbor Halogen")
    cmd.select("SecondNeighbor", "(neighbor FirstNeighbor) and not Halogen")
    model_neighbor=cmd.get_model("SecondNeighbor")
    for atom in model_neighbor.atom:
        cmd.select("SecondAtom", "id %s and ibenz"%(atom.id))
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
    NewCoords = getCoords(AtomName)
    cmd.translate([NewCoords[0]*(-1), NewCoords[1]*(-1), NewCoords[2]*(-1)],FileName)
#---------------------------------------------
#           orientate Halogen
#---------------------------------------------
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
#---------------------------------------------
#           orientate Nitrogen
#---------------------------------------------
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
        rotateZ(FileName,-cmd.get_angle("pseudoXZ","pseudoZ","CAtom",0),"CAtom")
    else:
        rotateZ(FileName,cmd.get_angle("pseudoXZ","pseudoZ","CAtom",0),"CAtom")
#---------------------------------------------
#           calculate angle
#---------------------------------------------
#-------- calculate angle for Y Rotation -----
def angleY(MoleculeName,Axis):
    co=getCoords(MoleculeName)
    name = "pseudo_%s"%(MoleculeName)
    cmd.pseudoatom(name, pos=[co[0],0,co[2]])
    angleY=cmd.get_angle(name,"Oreo",Axis,0)
    cmd.delete(name)
    return(angleY)
#-------- calculate angle for Z Rotation ------
def angleZ(MoleculeName,Axis):
    angleZ = cmd.get_angle(MoleculeName,"Oreo",Axis,0)
    return(angleZ)
#-------- calculate angle for X Rotation --------
def angleX(MoleculeName,Axis):
    angleX = cmd.get_angle(MoleculeName,"Oreo",Axis,0)
    return(angleX)
#---------------------------------------------
#           rotate on axis
#---------------------------------------------
#--------rotate on y axis -------
def rotateY(FileName,Angle,MoleculeName):
    cmd.rotate("y",Angle,FileName,0,1,None,"0,0,0")
#-------- rotate for x axis -------
def rotateX(FileName,Angle,MoleculeName):
    cmd.rotate("x",Angle,FileName,0,1,None,"0,0,0")
#-------- rotate for y axis -------
def rotateZ(FileName,Angle,MoleculeName):
    cmd.rotate("z", Angle,FileName,0,1,None,"0,0,0")
#---------------------------------------------
#           create grid
#---------------------------------------------
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

#---------------------------------------------
#           Rotation for grid
#---------------------------------------------
def rotateAll(x,y,z,FileName):
    cmd.rotate("z",z,FileName,0,1,None,"0,0,0")
    cmd.rotate("x",x,FileName,0,1,None,"0,0,0")
    cmd.rotate("y",y,FileName,0,1,None,"0,0,0")

#---------------------------------------------
#           create automate grid
#---------------------------------------------
def automationGrid(Grid,Step,MoleculeName,BotMol,PathToSave,FileType):
    for y in numpy.arange(-90,90+Step,Step):
        for x in numpy.arange(-60,60+Step,Step):
            for z in numpy.arange(-60,60+Step,Step):
                createGrid(Grid,[x,y,z],MoleculeName,BotMol,PathToSave,FileType)

#---------------------------------------------
#           random automate grid
#---------------------------------------------

def randomGrid(Grid,MoleculeName,BotMol,PathToSave,FileType):
#    rand = random.randint(100,150)
    rand = random.randint(2,30)
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

def analyse(values):
    print " x: "+str(values[0])
    print " y: "+str(values[1])
    print " z: "+str(values[2])
    x = numpy.arange(0,values[3])
    m = [numpy.average(values[0]) for i in values[0]]
    fig,ax = plt.subplots()
    plt.xlabel('number of simulations')
    plt.ylabel('rotation degree')
    plt.title('xRotation')
    plt.grid(True)
    print m
    ax.scatter(x,values[0],label='data',marker='o')
    ax.plot(x,m,label='mean')
    ax.legend(loc='upper right')
    plt.savefig("xRotation.png")
#    plt.scatter(numpy.arange(0,values[3]),values[1])
#    plt.savefig("yRotation.png")
#    plt.scatter(numpy.arange(0,values[3]),values[2])
#    plt.savefig("zRotation.png")
    print "Average x-rotation:"+str(numpy.average(values[0]))
    print "Average y-rotation:"+str(numpy.average(values[1]))
    print "Average z-rotation:"+str(numpy.average(values[2]))
#    plt.show()




# def _new_figure_manager(num, *args, **kwargs):
#     if pymol._ext_gui is None:
#         return new_figure_manager(num, *args, **kwargs)
#     backend_tkagg.show._needmain = False
#     import Tkinter as Tk
#     from matplotlib.figure import Figure
#     from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureManagerTkAgg
#     FigureClass = kwargs.pop('FigureClass', Figure)
#     print kwargs
#     figure = FigureClass(*args, **kwargs)
#     window = Tk.Toplevel(master=pymol._ext_gui.root)
#     canvas = FigureCanvasTkAgg(figure, master=window)
#     figManager = FigureManagerTkAgg(canvas, num, window)
#     if matplotlib.is_interactive():
#         figManager.show()
#     return figManager
#     new_figure_manager = backend_tkagg.new_figure_manager
#     backend_tkagg.new_figure_manager = _new_figure_manager



#---------------------------------------------
#           delete function
#---------------------------------------------
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
