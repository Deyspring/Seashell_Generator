"""
Shell generator 
by Roe Dey

"""
import math  
    
def generateShell(n,m):
    """ Generate shell mesh from passed variables"""
    #testing presets
    n = 4
    m = 3
    turns = 10
    s= 0
    # Boat ear moon presets
    i = 1
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
    
    #Adjust resolution of mesh for number of shell turns
    n = int( n * turns / 10.0) 
    spiral = PVector(n)# Pvector: a Processing class describing a 2D or 3D dimensional vector with magnatude and direction, creates a,b,c variablesspiral_row =[45]
    spiral_matrix=[]
    shell_matrix =[]
    shell = PVector(n,m) #Pvector 
    #print ("spiral, shell", spiral, shell)
    
    #Get vertices for the shell
    i= 0
    while i < n: 
        #Generate main spiral
        theta = float(map(i, 0, n, 0, turns))
        rad = float(exp(theta * cos(alpha) / sin(alpha)))
    
        x = float(A * rad * sin(beta) * cos(theta) * D)
        y = float( A * rad * sin(beta) * sin(theta))
        z = float(-A * rad * cos(beta))
     
        #spiral[i] = new PVector(x, y, z); place new Pvector at spiral array position i
        spiral_i = PVector(x,y,z)
        spiral_matrix.append(spiral_i)
       
    # Generate ellipse around each point of a spiral
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
            #translation to python
            #shell array[i position in array][j position in array] - does this mean a value is appended at i and a different value at j, or is i,j a description of one point in th array? 
            #PVector v3 = PVector.add(v1, v2) - add method is being used here. 
            shell = PVector.add(spiral_i, PVector(x, y, z))
            shell_matrix.append(shell) 
            
            j += 1 
        i += 1 
        
        #print ("spiral_matrix", spiral_matrix )
        #print ("shell_matrix ", shell_matrix)
        return (spiral_matrix, shell_matrix) 
        #return (shell_matrix) 

#def spiral():
    return [(0,0,0),(0,100,0),(0,100,100),(100,0,100),(100,100,0),(100,0,0)] 

"""def generateMesh(n,m):
    Create mesh from vertex data returned by generateShell function

    #Adjust resolution of mesh for number of shell turns.
    n = int(n * turns / 20.0)

    #Vertices
    vertices = [float[ n * m ],[3]]
    index = 0
        i = 0
        while i < n:
            j = 0
            while j < m:
                vertices[0] = shell[i][j].x #? 
                vertices[1] = shell[i][j].y
                vertices[2] = shell[i][j].z
             index++
            j += 1
        i += 1
  
    #Faces
    index = 0
    faces = [ int[ (n-1)*m ],[4] ]
    j = 0
    while j < n-1:
         i = 0
         while i < m:
            faces[0] = [i + m * j]
            faces[1] = [(i + 1) % m + m * j]
            faces[2] = [(i + 1) % m + m * (j + 1)]
            faces[3] = [i + m * (j + 1)]
        index++
        i += 1
    j += 1

    #HE_mesh creator - research this library? it may not be available to python
    HEC_FromFacelist creator=new HEC_FromFacelist()
    creator.setVertices(vertices)
    creator.setFaces(faces)
    creator.setDuplicate(false)
    mesh = new HE_Mesh(creator)"""
    
# Spiral function for point cloud testing
#def spiral():
#    return [(0,0,0),(0,100,0),(0,100,100),(100,0,100),(100,100,0),(100,0,0)] 
  
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
  
  #point_list = spiral()
  spiral_points, shell_points = generateShell(2,3)
  #spiral_point_list = generateShell(2,3)
  for vertex in shell_points:
        stroke(255,0,0)
        strokeWeight(10)
        x,y,z = vertex[0],vertex[1],vertex[2]
        point(x,y,z)
  
  for vertex in spiral_points: 
        stroke(0,0,255)
        strokeWeight(10)
        x,y,z = vertex[0],vertex[1],vertex[2]
        point(x,y,z)

    


#generateShell(2,3) # Don't forget to un-comment this if you want a list of points to be generated. 
