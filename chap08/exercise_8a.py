# Me Computer, Mandalay.
# June 19, 2022
# exercise_8.py
# Euclid's algorithm
# User inputs 2 values, m and n
# repeat formula n, m = m, n % m until m == 0
# Output n as the GCD of two numbers

def main():
    print("This program finds the greatest common divisor using the Euclidean algorithm.")
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    
    n, m = a, b
    while m != 0:
        n, m = m, n % m
    
    print(f"The greatest common divisor of {a} and {b} is: {n}.")

main()