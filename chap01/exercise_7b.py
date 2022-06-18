# ME Computer, Mandalay.
# June 12, 2022
# exercise_7b.py
# Chaos program to print values in chart form side-by-side
# This is ugly and not secure

print("Ths program illustrates a chaotic function")

x, y = eval(input("Enter 2 numbers between 0 and 1 separated by a comma: "))

print("input   ", x, "         ", y, " ")
print("---------------------------")

for i in range (10):
    x = 3.9 * x * (1 - x)
    y = 3.9 * y * (1 - y)
    
    print(round(x, 7), "   ", y)
