from projectile_ch10_ex6 import Projectile

def getInputs():
    angle = eval(input("Enter the launch angle (in degrees): "))
    vel = eval(input("Enter the initial velocity (in meters/sec): "))
    h0 = eval(input("Enter the initial height (in meters): "))
    time = eval(input("Enter the time interval between position calculations: "))
    return angle, vel, h0, time

def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time)
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))

main()