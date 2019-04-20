"""
Spiral 
"""
import math  

def BoatEarMoonPresets():
    """ Variables for the creation of a Boat Ear Moon Shell"""
    # variables to set the resolution of the shell mesh 
    n = 10
    m = 3
    turns = 10
    s= 0
    # Boat ear moon presets
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
    return n,m,turns,s,i,D,alpha_, beta,phi, mu, omega, A, a, b, L, P, W1, W2, N

    
def generateSpiral(presets):
    """ Generates spiral points """
    n,m,turns,s,i,D, alpha_, beta,phi, mu, omega,A, a, b, L, P, W1, W2,N = presets
    
    spiral_matrix=[]
    i= 0
    while i < n: 
        print ("i", i) 
        theta = float(map(i, 0, n, 0, turns))
        rad = float(exp(theta * cos(alpha_) / sin(alpha_)))
    
        x = float(A * rad * sin(beta) * cos(theta) * D)
        y = float( A * rad * sin(beta) * sin(theta))
        z = float(-A * rad * cos(beta))
     
        spiral_i = PVector(x,y,z)
        spiral_matrix.append(spiral_i)        
        i = i + 1  #for some reason i += 1 does not work here. It may be a processing thing. 
    return (spiral_matrix) 
 
# Point cloud rendering below 
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

  spiral_points= generateSpiral(BoatEarMoonPresets())

  for vertex in spiral_points: 
        stroke(0,0,255)
        strokeWeight(10)
        x,y,z = vertex[0],vertex[1],vertex[2]
        point(x,y,z)
