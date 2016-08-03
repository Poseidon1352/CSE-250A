from numpy import random
from math import fabs
import matplotlib.pyplot as plt
n_samples = 1000000
num = 0;den = 0;
p = [0]*n_samples
for i in range(n_samples):
    B = random.binomial(1,0.5,10)
    B = [str(x) for x in B]
    fB = int(''.join(B),2)
    pzb = 0.6*(0.25**(fabs(128 - fB)))
    if B[2] == '1':
        num = num + pzb
    den = den + pzb
    if den !=0:
        p[i] = num/den

print('Convergerd P(B=1|Z=128) = ' + str(p[n_samples-1]))
plt.plot(p)
plt.ylabel('P(B=1|Z=128)')
plt.xlabel('Iteration No')
plt.show()
