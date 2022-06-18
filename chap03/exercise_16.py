# ME Computer, Mandalay.
# June 14, 2022
# exercise_16.py
# this program computes the nth fibonacci sequence given by user

# 16. A Fibnoacci sequence is a sequence of numbers where each successive number is the sum 
#     of the previous two. The classic Fibonacii sequence begins: 1, 1, 2, 3, 5, 8, 13, .... 
#     Write a program that computes the nth Fibonacci number where n is a value input by the 
#     user. For example, if n = 6, then the result is 8.

def main():
    print("This program computers the nth Fibonacci number.")
    n = int(input("Enter the number of terms: "))
    
    a, b = 1, 1
    num = n - 2
    for i in range(num):
        a, b = b, a+b
    
    print(f"The Fibonacci number of {n} is {b}.", end=" ")
    print(f"(if n = {n}, then the result is {b}.)")

main()
