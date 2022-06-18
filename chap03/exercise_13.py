# ME Computer, Mandalay.
# June 14, 2022
# exercise_13.py
# This program sums a defined quantity of numbers entered by the user

# 13. Write a program to sum a series of numbers entered by the user. The program should 
#     first prompt the user for how many numbers are to be summed. The program should then 
#     prompt the user for each of the numbers in turn and print out a total sum after all 
#     the numbers have been entered. Hint: Use an input statement in the body of the loop.

def main():
    print("This program allows you to total up some numbers.")

    n = int(input("How many numbers do you have? "))

    total = 0
    for i in range(n):
        num = eval(input("Enter a number: "))
        total = total + num

    print("The sum of the numbers is:", total)

main()