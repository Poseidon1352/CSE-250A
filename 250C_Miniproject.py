import numpy as np
import matplotlib.pyplot as plt
np.random.seed(100) #edit seed to change pseudorandom numbers generated

sigma = 0.05; shape = 'box'
N = 400
T_vec = [50,100,500,1000]

# Setting theoretical parameters given scenario and sigma
if shape == 'box':
    M = np.sqrt(5); rho = np.sqrt(5)
    w_opt = [1,1,1,1,0]
    titlestr = 'Scenario 1: Hypercube, Sigma ='+str(sigma)
else:
    M = 1; rho = np.sqrt(2)
    w_opt = [0.5,0.5,0.5,0.5,0]
    titlestr = 'Scenario 2: Ball, Sigma ='+str(sigma)

#Euclidean projection function
def project(p):
    if shape == 'box':
        #Clips values when outside [-1,1], leaves them unmodified otherwise
        return (np.abs(p) > 1)*np.sign(p) + p*(np.abs(p) < 1) 
    else:
        #Divides by norm if outside unit ball
        if np.linalg.norm(p) > 1:
            return p/np.linalg.norm(p)
        else:
            return p

#Generates x given y
def x_oracle(y):
    p = np.random.normal(y*0.25,sigma,4) #4D IID Gaussian, mu=y/4
    return np.append(project(p),[1]) #projects point and appends x_0 dimension

#Generating test set
#y is Bernoulli with p = 0.5 which is Binomial with N=1, p = 0.5.
y_test = 2*(np.random.binomial(1,0.5,N)- 0.5);
x_test = [];
for i in range(N):
    x_test.append(x_oracle(y_test[i]))

err_mu = []; err_std = [];
lss_mu = []; lss_std = [];
eps = [];

#Iterating over number of training examples
for T in T_vec:
    err = [];lss = [];
    alpha = M/(rho*np.sqrt(T))
    #Repeating SGD for given T to get expected values of error,risk
    for SGD_reps in range(20):
        #initalize w to 0
        w = np.array([0]*5); w_sum = np.array([0]*5)
        for t in range(T-1):
            #Drawing fresh sample of z =(y,x)
            y = 2*(np.random.binomial(1,0.5)- 0.5)
            x = x_oracle(y)
            #Gradient oracle
            G = (-y*x*np.exp(-y*np.dot(w,x)))/(1 + np.exp(-y*np.dot(w,x)))
            #weight update
            w = project(w - alpha*G)
            w_sum = w_sum + w
        ws = w_sum/T
        #computing error and loss
        err.append(sum(np.sign(np.dot(x_test,ws)) != y_test)/N)
        lss.append(sum(np.log(1+np.exp(-y_test*np.dot(x_test,ws))))/N)
    eps.append(M*rho/np.sqrt(T))
    #Computing mean and standard deviation of error,risk
    err_mu.append(np.mean(err)); err_std.append(np.std(err))
    lss_mu.append(np.mean(lss)); lss_std.append(np.std(lss))

#Computing optimal risk for reference
#[approximating it by performance of optimal classifier on test set]
OptLss = sum(np.log(1+np.exp(-y_test*np.dot(x_test,w_opt))))/N

#Printing expected error
#This is useful when sigma = 0.05 and error is too small to see
print('Error ='+str(err_mu)+' for T ='+str(T_vec))
       
plt.figure()
plt.errorbar(T_vec,err_mu,yerr = 0.5*np.array(err_std))
plt.title('Classification Error, '+titlestr)
plt.ylabel('Expected Classification Error')
plt.xlabel('No of Training Samples')
plt.xlim(0,1100)
plt.show()

plt.figure()
plt.errorbar(T_vec,lss_mu,yerr = 0.5*np.array(lss_std))
a = plt.plot(T_vec,[OptLss]*4,'r',label='Optimal Classifier')
plt.legend(handles = a)
plt.title('Expected Risk, '+titlestr)
plt.ylabel('Expected Risk')
plt.xlabel('No of Training Samples')
plt.xlim(0,1100)
plt.show()

plt.figure()
plt.errorbar(T_vec,lss_mu-OptLss,yerr = 0.5*np.array(lss_std))
a = plt.plot(T_vec,eps,label='Worst case epsilon')
plt.legend(handles = a)
plt.title('Excess Risk, Epsilon '+titlestr)
plt.ylabel('Excess Risk, Epsilon')
plt.xlabel('No of Training Samples')
plt.xlim(0,1100)
plt.show()
