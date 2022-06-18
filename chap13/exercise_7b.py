# ME Computer, Mandalay.
# June 24, 2022
# exercise_7.py

import sys
sys.setrecursionlimit(1000)

def factorial(n):
    fact = 1
    for factor in range(n, 1, -1):
        fact = fact * factor
    return fact

def iterative_options(n, k):
    x = factorial(n)
    y = factorial(k) * factorial(n-k)
    return x // y   # choices are counting number

def recursive_options(n, k):
    if k == 1:
        options = n
    elif n < k:
        options = 0
    else:
        options = recursive_options(n-1, k-1) + recursive_options(n-1, k)
    return options

def main():
    # print(iterative_options(72, 5))
    # print(recursive_options(72, 5))
    print(iterative_options(6, 2))
    print(recursive_options(6, 2))

main()
    