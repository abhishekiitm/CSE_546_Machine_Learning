import numpy as np

A = np.array([[0,2,4],[2,4,2],[3,3,1]])
b = np.array([[-2],[-2],[-4]])
c = np.array([[1],[1],[1]])

A_inv = np.linalg.inv(A)
A_invb = np.matmul(A_inv, b)
Ac = np.matmul(A, c)

print(A_inv)
print(A_invb)
print(Ac)