# This code gives an approximate Monte-Carlo solution to the heat equation with the same initial and boundary conditions

import sys
from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import *

times = 100				# No. of times the iteration to be performed over all the nodes
ran_walk_count = 100	# No. of steps of random walk for every node
#h = 0.4
#k = 0.08
#r=(k/(h*h))
#p=1
cols = 10				# No. of cols
rows = 10				# No. of rows


def monte_solve(u):

	g=[]

	for i in range(cols):
		g.append(u[0][i])

	for i in range(rows-1):
		g.append(u[i+1][cols-1])

	for i in range(cols-1):
		g.append(u[rows-1][cols-2-i])

	for i in range(rows-2):
		g.append(u[rows-2-i][0])


	for i in range(rows):
		for j in range(cols):
			if (i!=0)&(i<rows-1)&(j!=0)&(j<cols-1):

				h = [0]*(2*rows + 2*cols - 4)

				i_temp = i
				j_temp = j

				for k in range(ran_walk_count):


					while ((i!=0)&(i<rows-1)&(j!=0)&(j<cols-1)):
						a = randint(1,4)
	
						if a==1:
							j-=1
						elif a==2:
							i-=1
						elif a==3:
							j+=1
						elif a==4:
							i+=1
	
					if i==0:
						h[i]+=1
					elif j==(cols-1):
						h[i+j]+=1
					elif i==(rows-1):
						h[rows+cols-2 + cols-1-j]+=1
					elif j==0:
						h[rows+cols-2 + cols -1 + rows-1-i]+=1


				i = i_temp
				j = j_temp
			
				l = len(g)
				for m in range(l):
					u[i][j] += (g[m]*h[m])/ran_walk_count	

u = [ [ 0 for i in range(cols) ] for j in range(rows) ] #zeros being initialized as matrix
u[0] = [ 10000 for i in range(cols) ]

for expr in range(times):
	monte_solve(u)

u[0] = [ (times*10000) for i in range(cols) ]

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
