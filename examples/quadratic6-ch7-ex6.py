import math

def main():
    print("This program finds the real solutions to a quadratic.")
    print()

    try:
        a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print()
        print("The solutions are:", root1, root2)
    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("\nThe equation has no real roots.")
        else:
            print("You didn't give me the right number of coefficients")
    except NameError:
        print("\nYou didn't enter three numbers.")
    except TypeError:
        print("\nYour inputs were not all numbers.")
    except SyntaxError:
        print("\nYour input was not in the correct form. Missing comma?")
    except:
        print("\nSomething went wrong")


main()