import numpy as np
a = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
print(np.__version__)
print(a.ndim)
print(a.shape)
print(a.size)
b = np.zeros((2,2))
c = np.ones((2,2))
d = np.empty((2,2))
print(b)
print(c)
print(d)