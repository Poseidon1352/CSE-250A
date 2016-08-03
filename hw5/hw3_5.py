import numpy as np

with open('spectX.txt') as file:
    X = file.read().splitlines()
X = [[float(i) for i in X[j].split()] for j in range(len(X))]

with open('spectY.txt') as file:
    T = file.read().splitlines()
T = [float(i) for i in T]

p = [2.0/23 for i in range(23)]
nE = [0]*257
Ll = [0]*257

for itno in range(257):
    py = 1 - np.array([np.prod([(1-pi)**Xi for (pi,Xi) in zip(p,Xj)]) for Xj in X])
    y = np.round(py)
    nE[itno] = np.sum(np.abs(y - T))
    Ll[itno] = (1.0/267)*(np.sum(np.log([pyi*Ti + (1-pyi)*(1-Ti) for (pyi,Ti) in zip(py,T)])))
    p = [np.sum([T[j]*X[j][i]*p[i]/py[j] for j in range(267)])/np.sum(X[j][i] for j in range(267)) for i in range(23)]
