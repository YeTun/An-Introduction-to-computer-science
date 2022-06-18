# ME Computer, Mandalay.
# June 12, 2022
# exercise_6.py
# Chaos program with 3 algebraically equivalent expressions

'''
Output comparison for .23 shows that algebraically equivalent expressions do not return
the same outputs when the input values are a floating-point data type. This is because of
rounding errors implicit in floats.
'''

print("This program is an experiment.")
a = eval(input("Enter a number between 0 and 1: "))
b = a
c = a

for i in range(10): # range(100)
    a = 3.9 * a * (1 - a)
    b = 3.9 * (b - b * b)
    c = 3.9 * c - 3.9 * c * c
    print("{0:<30.20}{1:<30.20}{2:<30.20}".format(a, b, c))
