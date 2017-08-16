from functions import *
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
<<<<<<< HEAD
rotateMatrixY("ibenz",138.351031052)
#138.351031052
print("nach 1. Drehen: "+str(getCoords("current_neighbor")))
rotateMatrixZ("ibenz",140)
print("nach 2. Drehen: "+str(getCoords("current_neighbor")))
=======
#rotateY("current_neighbor","Halogen","ibenz")
#print("nach 1. Drehen: "+str(getCoords("current_neighbor")))
#rotateZ("current_neighbor","Halogen","ibenz")
#print("nach 2. Drehen: "+str(getCoords("current_neighbor")))
>>>>>>> 965325e1c8c616d53940654c5a967d566c5c6205
