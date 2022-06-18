# Me Computer, Mandalay.
# June 16, 2022
# exercise_12.py

# 12. Write an improved version of the futval.py program from Chapter 2.
#     Your program will prompt the user for the amoutn of the investment,
#     the annualized interest rate, and the number of years of the investment. 
#     The program will then output a nicely formatted table that tracks the value 
#     of the investment year by year. Your output might look something like this:
#
#     Year     Value
#     ----------------
#       0     $2000.00
#       1     $2200.00
#       2     $2420.00
#       3     $2662.00
#       4     $2928.20
#       5     $3221.02
#       6     $3542.12
#       7     $3897.43

def main():
    print("This program calculates the future value of an investment.")
    print()
    
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))
    years = int(input("Enter the number of years: "))

    print("Year   Value")
    print("--------------")
    for i in range(years+1):
        print("{0:3}   ${1:7.2f}".format(i, principal))
        principal = principal * (1 + apr)

main()
