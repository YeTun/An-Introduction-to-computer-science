# ME Computer, Mandalay.
# June 13, 2022
# exercise_9.py

#  9. Write a program that converts temperatures from Fahrenheit to Celsius.

# convert2.py
#     A program to convert Fahrenheit temps to Celsius
# by: Susan Computewell

def main():
    print("This program converts Fahrenheit temperature to Celsius.")
    
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = (fahrenheit - 32) * 5/9
    
    print("The temperature is", celsius, "degrees Celsius.")
    input("Press the <Enter> key to quit.")

main()

