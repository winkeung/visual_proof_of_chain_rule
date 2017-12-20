'''
==========================
Visual Proof of Chain Rule
==========================

This Program Provide a Visual Proof of Chain Rule.
'''

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

import numpy
from mpl_toolkits.mplot3d import proj3d

def orthogonal_proj(zfront, zback):
    a = (zfront + zback) / (zfront - zback)
    b = -2 * (zfront * zback) / (zfront - zback)
    # -0.0001 added for numerical stability as suggested in:
    # http://stackoverflow.com/questions/23840756
    return numpy.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, a, b],
                        [0, 0, -0.0001, zback]])

# Later in your plotting code ...
proj3d.persp_transformation = orthogonal_proj

# Define u = f(x) and y = g(u) and their derivative here
def f(x):
    return x**2

def dfdx(x):
    return 2*x

def g(u):
    return u**2

def dgdu(u):
    return 2*u


mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

X = np.linspace(0, 5, 100)
U = [f(x) for x in X]
Y = [g(u) for u in U]

# Define the point which its tangent line will be shown.
x = 2

DX = np.linspace(-2, 3, 100)
DU = [dfdx(x) * dx for dx in DX]
DY = [dgdu(f(x)) * du for du in DU]

DX_Offset = [dx+x for dx in DX]
DU_Offset = [du+f(x) for du in DU]
DY_Offset = [dy+g(f(x)) for dy in DY]

ax.plot(X, U, Y, label='u = f(x)\ny = g(u)')
ax.set_xlabel('x')
ax.set_ylabel('u')
ax.set_zlabel('y')

ax.plot(DX_Offset, DU_Offset, DY_Offset, label = "tagent at x=2")

ax.legend()

plt.show()
