# Me Computer, Mandalay.
# June 19, 2022
# exercise_7.py
# Goldbach conjecture
# Every even number is the sum of two prime numbers
# This program gets a number from the user, validates it being even,
# then finds two primes that add up to that number

from math import sqrt

def isPrime(testValue):
    n = 2
    while (testValue % n != 0) and (n <= sqrt(testValue)):
        n += 1
    if testValue % n == 0:
        return False
    else:
        return True

def main():
    print("This program takes an even number and finds two prime numbers which")
    print("add up to the even number.")
    evenNumber = int(input("Enter an even number: "))
    
    if evenNumber % 2 != 0:
        print("The number is not even.")
    else:
        n = 2
        while (n <= evenNumber/2) and not (isPrime(n) and isPrime(evenNumber - n)):
            n += 1
        
        print(f"{n} and {evenNumber-n} sum up to {evenNumber} and are prime.")

main()
