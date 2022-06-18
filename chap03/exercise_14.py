# ME Computer, Mandalay.
# June 14, 2022
# exercise_14.py
# Average of numbers entered by the user.

# 14. Write a program that finds the average of a series of numbers entered by the user. 
#     As in the previous problem, the program will first ask the user how many numbers there 
#     are. Note: The average should always be a float, even if the user inputs are all ints.

def main():
    print("Program to calculate average")
    n = int(input("How many numbers do you have? "))
    
    total = 0
    for i in range(n):
        num = float(input("Enter a number: "))
        total = total + num

    print("The average of the numbers is:", total/n)

main()