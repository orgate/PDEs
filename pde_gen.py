#	This code solves any 2nd order PDE of the form:
#	(A*uxx) + (B*uxy) + (C*uyy) + (D*ux) + (E*uy) + (F*u) = G
#	where uxx means 2nd partial derivative of u along x-axis and similarly other notations
#	and A,B,C,D,E,F and G are real numbers
#	Also note that 'y' could be replaced by 't' too
# here the initial conditions and boundary conditions are not generic, but rather same as that of the heat equation
# i.e. u(0,t) = 0; here it means u[][0] = 0  (Boundary condition)
# 	   u(1,t) = 0; here it means u[][cols] = 0 (Boundary condition)
# 	   u(x,0) = 1; here it means u[0] = 10000 (Initial condition)

import sys
from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

times=1000		# No. of times the iteration happens
h = 0.4			# The x-axis length scale
k = 0.08		# The y-axis length scale or the time-scale
r=(k/(h*h))
p=1				# Parmeter to be used in implicit finite-difference method, but not used here
cols = 50		# No. of columns or no. of x-axis length divisions 
rows = 50		# No. of rows or no. of y-axis length divisions or no. of time units simulation is performed

# The parameters defining the PDE
A=1
B=0
C=1
D=0
E=0
F=1
G=0

def gen_solve(u,A,B,C,D,E,F,G):
	for i in range(rows):
		for j in range(cols):
			if (i!=0)&(i<rows-1)&(j!=0)&(j<cols-1):

				u[i][j] = ( G - u[i][j+1]*( (A/(h*h)) + (D/(2*h)) ) - u[i][j-1]*( (A/(h*h)) - (D/(2*h)) ) - u[i+1][j+1]*(B/(4*h*k)) + u[i+1][j-1]*(B/(4*h*k)) +  u[i-1][j+1]*(B/(4*h*k)) - u[i-1][j-1]*(B/(4*h*k)) - u[i+1][j]*( (C/(k*k)) + (E/(2*k)) ) - u[i-1][j]*( (C/(k*k)) - (E/(2*k)) ) ) / ( F - (2*A)/(h*h) - (2*C)/(k*k) )

u = [ [ 0 for i in range(cols) ] for j in range(rows) ] #zeros being initialized as matrix
#u[0] = [ 10000 for i in range(cols) ]



for i in range(cols):
	for j in range(rows):
		if ((i==(cols/2)) or (j==(rows/2))) and i!=0 and j!=0 and i!=cols-1 and j!=rows-1:
			u[i][j] = 1




for expr in range(times):
	gen_solve(u,A,B,C,D,E,F,G)

# The matrix u could be printed by uncommenting the below line
#print "u",u

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(cols):
	y = [ j for j in range(cols) ]
	x = [ i for j in range(cols) ]
	z = u[i]
	ax.plot(x,y,z) #to be modified
plt.title('Solution of any PDE as time progresses - Magnitude of u on z-axis')
plt.ylabel('x-axis length')
plt.xlabel('For different times (y-axis)')
plt.show()

