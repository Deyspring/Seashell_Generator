# Generate the shell mesh from shell variables
import math
    
def generateShell(n,m):
	""" Generate shell mesh from passed variables"""

	#Adjust resolution of mesh for number of shell turns
	n = int( n * turns / 10.0) 
	spiral = PVector(n) # Pvector: a class describing a 2D or 3D dimensional vector with magnatude and direction 
	shell = PVector(n,m) #Pvector, not sure how to import or link to this module, it's from Processing

	#Get vertices for the shell
	count = 0
	# Generate main spiral
  	theta = float(map(i, 0, n, 0, turns))
  	rad = float(exp(theta * cos(alpha) / sin(alpha)))
  	
  	x = float(A * rad * sin(beta) * cos(theta) * D)
  	y = float( A * rad * sin(beta) * sin(theta))
  	z = float(-A * rad * cos(beta))

  	spiral = [PVector(x, y, z)]
    

   # if count < n: count += 1 

turns = 1
D=1
alpha=math.radians(83)
beta=math.radians(42) 
phi=math.radians(70) 
mu=math.radians(10) 
omega=math.radians(30) 
A=25 
a=12 
b=20 
L=0 
P=0 
W1=0 
W2=0 
N=0
#generateShell(1,2)
