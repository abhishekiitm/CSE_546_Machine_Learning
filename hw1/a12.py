import numpy as np
import math
import matplotlib.pyplot as plt

eps = 0.0025
n = math.ceil(1/4/eps)

k_array = [1, 8, 64, 512]
k = k_array[1]
Z=np.random.randn(n)

plt.step(sorted(Z), np.arange(1,n+1)/float(n))
for k in k_array:
    Y_k = np.sum(np.sign(np.random.randn(n, k))*np.sqrt(1./k), axis=1) 
    plt.step(sorted(Y_k), np.arange(1,n+1)/float(n))

plt.show()