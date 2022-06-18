# ME Computer, Mandalay.
# June 13, 2022
# exercise_1.py

#  1. A user-friendly program should print an introduction that tells the user
# what the program does. Modify the convert.py program (Section 2.2) to
# print out an introduction.
'''
A program to convert Celsius temps to Fahrenheit
    by: Susan Computewell
    Testing by freezing and boiling points
'''

def main():
    print("This program converts Celsius temperature to Fahrenheit.")

    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()
