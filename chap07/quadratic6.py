# quadratic.py
# A program that computes the real roots of a quadratic equation.
# Note: this program crashes if the equation has no real roots.

import math # Makes the math library available

def main():
    print("This program finds the real solutions to a quadratic\n")

    try:
        a = float(input("Please enter coefficients a: "))
        b = float(input("Please enter coefficients b: "))
        c = float(input("Please enter coefficients c: "))

        discrim = b * b - 4 * a * c
        discRoot = math.sqrt(discrim)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        
        print("The solutions are:", root1, root2 )
    
    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("\nNo real roots.")
        else:
            print("Invalid coefficient given")
    except:
        print("\n Something went wrong, sorry!")

main()
