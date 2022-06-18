# Me Computer, Mandalay.
# June 17, 2022
# exercise_8.py
# This program computes the square root of n given by user

from math import sqrt

def nextGuess(guess, x):
    guess = (guess + x / guess) / 2
    return guess

def main():
    print("This program approximates a number's square root.")
    print("The first guess is n / 2, followed by (guess + n/guess) / 2.")
    n = int(input("Enter a number: "))
    nGuesses = int(input("Enter the number of guesses: "))
    for i in range(nGuesses):
        if i < 1:
            guess = n / 2
        else:
            guess = nextGuess(guess, n)
    
    print(f"The guess is: {guess:0.2f}")
    print("The actual root is: {0:0.2f}".format(sqrt(n)))
    print("The difference is: {0:0.2f}".format(sqrt(n) - guess))

main()

# import math as m

# def nextGuess(guess, x):
#     g = (guess + x / guess) / 2
#     return g

# def main():
#     x = eval(input("Find the square root of: "))
#     y = eval(input("How many iterations of Newton's formula would you like?: "))

#     g = x / 2    
#     for i in range (y):
#         g = nextGuess(g, x)
#     print(g)    

# main()
