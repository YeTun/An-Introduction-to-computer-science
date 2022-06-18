# ME Computer, Mandalay.
# June 13, 2022
# exercise_8.py
# Future value with multiple compounding periods

#  8. As an alternative to APR, the interest accrued on an account is often described 
#     in terms of a nominal rate and the number of compounding periods. For example, 
#     if the interest rate is 3% and the interest is compounded quarterly, the account 
#     actually earns .75% interest every 3 months.
#
#     Modify the futval.py program to use this method of entering the interest rate. 
#     The program should prompt the user for the yearly rate (rate) and the number of 
#     times that the interest is compounded each year (periods). To compute the value 
#     in ten years, the program will loop 10 * periods times and accrue rate/period 
#     interest on each iteration.

#     inputs: yearly rate
#             periods (number of times that the interest is compounded each year)
#             principal
#             fixed yearly investment
#             number of years
#     output: total accumulation

def main():
    print("This program calculates the future value of an investment.")
    
    principal = eval(input("Enter the initial principal: "))
    rate = eval(input("Enter the interest rate: "))
    periods = eval(input("Enter the number of compounding periods per year: "))
    years = eval(input("Enter the number of years: "))

    for i in range(years * periods):
        principal = principal * (1 + rate/periods)

    print("The amount in", years, "years is:", principal)

main()