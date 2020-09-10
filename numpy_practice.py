import numpy as np

data = np.arange(10)
data.shape=(2,5)
x=data[:]
#print(x)
#x = data[1,1,0]
y = np.arange(35).reshape(5,7)
#y[1:5:2,::3]
print(y[np.array([0,2,4]), np.array([0,1,2])])


#i = np.argmax(f)
#print x[i], f[i]
