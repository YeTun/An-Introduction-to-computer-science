# Me Computer, Mandalay.
# June 19, 2022
# exercise_6.py
# primes to n

from exercise_5 import isPrime

def main():
    print("This program finds all prime numbers up to N\n")
    n = int(input("Enter the upper limit, n: "))
    print("primes: ", end=' ')
    for i in range(2,n+1):
        if isPrime(i):
            print(i, end=' ')
    print("Done")

if __name__ == '__main__': main()
