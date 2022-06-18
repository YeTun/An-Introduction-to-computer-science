import math

def main():
    angle, vel, h0, time = getInputs()
    xpos, ypos = 0, h0
    xvel, yvel = getXYComponents(vel, angle)
    while ypos >= 0:
        xpos, ypos, yvel = updateCannonBall(time, xpos, ypos, xvel, yvel)
    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))

def getInputs():
    angle = eval(input("Enter the launch angle (in degrees): "))
    vel = eval(input("Enter the initial velocity (in meters/sec): "))
    h0 = eval(input("Enter the initial height (in meters): "))
    time = eval(input("Enter the time interval between position calculations: "))
    return angle, vel, h0, time

def getXYComponents(vel, angle):
    theta = math.radians(angle)
    xvel = vel * math.cos(theta)
    yvel = vel * math.sin(theta)
    return xvel, yvel

def updateCannonBall(time, xpos, ypos, xvel, yvel):
    xpos = xpos + time * xvel
    yvel1 = yvel - time * 9.8
    ypos = ypos + time * (yvel + yvel1) / 2.0
    yvel = yvel1
    return xpos, ypos, yvel

main()