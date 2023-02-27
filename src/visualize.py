import numpy as np
import matplotlib.pyplot as plt

def visualize(A, B) :
    A.remove(B[0])
    A.remove(B[1])
    A = np.array(A)
    B = np.array(B)
    fig = plt.figure()
    ax = plt.axes(projection = '3d')
    if (len(A) != 0) :
        ax.scatter3D(A[:,0], A[:,1], A[:,2], c='y')
    ax.scatter3D(B[:,0], B[:,1], B[:,2], c='r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()