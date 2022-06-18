# Me Computer, Mandalay.
# June 17, 2022
# exercise_8.py
# square roots

from math import sqrt

def nextGuess(guess, x):
    return (guess + x/guess) / 2.0

def sqrRoot(x, iters):
    guess = x / 2.0
    for i in range(iters):
        guess = nextGuess(guess, x)
    return guess
    

def main():
    x = float(input("Enter the value to take the root of: "))
    n = int(input("Enter the number of iterations: "))
    print("Square root is", sqrRoot(x, n))
    
    print("The actual root is: {0:0.15f}".format(sqrt(x)))
    print("The difference is: {0:0.15f}".format(sqrt(x) - sqrRoot(x, n)))

main()