# Me Computer, Mandalay.
# June 21, 2022
# exercise_1.py

from projectile import Projectile

def getInputs():
    angle = eval(input("Enter the launch angle (in degrees): "))
    vel = eval(input("Enter the initial velocity (in meters/sec): "))
    h0 = eval(input("Enter the initial height (in meters): "))
    time = eval(input("Enter the time interval between position calculations: "))
    return angle, vel, h0, time

def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    
    maxHeight = cball.getY()
    while cball.getY() >= 0:
        cball.update(time)
        if cball.getY() > maxHeight:
            maxHeight = cball.getY()
    
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))
    print("Maximum height: {0:0.1f} meters".format(maxHeight))

main()
