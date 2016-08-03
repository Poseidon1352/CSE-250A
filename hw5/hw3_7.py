import numpy as np
import matplotlib.pyplot as plt
def g(x):
    return (1.0/10)*sum(np.log([np.cosh(x + 1.0/np.sqrt(k*k+1)) for k in range(1,11)]))
def dg(x):
    return (1.0/10)*sum([np.tanh(x + 1.0/np.sqrt(k*k+1)) for k in range(1,11)])
x = [0]

while len(x) < 2 or abs(g(x[-1]) - g(x[-2])) > 0.00001:
    x.append(x[-1] - dg(x[-1]))

plt.plot(np.linspace(-10,10),g(np.linspace(-10,10)))
plt.xlabel('x')
plt.ylabel('g(x)')
plt.title('Plot of g(x)')
plt.show()

plt.plot(x)
plt.xlabel('Iteration no (n)')
plt.ylabel('$x_n$')
plt.show()
