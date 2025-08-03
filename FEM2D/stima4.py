import numpy as np
def stima4(x1,y1,x2,y2,x3,y3,x4,y4):
    D = np.array([[x2-x1, x4-x1], [y2-y1, y4-y1] ])
    temp = np.linalg.inv(np.matmul(D.T, D)) #symmetric matrix
    a,b,c = temp[0][0], temp[0][1], temp[1][1]
    M = (np.linalg.det(D)/6)*np.array([[3*b + 2*(a+c), -2*a + c, -3*b -(a+c),a - 2*c],
                                       [-2*a + c, -3*b + 2*(a+c), a - 2*c, 3*b - (a+c)],
                                       [-3*b-(a+c), a -2*c, 3*b + 2*(a+c),-2*a+c],
                                       [a - 2*c, 3*b - (a+c), -2*a + c, -3*b + 2*(a + c)]])
    return M