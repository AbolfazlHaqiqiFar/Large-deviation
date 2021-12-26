import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

mus = []
eigmus = []
lams = np.arange(-10, 0, 1)
# lams = [-10]
alpha = 0.75
L = 6000
T = 1000

Ns = pd.DataFrame(columns=[1, 2])


for lam in lams:
    U = np.array([[1 - alpha/2, alpha/2],
                 [alpha/2, 1 - alpha/2]])
    J = np.array([[0, 1],
                 [1, 0]])
    UT = np.exp(lam*J)*U
    eigmus.append(np.amax(np.linalg.eig(UT)[0]))
    K = np.diag(np.sum(UT, axis=0))
    Up = UT / np.diag(K)
    Ms = []

    p0 = np.array([5/6, 1/6])
    for t in range(T):
        n0 = L * p0
        Ns.loc[t] = n0
        n_half = np.matmul(K, n0)
        M = L / sum(n_half)
        Ms.append(M)
        p_half = 1/L * n_half
        n1 = np.matmul(Up, p_half)
        p1 = M * n1
        p0 = p1

    mu = (-sum(np.log(Ms)))/T
    mus.append(mu)

print(Ns)
t = np.linspace(0, 1000, 1000)
plt.plot(lams, eigmus)
# plt.plot(lams, mus)
# plt.scatter(Ns[1], t)
# plt.scatter(Ns[2], t)
plt.savefig('foo3.jpg')

