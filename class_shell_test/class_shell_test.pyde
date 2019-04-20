import math

# 3/22 this was the last file worked on

class Shell: 

    def __init__(self, n, m, turns, s, i, D, alpha_, beta, phi, mu, omega, A, a, b, L, P, W1, W2, N ):
        self.n = n
        self.m = m
        self.turns = turns
        self.s = s
        self.i = i
        self.D = D
        self.alpha_ = alpha_
        self.beta = beta
        self.phi = phi 
        self.mu = mu
        self.omega = omega
        self.A = A
        self.a = a
        self.b = b
        self.L = L 
        self.P = P
        self.W1 = W1
        self.W2 = W2
        self.N = N 

    def generateSpiral(self):  
        spiral_matrix=[]
        while self.i < self.n: 
            
            theta = float(map(self.i, 0, self.n, 0, self.turns))
            rad = float(exp(theta * cos(self.alpha_) / sin(self.alpha_)))
    
            x = float(self.A * rad * sin(self.beta) * cos(theta) * self.D)
            y = float(self.A * rad * sin(self.beta) * sin(theta))
            z = float(-self.A * rad * cos(self.beta))
  
            spiral_i = PVector(x,y,z)
            spiral_matrix.append(spiral_i) 

            self.i = self.i + 1  #for some reason i += 1 does not work here. It may be a processing thing. 
        return spiral_matrix, theta, rad

    def generateSpline(self, theta, rad):
        # can't figure out how to pass theta and rad to this function, hard coding for now
        #theta = 9.75 
        #rad = 3.310665607452392
        #_, theta, rad = self.generateSpiral() - do not know how to pass theta, rad from generateSpiral
        spline_matrix =[]
        
        self.j = 0 

        while self.j < self.m: 
            s = float(map(self.j, 0, self.m, 0, TWO_PI)) 
            r2 = float(pow( pow(cos(self.s)/self.a,2) + pow(sin(self.s)/self.b,2), -0.5 ))
        
            # add surface manipulations
            surfrad = float(0)
            if (self.W1==0 or self.W2==0 or self.N==0):
                surfrad = 0
            else: 
                lt = float((TWO_PI / self.N) * ( self.N*theta / TWO_PI - int(self.N*theta / TWO_PI) ))
                surfrad = self.L * exp( -( pow(2*(self.s-self.P)/self.W1, 2) + pow(2*lt/self.W2, 2) ) ) 

            r2 += surfrad
        
            x = cos(s + self.phi) * cos(theta + self.omega) * r2 * rad * self.D   # here  rad - 1 closes the opening of the curve at the origin
            y = cos(s + self.phi) * sin(theta + self.omega) * r2 * rad
            z = sin(s + self.phi)                      * r2 * rad
        
            # adjust orientation of the spline so shell doesn't flatten out to a ribbon?
            x -= sin(self.mu) * sin(self.s + self.phi) * sin(theta + self.omega) * r2
            y += sin(self.mu) * sin(self.s + self.phi) * cos(theta + self.omega) * r2
            z *= cos(self.mu)
        
            spline = PVector(x,y,z)
            spline_matrix.append(spline)   

            self.j = self.j+ 1 

        return spline_matrix
            
    def mesh(self,spiral_points, spline_points):
        return  zip(spiral_matrix, spline_matrix) 

def BoatEarMoonPresets():
    #Variables for the creation of a Boat Ear Moon Shell
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


#######################################################

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
  
  boat_var = BoatEarMoonPresets() # Cannot get variables directly into Shell class using BoatEarMoon function - do not know why 
  test = Shell(40, 40, 10, 0, 1, 1, 1.4486232791552935, 0.7330382858376184, 1.2217304763960306, 0.17453292519943295, 0.5235987755982988, 25, 12, 20, 0, 0, 0, 0, 0)
  
  spiral_points = test.generateSpiral()
  #print spiral_points
  spline_points = test.generateSpline(spiral_points[1],spiral_points[2])
  mesh = test.mesh(spiral_points[0], spline_points)


  for vertex in spiral_points[0]: 
        stroke(0,0,255)
        strokeWeight(10)
        x,y,z = vertex[0],vertex[1],vertex[2]
        point(x,y,z)

  for vertex in spline_points:
        stroke(255,0,0)
        strokeWeight(10)
        x,y,z = vertex[0],vertex[1],vertex[2]
        point(x,y,z) 

  for vertex in mesh:
        stroke(0,255,0)
        strokeWeight(10)
        x,y,z = vertex[0],vertex[1],vertex[2]
        point(x,y,z) 

 
