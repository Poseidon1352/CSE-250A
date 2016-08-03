import numpy as np
import matplotlib.pyplot as plt

x = [2]

while abs(x[-1]) > 0.001:
    x.append(x[-1] -np.tanh(x[-1]))

plt.plot(x)
plt.xlabel('Iteration no (n)')
plt.ylabel('$x_n$')
plt.show()
