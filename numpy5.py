import numpy as np
a = np.array([1,2,3,4,5,6,7])
b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
c = np.array([[2,3,4],
              [5,6,7],
              [8,9,10]])
a[0]=10
print(a[1])
print(a[0:])
print(a[1:5])
print(a[-6:-1])
print(b[2,2])
print(a[a>3])
print(a[(a>2)&(a<6)])
print(b+c)
print(c-b)
np.savetxt('firstfile.txt',c)
print(np.loadtxt('firstfile.txt'))
print(a.mean())
print(a.std())
print(a.var())