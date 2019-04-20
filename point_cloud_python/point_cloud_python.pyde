
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
  
  point_list = spiral()
  for vertex in point_list: 
        x,y,z = vertex[0],vertex[1],vertex[2]
        point(x,y,z)

def spiral():
    return [(0,0,0),(0,100,0),(0,100,100),(100,0,100),(100,100,0),(100,0,0)] 
    
        
