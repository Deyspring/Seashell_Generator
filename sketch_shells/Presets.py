#Functions to populate SeashellGenerator with preset variables for different shells
import math

def resMode(mode):
    """ Sets the resolution of the mesh generated """ 
    if mode==0:
        makeMesh(r0x, r0y)
    elif mode==1:
        makeMesh(r1x, r1y)
    elif (mode==2):
        makeMesh(r2x, r2y)


def BoatEarMoon():
    """ Variables for the Boat Ear Moon shell """
    D=1
    alpha=math.radians(83)
    beta=math.radians(42) 
    phi=math.radians(70) 
    mu=math.radians(10) 
    omega=math.radians(30) 
    A=25, a=12, b=20, L=0, P=0, W1=0, W2=0, N=0
  
    resMode()


