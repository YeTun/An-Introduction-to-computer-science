# ME Computer, Mandalay.
# June 12, 2022
# exercise_5.py
# Chaos program that prints a variable number of terms

print("This Program ilustrates a chaotic function")
n = eval(input("How many numbers should I print? "))
x = eval(input("Enter a number between 0 and 1: "))

for i in range(n):
    x = 3.9 * x * (1 - x)
    print(x)
