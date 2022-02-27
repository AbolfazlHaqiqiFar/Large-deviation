import numpy as np
import matplotlib.pyplot as plt
import math

C = np.array([5000, 1000])
dim = 2


Cprime = np.zeros(dim)
Lambda = 0
alpha = 0.75
T = 10
Uprime = np.zeros((dim , dim))
k, Utilde = np.zeros((dim, dim)),  np.zeros((dim, dim))

#Utilde = np.matrix([[1-  alpha , alpha* np.exp(Lambda) ], [ alpha * np.exp(Lambda), 1 - alpha ]])
for i in range(dim):
    prob = np.random.rand()
    Utilde[i][i] =1 - prob
    Utilde[(i+1)%dim][i] = prob
    #Utilde = np.matrix.transpose(Utilde)


Uprime = Utilde
for f in range(dim):
    Uprime[(f+1)%dim][f] = Uprime[(f+1)%dim][f] * np.exp(Lambda)
Mt = []
for w in range(10):
    c = np.zeros(dim)
    num = np.zeros(dim)
    D = [c[0], c[1]]
    for y in np.arange(0, dim):
        for z in np.arange(0, dim):
            if z != y :
                if Uprime[y][z] > np.random.random():
                    num[y] += 1
                    c[z] = C[z] - 1
                    Cprime[y] = num[y] + D[y]                
    for o in np.arange(0, 2):
        if k[o, o] - math.floor(k[o, o]) > np.random.random() :
            c[o] = C[o]+ math.floor(k[o, o]) + 1
        else:
            c[o] = C[o] + math.floor(k[o, o]) -1
            C[o] = C[0] + num[0]
    Mt.append(sum(c)/ sum(Cprime))

print( np.log(np.prod(Mt)) / T)
