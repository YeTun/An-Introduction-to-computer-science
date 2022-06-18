# File: chaos.py
# A simple program illustrating chaotic behavior.

print("This Program ilustrates a chaotic function")
x = eval(input("Enter a number between 0 and 1: "))

for i in range(10):
    x = 3.9 * x * (1 - x)   # k(x)*(1-x)
    print(x)