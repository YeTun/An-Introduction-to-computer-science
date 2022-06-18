# ME Computer, Mandalay.
# June 13, 2022
# exercise_2.py

#  2. On many systems with Python, it is posible to run a program by simply
#     clicking (or double-clicking) on the icon of the program file. If you are 
#     able to run the convert.py program this way, you may discover another
#     usability issue. The program starts running in a new window, but as soon as 
#     the program is finished, the window disappears so that you cannot read the results. 
#     Add an input statement at the end of the program so that it pauses to give the user 
#     a chance to read the results. Something like this should work:
#
#       input("Press the <Enter> key to quit.")
#
# convert.py
#     A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    print("This program converts Celsius temperature to Fahrenheit.")    
    celsius = eval(input("What is the Celsius temperature? "))
    
    fahrenheit = 9/5 * celsius + 32
    
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")    
    input("Press the <Enter> key to quit.")
    
main()