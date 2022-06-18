# ME Computer, Mandalay.
# June 13, 2022
# exercise_6.py
# Future value with number of years as an input.

#  6. Modify the futval.py program (Section 2.7) so that the number of yaers 
#     for the investment is also a user input. Make sure to change the final 
#     message to reflect the correct number of years.

def main():
    print("This program calculates the future value of an investment.")
    
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interest rate: "))
    years = eval(input("Enter the number of years: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The amount in", years, "years is:", principal)

main()
