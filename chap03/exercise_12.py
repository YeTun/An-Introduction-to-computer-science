# ME Computer, Mandalay.
# June 14, 2022
# exercise_12.py
# This program find the sum of the cubes of natural numbers

# 12. Write a program to find the sum of the cubes of the first n natural numbers 
#     where the value of n is provided by the user.

def main():
    print("This program finds the sum of the cubes of the first n natural numbers.")
    n = int(input("Please enter a value for n: "))
    
    sum = 0
    for i in range(1,n+1):
        sum = sum + i**3
    
    print("The sum of cubes of 1 through through", n, "is:", sum)

main()