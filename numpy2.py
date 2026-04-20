import numpy as np
a = np.arange(15)
print(a)
b = np.arange(1,15,2)
print(b)
c = np.linspace(0,10,num=5)
print(c)
d = np.array([8,5,2,6,3,7,1,4])
e = ([9,10,11,12])
print(np.sort(d))
print(np.concatenate((d,e)))
f = np.array([[2,3,4],
              [5,6,7]])
g = np.array([2,3,4,5,6,7])
print(g[np.newaxis,:]) # add axis at the beginning
print(g[:,np.newaxis]) # add axis at the end
print(f[0,:])
print(f[1,:])
print(f[:,0])
print(f[:,1])
print(f.sum(axis=0))
print(f.sum(axis=1))