# Computational Methods in Drug Discovery

**Lab for Molecular Design & Pharmaceutical Biophysics  
Institute of Pharmaceutical Sciences in the group of  **

This repository contains the work of my internship in 2017 as part of my undergraduate studies in Bioinformatics at the University of Tübingen, Germany supervised by Dr. Dr. Markus Zimmermann. 

- - - - - - - - - -

## Content
The script is a Python script written for the **PyMOL by Schrödinger** program. The script expects 2 files of the type mol2, a halogen and a nitrogen as input. In the first step, these two molecules are rotated and aligned around the axes x, y and z by selecting individual atoms. A copy of the halogen is then created and a grid is later created from this copy. The halogen is copied again several times and placed at the grid points. 
![Alt-Text](/Results/Grid.png =100x20)
These grid points can be entered manually or generated randomly. Then the coordinates and points of the halogen copies are saved in a.mol2 file. For the randomized grid generation, a statistical evaluation of the angles of rotation around the axes is also shown in a plot in order to see the distribution
### PyMOL
https://pymol.org/2/  
PyMOL is a user-sponsored molecular visualization system on an open-source foundation, maintained and distributed by Schrödinger.

### Input Parameters
```
Filename1 = "file1.mol2" 
Filename2 = "file2.mol2"
pathToSave = "/Results"
fileType  = "mol2"
```

### Included packages
```
from pymol import cmd
from pymol import math
import numpy
import random
import  matplotlib
import  matplotlib . pyplot  as  plt
```
