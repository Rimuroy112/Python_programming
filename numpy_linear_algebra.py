import numpy as np
a = np.array([[1,2],
              [3,4]])
b = np.array([[2,2],
              [2,2]])

print(a @ b)
print(a.dot(b))
print(np.matmul(a,b))
print(np.linalg.inv(a))
print(np.linalg.det(a))
