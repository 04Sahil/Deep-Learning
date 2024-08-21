import numpy as np
x = [1,2,3,4,5,6]
y = [7,8,9,10,11,12]
print(x+y)
print(np.sum(x))
a = np.array([1,2,3,4,5,6])
b = np.array([7,8,9,10,11,12])
print(a+b)
print(a.sum())
print("after reshape")
a_reshape = a.reshape((2, 3))
print("reshaped x:\n",a_reshape)
a_reshape[1,0] = 9
print("reshaped x:\n",a_reshape)
#two dimension
c = np.array([[1,2], [3,4]])
print(c.ndim)
print(c.shape)