# ME Computer, Mandalay.
# June 12, 2022
# exercise_4.py
# Chaos program amended to produce output sequence of 20 terms

print("This Program ilustrates a chaotic function")
x = eval(input("Enter a number between 0 and 1: "))

for i in range(20):
    x = 3.9 * x * (1 - x)
    print(x)
