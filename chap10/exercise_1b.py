# Me Computer, Mandalay.
# June 21, 2022
# exercise_1.py

from projectile import Projectile

def getInputs():
    a = eval(input("Enter the launch angle (in degrees): "))
    v = eval(input("Enter the initial velocity (in meters/sec): "))
    h = eval(input("Enter the initial height (in meters): "))
    return a, v, h

def main():
    angle, vel, h0 = getInputs()
    cball = Projectile(angle, vel, h0)
    
    alpha = .0001
    maxY = h0  
    time = 0
    t = 0
    while cball.getY() >= 0:
        cball.update(time*alpha)

        if cball.getY() > maxY:
            maxY = cball.getY()
            t = time
        
        time += 1
    print(cball.getX(), cball.getY(), time)
    
    print(f"\nDistance traveled: {cball.getX():0.1f} meters.")
    print(f"The time interval before hitting the ground {time/60:0.1f} sec.")
    print(f"\nThe maximum height achieved by the cannonball: {maxY:0.1f} meters at {t/60:0.1f} sec.")

main()
