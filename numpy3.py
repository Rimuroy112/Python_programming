import numpy as np
a = np.array([1,2,3,4,5,6,7,8])
print(a.sum())
print(a.min())
print(a.max())
b = np.array([[1,2],
              [3,4]])
c = np.array([[5,6],
            [7,8]])
              
print(np.hstack((b,c)))
print(np.vstack((b,c)))
print(np.random.random((3,2)))
d = np.array([1,1,2,3,3,4,5,5,6,7,7])
print(np.unique(d))
print(np.unique(d,return_index=True))
print(np.unique(d,return_counts=True))
