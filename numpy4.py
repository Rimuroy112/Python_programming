import numpy as np
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
b = np.array([1,2,3,4,5,6])
print(a.transpose())
print(a.T)
print(np.flip(b))
print(np.flip(a,axis=0))
print(np.flip(a,axis=1))
print(np.flip(a[1]))
print(a.flatten())

