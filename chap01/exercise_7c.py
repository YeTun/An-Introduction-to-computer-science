# ME Computer, Mandalay.
# June 12, 2022
# exercise_7c.py
# More secure version with bad formatting

print("Ths program illustrates a chaotic function")

x = float(input("Enter first number between 0 and 1: "))
y = float(input("Enter second number between 0 and 1: "))

print("input   ", x, "         ", y, " ")
print("---------------------------")

for i in range (10):
    x = 3.9 * x * (1 - x)
    y = 3.9 * y * (1 - y)
    print(x, "   ", y)
