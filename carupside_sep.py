import numpy as np
import matplotlib.pyplot as plt
x = [0,1,2,3,4,5,6]
y = [2.9,3.1,3.4,3.5,3.6,4,0]
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title('graph')
ax1.set_xlabel('year201X')
ax1.set_ylabel('value')
ax1.plot(x,y,c='g',label='stock car')
a = [0,1,2,3,4,5,6]
b = [1.7,1.8,2.4,1.3,0.9,1,0]
ax1.plot(a,b,c='r',label='diff car')
g = [0,1,2,3,4,5,6]
h = [2,2,2,2,2,2,4]
ax1.plot(g,h,c='b',label='try')
leg = ax1.legend(loc='upper left')
plt.show()
print("end")
