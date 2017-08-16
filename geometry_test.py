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
#cmd.pseudoatom("pseudoY", pos=[0,1,0])
#co1 = getCoords("pseudoY")
#co2 = getCoords("current_neighbor")
#up = (co1[0]*co2[0])+(co1[1]*co2[1])+(co1[2]*co2[2])
#bot1 = math.sqrt(co1[0]**2+co1[1]**2+co1[2]**2)
#bot2 = math.sqrt(co2[0]**2+co2[1]**2+co2[2]**2)
#bot = up/(bot1*bot2)
#ang = math.degrees(math.acos(bot))
cmd.pseudoatom("pseudoX", pos=[1,0,0])
co1 = getCoords("pseudoX")
co2 = getCoords("current_neighbor")
up = (co1[0]*co2[0])+(co1[1]*co2[1])+(co1[2]*co2[2])
#bot1 = math.sqrt(co1[0]**2+co1[1]**2+co1[2]**2)
bot2 = math.sqrt(co2[0]**2+co2[1]**2+co2[2]**2)
#wink =
#bot = up/(bot1*bot2)
#ang = math.degrees(math.acos(bot))
#print ang
#print  "co1: "+str(co1)
#print "co2: "+str(co2)
#-------- rotate-----------
#rotateY("current_neighbor","Halogen","ibenz")
#print("nach 1. Drehen: "+str(getCoords("current_neighbor")))
#rotateZ("current_neighbor","Halogen","ibenz")
#print("nach 2. Drehen: "+str(getCoords("current_neighbor")))
