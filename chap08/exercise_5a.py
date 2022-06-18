# Me Computer, Mandalay.
# June 19, 2022
# exercise_5.py
# This program validates input n as a prime number. The program will close
# if it finds n to be divisible by any number other than 1 and itself.

from math import sqrt

def main():
    print("This program tests if a number (n > 2) is prime.")
    testPrime = int(input("Enter a positive whole number greater than 2: "))
    
    n = 2
    while (testPrime % n != 0) and (n <= sqrt(testPrime)):
        n += 1
    if testPrime % n == 0:
        print(f"{testPrime} is evenly divided by {n}.")
    else:
        print(f"{testPrime} is prime.")

main()
