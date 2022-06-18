# Me Computer, Mandalay.
# June 21, 2022
# exercise_1.py
# Modification of cannonball to compute max height
# angle = 53.1, vel = 37, height = 0 ==> Range = 134.2, max_height = 44.7, time = 6.59

from projectile import Projectile

def getInputs():
    a = float(input("Enter the launch angle (in degrees): "))
    v = float(input("Enter the initial velocity (in meters/sec): "))
    h = float(input("Enter the initial height (in meters): "))
    t = float(input("Enter the time interval between position calculations: "))
    return a,v,h,t

def main():
    print("Cannonball Simulation\n")
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    maxHeight = h0
    while cball.getY() >= 0:
        cball.update(time)
        if cball.getY() >maxHeight:
            maxHeight = cball.getY()
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))
    print("Maximum height: {0:0.1f} meters.".format(maxHeight))

if __name__ == "__main__": main()