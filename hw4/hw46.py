import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1./(1+np.exp(-x))

with open('newTrain3.txt') as file:
    train3 = file.read().splitlines()
with open('newTrain5.txt') as file:
    train5 = file.read().splitlines()
train = train3 + train5

train = list(map(lambda x:x.split(),train))
train = [[int(x) for x in y] for y in train]
train = np.matrix(train)


y = np.matrix([0]*len(train3) + [1]*len(train5)).T
w = np.matrix(np.random.uniform(-1, 1, size=64)).T
alpha = 1/len(train)

logL = []
trainErr = []
while (len(logL) < 2) or (np.abs(logL[-1] - logL[-2]) > 0.01) :
    p = sigmoid(np.dot(train,w))
    trainErr.append(np.abs(np.sum(y - np.round(p))/len(train)))
    logL.append(float(y.T*np.log(p) + (1-y).T*np.log(1-p)))
    delta = np.dot(train.T,y-p)
    w = w + alpha*delta


with open('newTest3.txt') as file:
    test3 = file.read().splitlines()
with open('newTrain5.txt') as file:
    test5 = file.read().splitlines()
test = test3 + test5
test = list(map(lambda x:x.split(),test))
test = [[int(x) for x in y] for y in test]
test = np.matrix(test)
y = np.matrix([0]*len(test3) + [1]*len(test5)).T
p = sigmoid(np.dot(test,w))
testErr = np.sum(np.abs(y - np.round(p)))/len(test)
print('Test Error = '+str(testErr))

plt.plot(trainErr)
plt.ylabel('Training Error')
plt.xlabel('Iteration No')
plt.show()

plt.plot(logL)
plt.ylabel('Log Likelihood')
plt.xlabel('Iteration No')
plt.show()

w = w/max(np.abs(w))
w = np.array(w).reshape(8,8)
plt.pcolor(np.abs(w),cmap='Greys')
plt.show()
