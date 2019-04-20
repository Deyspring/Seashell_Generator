"""
Shell oval function
"""
import math  

def BoatEarMoonPresets():
    """ Variables for the creation of a Boat Ear Moon Shell"""
    # variables to set the resolution of the shell mesh 
    n = 40 # Increasing n,m does not make the shell bigger but does increase the resolution of the spirals 
    m = 40
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
        theta = float(map(i, 0, n, 0, turns))
        rad = float(exp(theta * cos(alpha_) / sin(alpha_)))
    
        x = float(A * rad * sin(beta) * cos(theta) * D)
        y = float( A * rad * sin(beta) * sin(theta))
        z = float(-A * rad * cos(beta))
     
        spiral_i = PVector(x,y,z)
        spiral_matrix.append(spiral_i)        
        i = i + 1  #for some reason i += 1 does not work here. It may be a processing thing. 
    return (spiral_matrix, theta, rad) 
 
    
def generateOval(presets, spiral_points):
    """ Generates ovals around spiral points?"""
    n,m,turns,s,i,D, alpha_, beta,phi, mu, omega,A, a, b, L, P, W1, W2,N = presets
     
    # From spiral function - figure out the way to pass these properly 
    theta = float(map(i, 0, n, 0, turns))
    rad = float(exp(theta * cos(alpha_) / sin(alpha_)))

    spiral = spiral_points
    shell =[]
    shell_matrix= []
    # Generate ellipse around each point of the spiral
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
            r2 += surfrad# loop end here? or one indent left
        
        x = cos(s + phi) * cos(theta + omega) * r2 * rad * D   # here  rad - 1 closes the opening of the curve at the origin
        y = cos(s + phi) * sin(theta + omega) * r2 * rad
        z = sin(s + phi)                      * r2 * rad
        
        # adjust orientation of the ellipse? so shell doesn't flatten out to a ribbon?
        x -= sin(mu) * sin(s + phi) * sin(theta + omega) * r2
        y += sin(mu) * sin(s + phi) * cos(theta + omega) * r2
        z *= cos(mu)
        
        #sp_x, sp_y, sp_z = spiral[j]  # 
        #spv1 = PVector(sp_x, sp_y, sp_z)
        #shell = PVector.add(spv1, PVector(x, y, z)) # this generates another spiral 
        
        shell = PVector(x,y,z) #this generates an oval 
        shell_matrix.append(shell) 
            
        j = j+ 1 
        
    return shell_matrix 
        
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
  print ("spiral_points", spiral_points[0]) 

  for vertex in spiral_points[0]: 
        print ("vertex", vertex) 
        stroke(0,0,255)
        strokeWeight(10)
        x,y,z = vertex[0],vertex[1],vertex[2]
        print ("x,y,z", x,y,z) 
        point(x,y,z)
  
  oval_points = generateOval(BoatEarMoonPresets(), spiral_points[0])

  for vertex in oval_points:
        stroke(255,0,0)
        strokeWeight(10)
        x,y,z = vertex[0],vertex[1],vertex[2]
        point(x,y,z)
