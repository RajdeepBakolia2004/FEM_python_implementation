import numpy as np
def stima3(x1,y1,x2,y2,x3,y3):
    mat = np.array([[1,1,1], [x1,x2, x3], [y1,y2, y3]])
    d = np.array([[0,0], [1,0],[0,1]])
    G = np.matmul(np.linalg.inv(mat),d)
    val = np.linalg.det(mat)
    M = (np.matmul(G, G.T))*val 
    return M