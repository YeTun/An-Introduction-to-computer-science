# cball2.py
# Simulation of the flight of a cannonball (or other projectile)
# This version uses functional (top-down) composition.

from math import pi, sin, cos

def getInputs():
    a = float(input("Enter the launch angle (in degrees): "))
    v = float(input("Enter the initial velocity (in meters/sec): "))
    h = float(input("Enter the initial height (in meters): "))
    t = float(input("Enter the time interval between position calculations: "))
    return a,v,h,t

def getXYComponents(vel, angle):
    radians = (angle * pi)/180.0
    x = vel * cos(radians)
    y = vel * sin(radians)
    return x,y

def updateCannonBall(time, xpos, ypos, xvel, yvel):
        xpos = xpos + time * xvel
        yvel1 = yvel - 9.8 * time
        ypos = ypos + time * (yvel + yvel1)/2.0
        return xpos, ypos, yvel1
     
def main():
    angle, vel, h0, time = getInputs()
    xpos, ypos = 0, h0
    xvel, yvel = getXYComponents(vel, angle)
    while ypos >= 0:
        xpos, ypos, yvel = updateCannonBall(time, xpos, ypos, xvel, yvel)
    
    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))

if __name__ == "__main__": main()


