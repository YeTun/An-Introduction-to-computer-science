# ME Computer, Mandalay.
# June 14, 2022
# exercise_7.py
# This program determines the distance between two points

#  7. Write a program that accepts two points (see previous problem) and determins 
#     the distance between them.
#       distances = sqrt((x2 - x1)^2 + (y2 - y1)^2)

from math import sqrt

def main():
    print("Program calculates the distance between 2 cartesian coordinates.")
    x1 = int(input("Enter X1: "))
    y1 = int(input("Enter Y1: "))
    x2 = int(input("Enter X2: "))
    y2 = int(input("Enter Y2: "))
    
    distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)

    print("The slope of the line between the points is:", round(distance, 2))

main()
