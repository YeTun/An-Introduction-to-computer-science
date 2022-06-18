# ME Computer, Mandalay.
# June 13, 2022
# exercise_4.py

#  4. Modify the convert.py program (Section 2.2) with a loop so that it executes 
#     5 times before quitting. EAch time through the loop, the program should get 
#     another temperature from the user and print a converted value.
#
# convert.py
#     A program to convert Celsius temps to Fahrenheit five times
# by: Susan Computewell

def main():
    
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))

        fahrenheit = 9/5 * celsius + 32
        
        # print("The temperature is", fahrenheit, "degrees Fahrenheit.")
        print(f"The temperature is {fahrenheit:0.2f} degrees Fahrenheit.")

main()