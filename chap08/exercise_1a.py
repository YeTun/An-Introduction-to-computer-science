# Me Computer, Mandalay.
# June 19, 2022
# exercise_1.py

def main():
    print("This program computes the n-th Fibonacci number, n is specified.")
    n = int(input("Enter the n-th Fibonacci number to calculate [1-999,999]: "))
    
    x = 1
    y = 0
    count = 0
    while count < n:
        z = x + y
        x, y = y, z
        count += 1
    
    print(f"The {n} Fibonacci is: {z}")

main()
