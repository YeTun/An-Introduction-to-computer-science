# cball1.py

from math import sin, cos, radians

def main():
    angle = eval(input("Enter the launch angle (in degrees): "))
    vel = eval(input("Enter the initial velocity (in meters/sec): "))
    h0 = eval(input("Enter the initial height (in meters): "))

    # convert angel to radians
    theta = radians(angle)

    # set the initial position and velocities in x and y directions
    xpos = 0
    ypos = h0
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)

    # loop until the ball hits the ground
    time = 0
    max = h0
    while ypos >= 0:
        # calculate position and velocity in time seconds
        xpos = xpos + time * xvel
        yvel1 = yvel - time * 9.8
        ypos = ypos + time * (yvel + yvel1)/2
        yvel = yvel1
        print(xpos, ypos)

        if ypos > max:
            max = ypos
        time += .001
    
    print(f"\nDistance traveled: {xpos:0.1f} meters.")
    print(f"The time interval before hitting the ground {(time/60)*1000:0.1f} sec.")
    print(f"\nThe maximum height achieved by the cannonball: {max:0.1f} meters.")

main()
