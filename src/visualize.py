import numpy as np
import matplotlib.pyplot as plt

def visualize(A, B) :
    A = np.array(A)
    B = np.array(B)
    fig = plt.figure()
    ax = plt.axes(projection = '3d')
    ax.scatter3D(A[:,0], A[:,1], A[:,2], c='lightsteelblue')
    ax.scatter3D(B[:,0], B[:,1], B[:,2], edgecolor='black', c='midnightblue')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()