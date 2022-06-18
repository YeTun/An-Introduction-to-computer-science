# ME Computer, Mandalay.
# June 12, 2022
# exercise_6b.py
# Chaos program with 3 algebraically equivalent expressions

print("This Program ilustrates a chaotic function")

n = eval(input("How many numbers should I print? "))
x = eval(input("Enter a value between 0 and 1: "))

for i in range(n):
    x = 3.9 * (x - x * x)
    print(x)
