import numpy as np
import matplotlib.pyplot as plt

coordinate_file = open('coordinates.txt', 'r')

with coordinate_file:
    coordinates = []
    for line in coordinate_file:
        if line.strip():  # Check if the line is not empty
            temp, x, y = map(float, line.split())
            coordinates.append((x, y))

    coordinates = np.array(coordinates)
    
trinagle_file = open('elements3.txt', 'r')

with trinagle_file:
    triangles = []
    for line in trinagle_file:
        if line.strip():  # Check if the line is not empty
            temp, v1, v2, v3 = map(int, line.split())
            triangles.append((v1 - 1, v2 - 1, v3 - 1))  # Convert to zero-based index

    triangles = np.array(triangles)
    
parallel_file = open('elements4.txt', 'r')

with parallel_file:
    parallels = []
    for line in parallel_file:
        if line.strip():  # Check if the line is not empty
            temp, v1, v2, v3, v4 = map(int, line.split())
            parallels.append((v1 - 1, v2 - 1, v3 - 1, v4 - 1))  # Convert to zero-based index

    parallels = np.array(parallels)


neumann_file = open('neumann.txt', 'r')

with neumann_file:
    neumann = []
    for line in neumann_file:
        if line.strip():  # Check if the line is not empty
            temp, v1, v2 = map(int, line.split())
            neumann.append((v1 - 1, v2 - 1))  # Convert to zero-based index

    neumann = np.array(neumann)

dirichlet_file = open('dirichlet.txt', 'r')

with dirichlet_file:
    dirichlet = []
    for line in dirichlet_file:
        if line.strip():  # Check if the line is not empty
            temp, v1, v2 = map(int, line.split())
            dirichlet.append((v1 - 1, v2 - 1))  # Convert to zero-based index

    dirichlet = np.array(dirichlet)

# plot the points and then the trianles and parallelograms and marks the dirichlet and neumann boundaries with red and blue colors respectively
plt.figure(figsize=(10, 10))
plt.scatter(coordinates[:, 0], coordinates[:, 1], color='black', s=10, label='Points')
plt.legend()
for triangle in triangles:
    pts = coordinates[list(triangle)]
    plt.fill(pts[:, 0], pts[:, 1], edgecolor='yellow', fill=False, alpha=1, label='Triangle')
for parallel in parallels:
    pts = coordinates[list(parallel)]
    plt.fill(pts[:, 0], pts[:, 1], edgecolor='green', fill=False, alpha=1, label='Parallelogram')
for d in dirichlet:
    pts = coordinates[list(d)]
    plt.plot(pts[:, 0], pts[:, 1], color='red', linewidth=2, label='Dirichlet Boundary')
for n in neumann:
    pts = coordinates[list(n)]
    plt.plot(pts[:, 0], pts[:, 1], color='blue', linewidth=2, label='Neumann Boundary')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Mesh Visualization')
plt.axis('equal')
plt.grid()
plt.savefig('mesh_visualization.png')