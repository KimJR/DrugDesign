from functions import moveOrigin
from functions import getCoords
from functions import rotateZ
from functions import rotateY
from functions import rotateX
from functions import selectNitrogen
from functions import selectHalogen
from functions import move

from pymol import cmd
cmd.reinitialize()


#---------------------------------------------
#           load and select
#---------------------------------------------
cmd.load("ibenz.mol2")
selectHalogen()
#-------- move in Origin-----------
moveOrigin("Halogen","ibenz")
print(getCoords("Halogen"))

cmd.pseudoatom("pseudoX", pos=[1.0,0,0.0])
cmd.color("hotpink", "pseudoX")
angleX = cmd.angle("Angle1","current_neighbor","Halogen","pseudoX")
print("vor Drehen: "+str(getCoords("current_neighbor")))
print(angleX)
rotMat=[  math.cos(angleX),0,math.sin(angleX),0,
          0,1,0,0,
          0,0,1,0,            #-math.sin(angleX),0,math.cos(angleX),0,
          0,0,0,1]
cmd.transform_selection("ibenz", rotMat, homogenous=0)
print rotMat
#-----------zachse--------------
#cmd.pseudoatom("pseudoY", pos=[0,1,0])
#cmd.color("hotpink", "pseudoY")
#angleY = cmd.angle("Angle2","current_neighbor","Halogen","pseudoY")
print("nach Drehen: "+str(getCoords("current_neighbor")))
#print(angleY)
#rotMat=[  math.cos(angleY),-math.sin(angleY),0,0,
#          math.sin(angleY),math.cos(angleY),0,0,
#          0,0,1,0,
#          0,0,0,1]
#cmd.transform_selection("ibenz", rotMat, homogenous=0)
#print rotMat

#cmd.pseudoatom("pseudoX", pos=[1.0,0.0,0.0])
#angleY = cmd.get_angle("second_atom","Halogen","pseudoX",0)
#rotMat2=[math.cos(angleY),0,math.sin(angleY),0,
#          0,1,0,0,
#          -math.sin(angleY),0,math.cos(angleY),0,
#          0,0,0,1]
#cmd.transform_selection("ibenz", rotMat2, homogenous=0)
#print(getCoords("second_atom"))
