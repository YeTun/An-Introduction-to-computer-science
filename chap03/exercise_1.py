# ME Computer, Mandalay.
# June 14, 2022
# exercise_1.py
#   Program to calculate the volume and surface area of a sphere

#  1. Write a program to calculate the volume and surface area of a sphere from its radius, 
#     given as input. Here are some formulas that might be useful:
#       V = (4/3)3pir^3
#       A = 4pir^2

from math import pi

def main():
    print("Program calculates the vol. & surface area of a sphere given the radius.")
    radius = float(input("Enter the radius of a sphere: "))

    volume = 4 / 3 * pi * radius**3     # Volume formula
    area = 4 * pi * radius**2           # Area formula

    print(f"The volume of the sphere is {volume}.")
    print(f"The area of the sphere is {area}.")

main()
