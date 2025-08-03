# this is a python implementation of FEM for 2D problems
# the code is structured to read mesh and boundary condition files and then visualize the solution

import numpy as np
import matplotlib.pyplot as plt
from stima3 import stima3  
from stima4 import stima4  
from f import f

#part1: loading of the mesh geometry and initialization


with open('coordinates.txt', 'r') as coordinate_file:
    coordinates = []
    for line in coordinate_file:
            x, y = map(float, line.split())
            coordinates.append((x, y))
    coordinates = np.array(coordinates)
try:
    with open('elements3.txt', 'r') as triangle_file:
        triangles = []
        for line in triangle_file:
            v1, v2, v3 = map(int, line.split())
            triangles.append((v1 - 1, v2 - 1, v3 - 1))  
        triangles = np.array(triangles)
except FileNotFoundError:
    triangles = np.array([])
try:
    with open('elements4.txt', 'r') as parallel_file:
        quadrilaterals = []
        for line in parallel_file:
            v1, v2, v3, v4 = map(int, line.split())
            quadrilaterals.append((v1 - 1, v2 - 1, v3 - 1, v4 - 1))  
        quadrilaterals = np.array(quadrilaterals)
except FileNotFoundError:
    quadrilaterals = np.array([])
try:
    with open('neumann.txt', 'r') as neumann_file:
        neumann = []
        for line in neumann_file:
            v1, v2 = map(int, line.split())
            neumann.append((v1 - 1, v2 - 1))  
        neumann = np.array(neumann)
except FileNotFoundError:
    neumann = np.array([])
try:
    with open('dirichlet.txt', 'r') as dirichlet_file:
        dirichlet = []
        for line in dirichlet_file:
            v1, v2 = map(int, line.split())
            dirichlet.append((v1 - 1, v2 - 1))  
        dirichlet = np.array(dirichlet)
except FileNotFoundError:
    dirichlet = np.array([])

# we have now coordinates, triangles, parallelogram, neumann, and dirichlet loaded

FreeNodes = [i for i in range(len(coordinates))]
for v1, v2 in dirichlet:
    if v1 in FreeNodes:
        FreeNodes.remove(v1)
    if v2 in FreeNodes:
        FreeNodes.remove(v2)

A = np.zeros((len(coordinates), len(coordinates)))
b = np.zeros((len(coordinates),1))


# part2: assembling the stiffness matrix in two loops first for triangles and then for quadrilaterals
for element in triangles:
    v1, v2, v3 = element
    x1, y1 = coordinates[v1]
    x2, y2 = coordinates[v2]
    x3, y3 = coordinates[v3]
    AK = stima3(x1, y1, x2, y2, x3, y3 )
    A[np.ix_([v1, v2, v3], [v1, v2, v3])] += AK


for element in quadrilaterals:
    v1, v2, v3, v4 = element
    x1, y1 = coordinates[v1]
    x2, y2 = coordinates[v2]
    x3, y3 = coordinates[v3]
    x4, y4 = coordinates[v4]
    AK = stima4(x1, y1, x2, y2, x3, y3, x4, y4)
    A[np.ix_([v1, v2, v3, v4], [v1, v2, v3, v4])] += AK

# part3: Incorporating the volume force in two loops for triangles and quadrilaterals

for element in triangles:
    v1, v2, v3 = element
    x1, y1 = coordinates[v1]
    x2, y2 = coordinates[v2]
    x3, y3 = coordinates[v3]
    x,y = (x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3
    value = (np.linalg.det(np.array([[x2-x1, x3-x1], [y2-y1, y3-y1]])))* f(x,y)/6
    b[v1] += value
    b[v2] += value
    b[v3] += value
for element in quadrilaterals:
    v1, v2, v3, v4 = element
    x1, y1 = coordinates[v1]
    x2, y2 = coordinates[v2]
    x3, y3 = coordinates[v3]
    x4, y4 = coordinates[v4]
    x,y = (x1 + x2 + x3 + x4) / 4, (y1 + y2 + y3 + y4) / 4
    value = (np.linalg.det(np.array([[x2-x1, x3-x1], [y2-y1, y3-y1]])))* f(x,y)/4
    b[v1] += value
    b[v2] += value
    b[v3] += value
    b[v4] += value 

#part4: Incorporating neumann boundary conditions
