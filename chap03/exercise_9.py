# ME Computer, Mandalay.
# June 14, 2020
# exercise_9.py
# This program calculates the area of a triangle given the length of three sides

#  9. Write a program to calcualte the area of a triangle given the length of its 
#     three sides - a, b, and c - using these formulas:
#       s = (a + b + c) / 2
#       A = sqrt(s(s - a)(s - b)(s - c))

import math

def main():
    print("This program calculates the are of a triangle.")
    print()

    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))
    
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    print()
    print("The area is", area, "square units.")

main()