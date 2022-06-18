# quadratic.py
# A program that computes the real roots of a quadratic equation.
# Illustrates use of the math library
# Note: this program crashes if the equation has no real roots
#        ValueError: math domain error

import math # Makes the math library available

def main():
    print("This program finds the real solutions to a quadratic")
    print()

    a = float(input("Please enter coefficients a: "))
    b = float(input("Please enter coefficients b: "))
    c = float(input("Please enter coefficients c: "))

    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print()
    print("The solutions are:", root1, root2 )

main()
