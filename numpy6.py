import numpy as np
arr = np.array([1,2,3,4,5,6,7])
arr1 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print(arr[::2])
print(arr1[1,2])
print(arr1[0:2,2:3])
indices = [0,2]
print(arr1[indices ,:])
print(arr1[:, indices])
