# cball1.py
# angle = 53.1, vel = 37, height = 0 ==> Range = 134, max_height = 44.7, time = 6.59

from math import sin, cos, radians

def main():
    angle = eval(input("Enter the launch angle (in degrees) (e.g. 53.1): "))
    vel = eval(input("Enter the initial velocity (in meters/sec) (e.g. 37): "))
    h0 = eval(input("Enter the initial height (in meters) (e.g. 0): "))
    t = eval(input("Enter the time interval between position calculations: "))

    # convert angel to radians
    theta = radians(angle)

    # set the initial position and velocities in x and y directions
    xpos = 0
    ypos = h0
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)
    print(xvel, yvel)

    # loop until the ball hits the ground
    alpha = .00001
    time = 0
    t = 0
    max = ypos
    while ypos >= 0:
        # calculate position and velocity in time seconds
        xpos = xpos + time * xvel
        yvel1 = yvel - time * 9.8
        ypos = ypos + time * (yvel + yvel1)/2
        yvel = yvel1
        time += alpha
        
        if ypos > max:
            max = ypos
            t = time     
        
    print(xpos, ypos)
    print()
    
    print(f"\nDistance traveled: {xpos:0.0f} meters in {time*600} sec.")
    print(f"max height: {max:0.1f} meters at {int(t*600)} ses.")

main()
