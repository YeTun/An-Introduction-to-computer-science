# Me Computer, Mandalay.
# June 17, 2022
# exercise_3.py
# Program to calculate the volume and surface area of a sphere

from math import pi

def sphereArea(radius):
    area = 4 * pi * radius**2       # Area formula
    return area

def sphereVolume(radius):
    volume = (4/3 * pi * radius**3) # Volume formula
    return volume

def main():
    print("The program calculates the volume and surface area of a sphere")
    r = float(input("What is the radius of the sphere: "))

    vol = sphereVolume(r)
    area = sphereArea(r)

    print(f"The volume of the sphere is {round(vol, 2)}.")
    print(f"The surface area of the sphere is {area:0.2f}.")

main()


# import math as m

# def sphereArea(radius):
#     area = 4 * m.pi * (radius*radius)
#     return area

# def sphereVolume(radius):
#     volume = 4/3 * m.pi * (radius ** 3)
#     return volume

# def main():
#     r = (eval(input("Input a value for the radius: ")))

#     a = sphereArea(r)
#     v = sphereVolume(r)
    
#     print(f"A sphere with radius {r} has volume {round(v, 3)}.")
#     print(f"And surface area {round(a, 3)}.")

# main()
