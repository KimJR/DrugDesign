from functions import *
from pymol import cmd

cmd.reinitialize()


#___________set Filename______________________
#*********************************************
#Filename1: bottom molecule
#Filename2: halogen molecule
Filename1="imidazol.mol2"
Filename2="ibenz.mol2"
#*********************************************



#___________set regular grid values___________
#*********************************************
#length z-axis | width x-axis | height y-axis
length=3
width=3
height=2
steps=0.5
#*********************************************

#___________functions call____________________
#*********************************************
cmd.load(Filename1)
cmd.load(Filename2)
<<<<<<< HEAD
=======
=======
#---------------------------------------------
#           load and select
#---------------------------------------------
cmd.load("ibenz.mol2")
selectHalogen()
#-------- move in Origin-----------
moveOrigin("Halogen","ibenz")
#cmd.pseudoatom("pseudoY", pos=[0,1,0])
#co1 = getCoords("pseudoY")
co2 = getCoords("current_neighbor")
#up = (co1[0]*co2[0])+(co1[1]*co2[1])+(co1[2]*co2[2])
#bot1 = math.sqrt(co1[0]**2+co1[1]**2+co1[2]**2)
#bot2 = math.sqrt(co2[0]**2+co2[1]**2+co2[2]**2)
#bot = up/(bot1*bot2)
#ang = math.degrees(math.acos(bot))

#----------y rotation--------
cmd.pseudoatom("pseudoX", pos=[1,0,0])
cmd.pseudoatom("pseud", pos=[co2[0],0,co2[2]])
angle = cmd.angle("bla","pseud","Halogen","pseudoX")
#angle = cmd.get_angle("pseud","Halogen","pseudoX",0)
cmd.rotate("y", angle,"ibenz",0,1,None,"0,0,0")
print "current_neighbor:"+str(getCoords("current_neighbor"))
# cmd.pseudoatom("pseudoY", pos=[0,1,0])
# #cmd.pseudoatom("pseud", pos=[co2[0],0,co2[2]])
# angle2 = cmd.angle("bla2","current_neighbor","Halogen","pseudoY")
# #angle2 = cmd.get_angle("current_neighbor","Halogen","pseudoY",0)
# cmd.rotate("z", angle2,"ibenz",0,1,None,"0,0,0")
cmd.load("imidazol.mol2")
>>>>>>> e7adf6a655e28c1c3c41e1247a6d4b1dc2612b3a
>>>>>>> 13d1fecda62ee870f1b60ee719c9ad9b47c15809
pseudoAtoms()

try:
    orientateHalogen(Filename2[:-5])
    orientateNitrogen(Filename1[:-5])
#cmd.copy("cop",Filename2[:-5])
#rotateAll(-50,50,0,cop)
#createGrid(length,width,height,steps,"cop")
#rotateAll(20,0,20,cop)
#createGrid(length,width,height,steps,"cop")
except:
    e = sys.exc_info()[0]
#    print "Error: %s and message: %s" %(e,e.message)
<<<<<<< HEAD
=======
=======
    print "Error: %s" %e



#print angleY("current_neighbor")
#print angleY("second_atom")
#rotateY("ibenz",angleY("current_neighbor"),"current_neighbor")
#rotateZ("ibenz",angleZ("current_neighbor"))
#rotateY("ibenz",angleY("second_atom"),"second_atom")
#print("current_neigh:"+str(getCoords("current_neighbor")))
#
#
# #cmd.pseudoatom("pseud", pos=[co2[0],0,co2[2]])
#
# #angle2 = cmd.get_angle("current_neighbor","Halogen","pseudoY",0)
# #cmd.rotate("z", angle2,"ibenz",0,1,None,"0,0,0")
# #cmd.rotate("x", "15","ibenz",0,1,None,"0,0,0")
# #print "second_atom:"+str(getCoords("second_atom"))
# #print "halogen" + str(getCoords("Halogen"))
# #cmd.pseudoatom("pseudoXm", pos=[-1,0,0])
# #angle3 = cmd.angle("bla3","second_atom","Halogen","pseudoXm")
# #cmd.rotate("y", angle3,"ibenz",0,1,None,"0,0,0")
#
#
# co = getCoords("second_atom")
# cmd.pseudoatom("pseudz", pos=[co[0],0,co[2]])
# angle4 = cmd.angle("bla4","pseudz","Halogen","pseudoX")
# #angle4 = cmd.get_angle("pseudz","Halogen","pseudoX",0)
# cmd.rotate("y", angle4,"ibenz",0,1,None,"0,0,0")
# print"current_neighbor new:"+str(getCoords("current_neighbor"))
# print "second_atom new:"+str(getCoords("second_atom"))
# #print "halogen new:" + str(getCoords("Halogen"))
# #cmd.rotate("y", "180","ibenz",0,1,None,"0,0,0")
# #print getCoords("second_atom")
# #angle2 = cmd.angle("bla2","Halogen","current_neighbor","pseud")
# #print co2
# #print angle2
#
# cmd.load("imidazol.mol2")
# selectNitrogen()
# moveOrigin("Nitrogen","imidazol")
# co3 = getCoords("nitrogen_NH")
# cmd.pseudoatom("pseudoZ", pos=[0,0,1])
# cmd.pseudoatom("pseudz2", pos=[co3[0],0,co3[2]])
# print "nitrogen_NH: "+str(getCoords("nitrogen_NH"))
# angle5 = cmd.angle("bla","pseudz2","nitrogen_N","pseudoZ")
# # angle5 = cmd.get_angle("pseudz2","nitrogen_N","pseudoZm",0)
# #cmd.rotate("y", -angle5,"imidazol",0,1,None,"0,0,0")
# cmd.rotate("y", angle5,"imidazol",0,1,None,"0,0,0")
# # #-angle, da in die Rueckrichtung drehen, -z
# angle6 = cmd.angle("bla","nitrogen_NH","nitrogen_N","pseudoZ")
# # angle6 = cmd.get_angle("nitrogen_NH","nitrogen_N","pseudoZm",0)
# cmd.rotate("x", -angle6,"imidazol",0,1,None,"0,0,0")
# #print "nitrogen_NH new:"+str(getCoords("nitrogen_NH"))
# #co3 = getCoords("newC")
# #cmd.pseudoatom("pseudz2", pos=[co3[0],0,co3[2]])
# #
# #
# #
# #print "newC:" + str(getCoords("newC"))
# #cmd.pseudoatom("pseudoZ", pos=[0,0,1])
# angle7 = cmd.angle("bla5","newC","nitrogen_N","pseudoX")
# # angle7 = cmd.get_angle("newC","nitrogen_N","pseudoZ",0)
# # #angle7 = cmd.get_angle("newC","nitrogen_N","pseudoX",0)
# # cmd.rotate("x",-angle7,"imidazol",0,1,None,"0,0,0")
# cmd.rotate("z",angle7,"imidazol",0,1,None,"0,0,0")
# #
# #
# print "newC new:"+str(getCoords("newC"))
# print "nitrogen_NH new:"+str(getCoords("nitrogen_NH"))
# # #rotateMatrixY("ibenz",180-angle)
# # #cmd.pseudoatom("pseudoY", pos=[0,1,0])
# # #co1 = getCoords("pseudoX")
# # #co2 = getCoords("current_neighbor")
# # #cmd.pseudoatom("pseud", pos=[co2[0],0,co2[2]])
# # #co3 = getCoords("current_neighbor")
# # #angle3 = math.degrees(math.atan2(co3[1],co3[0]))
# # #print angle3
# #
# # #rotateMatrixZ("ibenz",-angle2)
# # #print getCoords("current_neighbor")
# # #print getCoords("current_neighbor")
# #
# # #up = (co1[0]*co2[0])+(co1[1]*co2[1])+(co1[2]*co2[2])
# # #bot1 = math.sqrt(co1[0]**2+co1[1]**2+co1[2]**2)
# # #bot2 = math.sqrt(co2[0]**2+co2[1]**2+co2[2]**2)
# # #r = math.sqrt(co2[0]**2+co2[1]**2+co2[2]**2)
# # #bot2 = co2[0]/(math.sqrt(co2[0]**2+co2[1]**2))
# # #print bot2
# # #ang = math.degrees(math.acos(bot2))
# # #print ang
# # #wink =
# # #bot = up/(bot1*bot2)
# # #ang = math.degrees(math.acos(bot))
# # #print ang
# # #print  "co1: "+str(co1)
# # #print "co2: "+str(co2)
# # #-------- move in Origin and orientate-----------
# # #orientate()
# # #print("nach 1. Drehen: "+str(getCoords("current_neighbor")))
# # #rotateMatrixZ("ibenz",69.799999999)
# # #print("nach 2. Drehen: "+str(getCoords("current_neighbor")))
# # #-------- rotate second atom-----------
# # #rotateMatrixY("ibenz",41.82)
# # #print("nach 3. Drehen: "+str(getCoords("second_atom")))
# =======
# co1 = getCoords("pseudoX")
# cmd.pseudoatom("pseud", pos=[co2[0],0,co2[2]])
# co2 = getCoords("current_neighbor")
# angle = cmd.angle("bla","pseud","Halogen","pseudoX")
# angle2 = cmd.angle("bla2","Halogen","current_neighbor","pseud")
# print co2
# print angle2
#
# rotateMatrixY("ibenz",180-angle)
# #cmd.pseudoatom("pseudoY", pos=[0,1,0])
# #co1 = getCoords("pseudoX")
# #co2 = getCoords("current_neighbor")
# #cmd.pseudoatom("pseud", pos=[co2[0],0,co2[2]])
# co3 = getCoords("current_neighbor")
# angle3 = math.degrees(math.atan2(co3[1],co3[0]))
# print angle3
#
# #rotateMatrixZ("ibenz",-angle2)
# print getCoords("current_neighbor")
# #print getCoords("current_neighbor")
#
# #up = (co1[0]*co2[0])+(co1[1]*co2[1])+(co1[2]*co2[2])
# #bot1 = math.sqrt(co1[0]**2+co1[1]**2+co1[2]**2)
# #bot2 = math.sqrt(co2[0]**2+co2[1]**2+co2[2]**2)
# #r = math.sqrt(co2[0]**2+co2[1]**2+co2[2]**2)
# #bot2 = co2[0]/(math.sqrt(co2[0]**2+co2[1]**2))
# #print bot2
# #ang = math.degrees(math.acos(bot2))
# #print ang
# #wink =
# #bot = up/(bot1*bot2)
# #ang = math.degrees(math.acos(bot))
# #print ang
# #print  "co1: "+str(co1)
# #print "co2: "+str(co2)
# #-------- move in Origin and orientate-----------
# orientate()
# #print("nach 1. Drehen: "+str(getCoords("current_neighbor")))
# #rotateMatrixZ("ibenz",69.799999999)
# #print("nach 2. Drehen: "+str(getCoords("current_neighbor")))
# #-------- rotate second atom-----------
# #rotateMatrixY("ibenz",41.82)
# #print("nach 3. Drehen: "+str(getCoords("second_atom")))
<<<<<<< HEAD
=======
# >>>>>>> c834b8b5f90e2111632581182bf5d809f2db7b73
>>>>>>> e7adf6a655e28c1c3c41e1247a6d4b1dc2612b3a
>>>>>>> 01c33289ff12a952cd2e2f0c68dfa35bb17287e3
>>>>>>> 13d1fecda62ee870f1b60ee719c9ad9b47c15809
