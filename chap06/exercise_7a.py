# Me Computer, Mandalay.
# June 17, 2022
# exercise_7.py
# This program computes the nth fibonacci sequence given by user

def fib(n):
    a, b = 0, 1
    num = n-1
    for i in range(num):
        a, b = b, a+b
    return b
        
def main():
    print("This program calculates the nth Fibonacci sequence number")
    n = int(input("Enter the fibonacci number you want to be calulated: "))

    print(f"The Fibonacci number of {n} is {fib(n)}")

main()


# def fibonnaci(n):
#     x, y, z = 0, 1, 0

#     for i in range (n - 1):
#         z = x + y
#         x, y = y, z
#         # print(x, y)
#     return y

# def main():
#     n = eval(input("What number in the Fibonnaci sequence would you like to see?: "))
#     f = fibonnaci(n)
    
#     print(f"The {n} Fibonnaci number is {f}.")

# main()
