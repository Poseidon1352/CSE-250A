import numpy as np
import copy

with open('rewards.txt') as file:
    R = file.read().splitlines()
R = np.array([int(x) for x in R])
gamma = 0.9875
A = {}
for i in range(4):
    A[i] = np.array([[0.0]*81 for x in range(81)])
    with open('prob_a'+str(i+1)+'.txt') as file:
        for line in file:
            vals = line.split()
            A[i][int(vals[0])-1][int(vals[1])-1] = float(vals[2])

V_val = [0]*81; V_prev = [-1]*81
while V_prev != V_val:
    V_prev = copy.deepcopy(V_val)
    a1 = np.dot(A[0],V_val);a2 = np.dot(A[1],V_val);
    a3 = np.dot(A[2],V_val);a4 = np.dot(A[3],V_val);
    for s in range(81):
        V_val[s] = R[s] + gamma*max([a1[s],a2[s],a3[s],a4[s]])

pi_val = [0]*81
print('Non Zero Values in format \ns : V*[s]\n')
for s in range(81):
    pi_val[s] = np.argmax([a1[s],a2[s],a3[s],a4[s]])
    if V_val[s] != 0:
        print(str(s+1)+' : '+str(V_val[s]))

pi_pol = [0]*81; pi_prev = [-1]*81; I = np.identity(81); n_iter = 0;
while pi_prev != pi_pol:
    n_iter = n_iter + 1
    pi_prev = copy.deepcopy(pi_pol); P_pi = []
    for s in range(81):
        P_pi.append(A[pi_pol[s]][s])
    P_pi = np.array(P_pi)
    V_pol = np.linalg.solve(I-gamma*P_pi,R)
    a1 = np.dot(A[0],V_pol);a2 = np.dot(A[1],V_pol);
    a3 = np.dot(A[2],V_pol);a4 = np.dot(A[3],V_pol);
    for s in range(81):
        pi_pol[s] = np.argmax([a1[s],a2[s],a3[s],a4[s]])

print('n_iter='+str(n_iter))
