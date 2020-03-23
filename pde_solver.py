#	Solution of (heat eqution) PDE as time progresses - Magnitude of u or temperature
import sys
from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

h = 0.4
k = 0.08
r=(k/(h*h))
p=1
cols = 100
rows = 100


def implicit_solve(u):
	for i in range(rows):
		for j in range(cols):
			if (i<rows-1)&(j!=0)&(j<cols-1):
				u[i+1][j] = (r*(1-p)*u[i][j+1] + (1-2*r*(1-p))*u[i][j] + r*(1-p)*u[i][j-1] + p*r*u[i+1][j+1] + p*r*u[i+1][j-1])/(1+2*r*p)

u = [ [ 0 for i in range(cols) ] for j in range(rows) ] #zeros being initialized as matrix

u[0] = [ 10000 for i in range(cols) ]

for expr in range(20):
	implicit_solve(u)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(cols):
	y = [ j for j in range(cols) ]
	x = [ i for j in range(cols) ]
	z = u[i]
	ax.plot(x,y,z) #to be modified

plt.title('Solution of (heat eqution) PDE as time progresses - Magnitude of u or temperature on z-axis')
plt.ylabel('x-axis length')
plt.xlabel('For different times')
plt.show()

