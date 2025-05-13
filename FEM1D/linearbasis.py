import numpy as np
import matplotlib.pyplot as plt

def linear_basis(n,j,x):
    h = 1/(n+1)
    if x < (j-1)*h or x > (j+1)*h:
        return 0
    elif x < j*h:
        return (x - (j-1)*h)/h
    else:
        return ((j+1)*h - x)/h
    
if __name__ == "__main__":
    n = 4
    x = np.arange(0, 1 + 1/((n+1)*10), 1/((n+1)*10))
    plt.figure(figsize=(6, 15))
    for j in range(1, n+1):
        plt.subplot(n, 1, j)
        plt.plot(x, [linear_basis(n,j,x_i) for x_i in x], 'r-')
        plt.title(f'j={j}')
        plt.xlim(0, 1.03)
        plt.ylim(-0.1, 1.1)
    plt.savefig('linear_basis.png')
    n = 4
    x = np.arange(0, 1 + 1/((n+1)*10), 1/((n+1)*10))
    plt.figure(figsize=(4, 4))
    plt.plot(x, [linear_basis(n,1,x_i) for x_i in x], 'b-')
    plt.plot(x, [linear_basis(n,2,x_i) for x_i in x], 'r-')
    plt.plot(x, [linear_basis(n,3,x_i) for x_i in x], 'g-')
    plt.plot(x, [linear_basis(n,4,x_i) for x_i in x], 'y-')
    plt.title('basis function')
    plt.xlim(0, 1.03)
    plt.ylim(-0.1, 1.1)
    plt.savefig('linear_basis_all.png')