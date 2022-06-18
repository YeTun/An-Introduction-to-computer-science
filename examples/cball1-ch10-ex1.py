import math

def main():
    angle = eval(input("Enter the launch angle (in degrees): "))
    vel = eval(input("Enter the initial velocity (in meters/sec): "))
    h0 = eval(input("Enter the initial height (in meters): "))
    time = eval(input("Enter the time interval between position calculations: "))

    xpos = 0.0
    ypos = h0

    theta = math.radians(angle)
    xvel = vel * math.cos(theta)
    yvel = vel * math.sin(theta)

    while ypos >= 0.0:
        xpos = xpos + time * xvel
        yvel1 = yvel - time * 9.8
        ypos = ypos + time * (yvel + yvel1) / 2.0
        yvel = yvel1

    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))

main()