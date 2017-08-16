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

#----------y rotation--------
cmd.pseudoatom("pseudoX", pos=[1,0,0])
co1 = getCoords("pseudoX")
cmd.pseudoatom("pseud", pos=[co2[0],0,co2[2]])
co2 = getCoords("current_neighbor")
angle = cmd.angle("bla","pseud","Halogen","pseudoX")
angle2 = cmd.angle("bla2","Halogen","current_neighbor","pseud")
print co2
print angle2

rotateMatrixY("ibenz",180-angle)
#cmd.pseudoatom("pseudoY", pos=[0,1,0])
#co1 = getCoords("pseudoX")
#co2 = getCoords("current_neighbor")
#cmd.pseudoatom("pseud", pos=[co2[0],0,co2[2]])
co3 = getCoords("current_neighbor")
angle3 = math.degrees(math.atan2(co3[1],co3[0]))
print angle3

#rotateMatrixZ("ibenz",-angle2)
print getCoords("current_neighbor")
#print getCoords("current_neighbor")

#up = (co1[0]*co2[0])+(co1[1]*co2[1])+(co1[2]*co2[2])
#bot1 = math.sqrt(co1[0]**2+co1[1]**2+co1[2]**2)
#bot2 = math.sqrt(co2[0]**2+co2[1]**2+co2[2]**2)
#r = math.sqrt(co2[0]**2+co2[1]**2+co2[2]**2)
#bot2 = co2[0]/(math.sqrt(co2[0]**2+co2[1]**2))
#print bot2
#ang = math.degrees(math.acos(bot2))
#print ang
#wink =
#bot = up/(bot1*bot2)
#ang = math.degrees(math.acos(bot))
#print ang
#print  "co1: "+str(co1)
#print "co2: "+str(co2)
