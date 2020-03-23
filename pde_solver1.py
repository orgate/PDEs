# Solution of (heat equation) PDE when iterated in the forward direction and in the reverse direction
import sys
from numpy import *

h = 0.2
#	k = 0.08
cols = 10
rows = 10
times = 20

def implicit_solve(u,v):
	for i in range(rows):
		for j in range(cols):
			if (i!=0)&(i!=rows-1)&(j!=0)&(j!=cols-1):
				u[i,j] = (u[i+1,j] + u[i-1,j] + u[i,j+1] + u[i,j-1])/4
				v[rows-i-1,cols-j-1] = (v[rows-i-2,cols-j-1] + v[rows-i,cols-j-1] + v[rows-i-1,cols-j-2] + v[rows-i-1,cols-j])/4

u = matrix([ [0] * cols ] * rows)
v = matrix([ [0] * cols ] * rows)

#	r = k/(h*h)


for i in range(cols):
	u[0,i] = 10000*sin(i*pi/10)
	v[0,i] = 10000*sin(i*pi/10)


for expr in range(times):
	implicit_solve(u,v)

print "Matrix, when itertion starts from t=0 to t=T"
print u
print "Matrix, when itertion starts from t=T to t=0"
print v

