# Me Computer, Mandalay.
# June 19, 2020
# exercise_8.py
# Euclid's algorithm
# User inputs 2 values, m and n
# repeat formula n, m = m, n % m until m == 0
# Output n as the GCD of two numbers

def main():
    m, n = eval(input("Please enter 2 numbers, separated by a comma: "))

    try:
        if m < n:
            y = n
            m, n = y, m
            
        while m != 0:
            y = m
            m, n = n % m, y
        
        print("The GCD is {}".format(n))

    except TypeError:
        print("The input must be numerical.")

main()
