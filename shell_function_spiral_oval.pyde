"""
Shell mesh function
"""
import math  
    
def generateShell(spiral_points):
    """ Generate shell mesh from spiral function"""
    n = 10
    m = 10 # 6 generates a "sort of oval" it might just be two arches 
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
    
    spiral = spiral_points
    shell =[]
    shell_matrix =[]
    
    theta = float(map(i, 0, n, 0, turns))
    rad = float(exp(theta * cos(alpha_) / sin(alpha_)))
    
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
      
        #shell[i][j] = PVector.add(spiral[i], new PVector(x, y, z));
        #shell array[i position in array][j position in array] - does this mean a value is appended at i and a different value at j, or is i,j a description of one point in th array? 

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

  spiral_points= [[ 16.728266, 0.0, -18.57862 ], 
                  [ 10.219092, 15.915295, -21.005745 ], 
                  [ -8.899115, 19.44492, -23.749952 ], 
                  [ -23.936285, 3.4120345, -26.852665 ], 
                  [ -17.8686, -20.688646, -30.36072 ], 
                  [ 8.767497, -29.638655, -34.32707 ], 
                  [ 33.554214, -9.764483, -38.811584 ], 
                  [ 29.787807, 25.958525, -43.88196 ], 
                  [ -6.499968, 44.197906, -49.614735 ], 
                  [ -46.020702, 20.815886, -56.096443 ]]
  
  
  shell_points = generateShell(spiral_points)

  for vertex in shell_points:
        stroke(255,0,0)
        strokeWeight(10)
        x,y,z = vertex[0],vertex[1],vertex[2]
        point(x,y,z)
