

int currentFrame = 0;

void setup(){
  size(600,600,P3D); 
  frameRate(24);
}

void draw(){
  background(255,255,255);
  currentFrame = currentFrame + 1;
  
  float fov = PI/3;
  float cameraZ = (height/2.0) / tan(fov/2.0);
  perspective(fov, float(width)/float(height), cameraZ/10.0, cameraZ*10.0); 
  
  translate(300,300);
  rotateY(currentFrame/24.0);

  stroke(255,0,0);
  strokeWeight(10);
  point(0,0,0);
  point(0,100,0);
  point(0,100,100);
  point(100,0,100);
  point(100,100,0);
  point(100,0,0);
  
}
