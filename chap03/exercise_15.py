# ME Computer, Mandalay.
# June 14, 2022
# exercise_15.py

# 15. Write a program tha approximates the value of pi by summing the terms of this series:
#     4/1 - 4/3 + 4/5 = 4/7 + 4/9 - 4/11 + ... The program should prompt the user for n, the 
#     number of terms to sum, and then output the sum of the first n terms of this series. 
#     Have your program subtrac the approximation from the value of math.pi to see how 
#     accurate it is.

import math

def main():
    print("This program evaluates first n-terms of pi to compare them to pi.")
    print("Using the equation: 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11...")    
    n = int(input("How many terms should I use? "))

    total = 0
    sgn = 1     # used to alternate sign of terms
    for denom in range(1, 2*n, 2):
        total = total + sgn * 4/denom
        sgn = -sgn #flip the sign

    print("Approximation to pi is:", total)
    print("math.pi is:", math.pi)
    print("Difference from math.pi:", math.pi - total)

main()