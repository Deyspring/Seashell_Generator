"""
Shell generator 
by Roe Dey

"""
import math

"""
location = PVector(100, 100)  # Location of shape
#velocity = PVector(1.5, 2.1)  # Velocity of shape
#gravity = PVector(0, 0.2)  # Gravity acts at the shape's acceleration.


def setup():
    size(200, 200)
    smooth()

def draw():
    background(200,200,200)
    # Add velocity to the location.
    #location.add(velocity)
    # Add gravity to velocity.
    #velocity.add(gravity)
    # Bounce off edges.
    #if location.x < 0 or location.x > width:
      #  velocity.x = velocity.x * -1
    #if location.y > height:
        # We're reducing velocity ever so slightly
        # when it hits the bottom of the window.
       # velocity.y = velocity.y * -0.95
        #location.y = height
    # Display circle at location vector.
    stroke(255)
    strokeWeight(0)
    fill(0,10,0)
    #ellipse(location.x, location.y, 48, 48)
    
    
"""    
    
def generateShell(n,m):
    """ Generate shell mesh from passed variables"""
    #testing presets
    n = 10
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
    spiral = PVector(n)# Pvector: a class describing a 2D or 3D dimensional vector with magnatude and direction, creates a,b,c variables
    spiral_row =[]
    shell = PVector(n,m) #Pvector, not sure how to import or link to this module, it's from Processing
    #print ("spiral, shell", spiral, shell)
    #ellipse(location.x, location.y, n, m)
    
    #Get vertices for the shell
    i = 0
    while i < n: 
        #Generate main spiral
        theta = float(map(i, 0, n, 0, turns))
        rad = float(exp(theta * cos(alpha) / sin(alpha)))
    
        x = float(A * rad * sin(beta) * cos(theta) * D)
        y = float( A * rad * sin(beta) * sin(theta))
        z = float(-A * rad * cos(beta))
     
        #spiral[i] = new PVector(x, y, z); ????
        vector = PVector(x, y, z)
        spiral_row.append(vector)
        #i += 1 # temp loop 
    #print ("spiral matrix:", spiral_row) 

    # Generate ellipse around each point of a spiral
        j = 0 
        if j < m: 
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
      
            #shell[i][j] = PVector.add(spiral[i], PVector(x, y, z)) - Java multidimentional array 
            spiral =[i]
            oval = [PVector(x,y,z)]
            shell = [[spiral],[oval]]
        
        j+= 1 
    i += 1 

    print ("spiral", spiral) 
    print ("oval", oval)
    print ("shell", shell) 
    
generateShell(1,2)
