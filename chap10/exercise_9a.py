# Me Computer, Mandalay.
# June 21, 2022
# exercise_9.py

from sphere import Sphere

def main():
    print("This program calculates the volume and surface area of a sphere.")
    
    radius = eval(input("Please enter a radius: "))
    sphere = Sphere(radius)

    print(f"The volume of your sphere is {sphere.volume():0.1f}.")
    print(f"And the area of your sphere is {sphere.surfaceArea():0.1f}.")

main()
