# ME Computer, Mandalay.
# June 14, 2022
# exercise_6.py
# This program calculate the slope between two points of a plane

#  6. Two points in a plane are specified using the coordinates (x1, y1) and (x2, y2). 
#     Write a program that calculates the slope of a line through two (non-vertical)
#     points entered by the user.
#           slope = (y2 - y1) / (x2 - x1)

def main():
    print("This program calculates the slope between 2 cartesian coordinates.")
    x1 = int(input("Enter X1: "))
    y1 = int(input("Enter Y1: "))
    x2 = int(input("Enter X2: "))
    y2 = int(input("Enter Y2: "))
    
    slope = (y2 - y1) / (x2 - x1)

    print("The slope of the line between the points is:", round(slope, 2))
    
main()
