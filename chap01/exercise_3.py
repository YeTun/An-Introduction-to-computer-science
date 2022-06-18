# ME Computer, Mandalay.
# June 12, 2022
# exercise_3.py
# A simple program illustrating chaotic behavior.

print("This Program ilustrates a chaotic function")
x = eval(input("Enter a number between 0 and 1: "))

for i in range(10):
    x = 2.0 * x * (1 - x)
    print(x)

# When the multiplier is 2, the logistic function appears to behave
# in a "less random" fashion.