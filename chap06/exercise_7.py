# Me Computer, Mandalay.
# June 17, 2022
# exercise_7.py
# This program computes the nth fibonacci sequence given by user

def fibo(n):
    curr, prev = 1,1
    for i in range(n-2):
        curr, prev = curr+prev, curr
    return curr

def main():
    print("Nth Fibonacci number\n")
    n = int(input("Enter n: "))
    print("The Fibonacci value is", fibo(n))

main()

