# Me Computer, Mandalay.
# June 17, 2022
# exercise_4.py
# Program to calculates the sum of natural numbers and sum of cubed natural numbers

def sumN(n):
    return sum(range(1, n+1))

def sumNCubes(n):
    return sum(i**3 for i in range(1, n+1))  # sum of cubed natural numbers

def main():
    print("This program calculates the sum of natural numbers and sum of cubed natural numbers")
    num = int(input("How many natural numbers to sum: "))
    
    sum = sumN(num)
    cube = sumNCubes(num)
    
    print(f"The sum of all natural numbers to {num} is {sum}.")
    print(f"The sum of all cubed natural numbers to {num} is {cube}.")

main()


# def sumN(n):
#     sum = 0
#     for num in range(n+1):
#         sum += num
#     return sum

# def sumNCubes(n):
#     cube = 0
#     for num in range(n+1):
#         cube += num ** 3
#     return cube

# def main():
#     n = eval(input("Enter a value: "))
    
#     sum = sumN(n)
#     cube = sumNCubes(n)
    
#     print(f"The sum of the first {n} natural numbers is {sum}.")
#     print(f"And the sum of the first {n} cubes is {cube}.")

# main()
