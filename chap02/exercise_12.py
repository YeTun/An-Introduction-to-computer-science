# ME Computer, Mandalay.
# June 13, 2022
# exercise_12.py

# 12. Write an interactive Python calculator program. The program should allow the user 
#     to type a mathematical expression, and then print the value of the expression. 
#     Include a loop so that the user can perform many calculations (say, up to 100). 
#     Note: To quit early, the user can make the program crash by typing a bad expression 
#     or simply closing the window that the calculator program is running in. 
#     You'll learn better ways of terminating interactive programs in later chapters.

def main():

# Explain the program
    print("------------------------------------------------")
    print("This program works as a mathematical calculator.")
# Explain how to enter expression
    print("It can add (+), subtract (-), multiply (*), divide (/),")
    print("use exponents (**), and modulus (//).")
    print("Enter a mathematical expression when prompted. E.g. 1000*10+5/22")
    print("The program will print out the answer then prompt for another expression.")
# Explain how to quit
    print("To quit, type 'quit()'.")

# Loop 100 times
    for j in range(100):
        # Prompt user for expression to calculate
        ans = eval(input("Type in a mathematical expression: "))
        # Print out answer
        print("The answer is", ans)

main()
