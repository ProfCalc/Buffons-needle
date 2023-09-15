import numpy as np
import matplotlib.pyplot as plt
print('hello world')
print(np.pi)

def sawtooth(x):
    ans = (1/2 - (1/np.pi)*((np.sin(np.pi*x)) + ((np.sin(2*np.pi*x))/2) + ((np.sin(3*np.pi*x))/3) + ((np.sin(4*np.pi*x))/4) + ((np.sin(5*np.pi*x))/5)))
    return ans

print(sawtooth(2.5) + 5)
print(type(sawtooth(2.5) + 5))
x=[]
y=[]

# for i in range(0,20):
#     x.append(i)
#     y.append(sawtooth(i))

# print(x)
# print(y)    

# plt.plot(x,y)
# plt.show