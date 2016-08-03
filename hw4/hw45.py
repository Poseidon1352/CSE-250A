import numpy as np
with open('nasdaq00.txt') as file:
    prices = file.read().splitlines()
prices = list(map(lambda x: float(x),prices))
coeffs = [[0]*4 for x in range(0,4)];
bias = [0]*4
for i in range(5,len(prices)+1):
    x = prices[i-5:i]
    for j in range(0,4):
        coeffs[j] = [x[j]*y + b for y,b in zip(x[0:4],coeffs[j])]
        bias[j] = bias[j] + x[j]*x[4]

a = np.linalg.solve(coeffs,bias)
MSE = 0
for i in range(4,len(prices)):
    x = prices[i-4:i]
    MSE = MSE + (np.dot(x,a) - prices[i])**2

MSE = MSE/(len(prices) - 4)
print('MSE for year 2000: '+str(MSE))


with open('nasdaq01.txt') as file:
    prices2 = file.read().splitlines()
prices2 = list(map(lambda x: float(x),prices2))
MSE = 0
for i in range(4):
    x = prices[-4+i:] + prices2[:i]
    MSE = MSE + (np.dot(x,a) - prices2[i])**2
for i in range(4,len(prices2)):
    x = prices2[i-4:i]
    MSE = MSE + (np.dot(x,a) - prices2[i])**2

MSE = MSE/len(prices2)
print('MSE for year 2001: '+str(MSE))
