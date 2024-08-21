import numpy as np
a = np.array([[1,2,3,4],[8,9,10,11],[55,56,57,58],[20,21,22,23]])
m  = np.reshape(a,(4,4))
print(m)
m = np.append(m,[[1,91,54,87]],0)
print(m)
m = np.delete(m,[4],0)      
print(m)
p = [2,1,3,3,4]
slicied_array = p[1:3]
print(slicied_array)

p.reverse()
print(p)