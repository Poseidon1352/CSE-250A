import numpy as np
import matplotlib.pyplot as plt

with open('initialStateDistribution.txt') as file:
    pi = file.read().splitlines()
with open('transitionMatrix.txt') as file:
    a = file.read().splitlines()
with open('emissionMatrix.txt') as file:
    b = file.read().splitlines()
with open('observations.txt') as file:
    o = file.read().split()

pi = np.log([float(x) for x in pi])
a = [x.split() for x in a]
a = np.log([[float(x) for x in y] for y in a])
b = [x.split() for x in b]
b = np.log([[float(x) for x in y] for y in b])
o = [int(x) for x in o] 
T = len(o)

L = np.array([[[0.,0] for x in range(26)] for y in range(T)])

L[0] = [[pi[i] + b[i][o[0]],-1] for i in range(26)]

for t in range(T-1):
    for j in range(26):
        i = np.argmax(L[t,:,0]+a[:,j])
        L[t+1,j] = [L[t,i,0] + a[i,j] + b[j,o[t+1]],i]

S = [int(np.argmax(L[T-1][:,0]))]
for t in range(T-1,0,-1):
    S.append(int(L[t][S[-1]][1]))
S.reverse()
S = [x+1 for x in S]
msg = [chr(S[0]+96)]
for t in range(1,T):
    if S[t] != S[t-1]:
        msg.append(chr(S[t]+96))

print(''.join(msg))
plt.plot(S)
plt.xlabel('Time')
plt.ylabel('Hidden State')
plt.show()
