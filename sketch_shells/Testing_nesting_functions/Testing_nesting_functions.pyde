"""
Shell spiral and oval generator 
"""
# This file is an extension of shell_function, which produces a spiral and one oval. 
#Trying to create a shell function that generates the spiral and multiple ovals that show the shape of the shell

import math  

def BoatEarMoonPresets():
    """ Variables for the creation of a Boat Ear Moon Shell"""
    i = 1
    D=1
    alpha_=math.radians(83)
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
    return i,D,alpha_, beta,phi, mu, omega, A, a, b, L, P, W1, W2, N

def generateSpiral(presets,n,m,turns):
    """ Generates spiral points """
    i,D,alpha_, beta,phi, mu, omega, A, a, b, L, P, W1, W2, N = presets
    
    spiral_matrix=[]

    while i < n: 
        theta = float(map(i, 0, n, 0, turns))
        rad = float(exp(theta * cos(alpha_) / sin(alpha_)))
    
        x = float(A * rad * sin(beta) * cos(theta) * D)
        y = float( A * rad * sin(beta) * sin(theta))
        z = float(-A * rad * cos(beta))
        
        spiral_i = PVector(x,y,z)
        
        generateSpline(presets,m,theta,rad,spiral_i)  
        
        spiral_matrix.append(spiral_i) 
        i = i + 1  #for some reason i += 1 does not work here. It may be a processing thing. 
    
    return spiral_matrix


def generateSpline(presets,m,theta,rad,spiral_i):
    #Generates spline around a spiral point 
    
    i,D,alpha_, beta,phi, mu, omega, A, a, b, L, P, W1, W2, N = presets

    spline_matrix= []

    j = 0 
    while j < m: 
        s = float(map(j, 0, m, 0, TWO_PI)) 
        r2 = float(pow( pow(cos(s)/a,2) + pow(sin(s)/b,2), -0.5 ))
        # add surface manipulations
        surfrad = float(0)
        if (W1==0 or W2==0 or N==0):
            surfrad = 0
        else: 
            lt = float((TWO_PI / N) * ( N*theta / TWO_PI - int(N*theta / TWO_PI) ))
            surfrad = L * exp( -( pow(2*(s-P)/W1, 2) + pow(2*lt/W2, 2) ) ) 
        j = j+ 1 
    
    surface_radiations(s, phi, r2, rad, surfrad, theta, omega, D, mu) 
    
    return spline_matrix 


def surface_radiations(s, phi, r2, rad, surfrad, theta, omega, D, mu): 
    r2 += surfrad# loop end here? or one indent left
        
    x = cos(s + phi) * cos(theta + omega) * r2 * rad * D   # here  rad - 1 closes the opening of the curve at the origin
    y = cos(s + phi) * sin(theta + omega) * r2 * rad
    z = sin(s + phi)                      * r2 * rad
        
    # adjust orientation of the ellipse? so shell doesn't flatten out to a ribbon?
    x -= sin(mu) * sin(s + phi) * sin(theta + omega) * r2
    y += sin(mu) * sin(s + phi) * cos(theta + omega) * r2
    z *= cos(mu)
    return  x,y,z

        
# Draw Shell point cloud on screen
        
currentFrame = 0

def setup():
  size(600,600,P3D) 
  frameRate(24)

def draw():
  background(255,255,255)
  global currentFrame
  currentFrame = currentFrame + 1
  
  fov =  float(PI/3)
  cameraZ = float((height/2.0) / tan(fov/2.0))
  perspective(fov, float(width)/float(height), cameraZ/10.0, cameraZ*10.0) 
  
  translate(300,300)
  rotateY(currentFrame/24.0)
 
  stroke(255,0,0)
  strokeWeight(10)
  
  # variables to set the resolution of the shell mesh 
  n = 10 # Increasing n,m does not make the shell bigger but does increase the resolution of the spirals 
  m = 20
  turns = 10 # This increases the size
  s= 0

  spiral_points= generateSpiral(BoatEarMoonPresets(),n,m,turns)
  
  for vertex in spiral_points: # need to make this spiral_points[0] if returning more than just points
        stroke(0,0,255)
        strokeWeight(10)
        x,y,z = vertex[0],vertex[1],vertex[2]
        point(x,y,z)
  
  #oval_points = generateOval(BoatEarMoonPresets(), spiral_points[0])
'''
  for vertex in oval_points:
        stroke(255,0,0)
        strokeWeight(10)
        x,y,z = vertex[0],vertex[1],vertex[2]
        point(x,y,z)'''
