# ME Computer, Mandalay.
# June 14, 2022
# exercise_11.py
# This program finds the sum of first n natural numbers

# 11. Write a program to find the first n natural numbers, where the 
#     value of n is provided by the user.

#    

def main():
    print("This program finds the sum of the first n natural numbers.")
    print()

    n = int(input("Please enter a value for n: "))
    sum = 0
    for i in range(1,n+1):
        sum = sum + i

    print()
    print("The sum from 1 to", n, "is:", sum)

main()