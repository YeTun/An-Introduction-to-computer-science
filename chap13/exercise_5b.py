# ME Computer, Mandalay.
# June 24, 2022
# exercise_5.py

def baseConversion(num, base):
    digit = num % base
    print(num, digit)
    num = num // base
    
    if num == 0:
        return 1
    elif num < base:
        digit = num
        num = 0
        print(num, digit)
    else:
        baseConversion(num, base)

baseConversion(153, 10)

print()
baseConversion(1234, 16)

print()
baseConversion(192, 2)

        

