# Me Computer, Mandalay.
# June 16, 2022
# exercise_12b.py

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

# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future

def main():
    print("This program calculates the future value of an investment.")

    principal = float(input("Enter the initial principal: "))
    dollars = principal // 1
    cents = round((principal - dollars) * 100 , 2)
    apr = float(input("Enter the annualized interest rate: "))
    years = int(input("Enter the number of years invested: "))

    print("\nYear   Value  ")
    print("----------------")
    print("{0:^4} ${1:0.0f}.{2:0>2.0f}".format("0", dollars, cents))

    for i in range(1,years+1):
        principal = principal * (1 + apr)
        dollars = principal // 1
        cents = round((principal - dollars) * 100 , 2)
        print("{0:^4} ${1:0.0f}.{2:0>2.0f}".format(i, dollars, cents))

    print("\nThe value in 10 years is:", principal)

main()


# def main():
#     print("This program calculates the future value")
#     principal = float( input("Enter the initial principal: "))
#     apr = float( input("Enter the annual interest rate: "))
#     years = int(input("How many years in the future: "))

#     print("of a 10 year investment")
#     # Title of table
#     title = "Year   Value"
    
#     # outputs table title and table dashes
#     print("\n {}\n{}".format(title,"-"*14))
#     print("  {:>2.0f} {:10.2f}".format(0, principal)) # Outputs initial principal on table
    
#     # iterates through years
#     for i in range(1, years+1):
#          principal = float(principal * (1 + apr))
#          print("  {:>2.0f} {:10.2f}".format(i, principal))

# main()

# def main():
#     print("This program calculates the future value")
#     print("of a 10-year investment.")

#     principal = eval(input("Enter the initial principal: "))
#     apr = eval(input("Enter the annual interest rate: "))

#     print("{0:<9}{1:<7}").format("Year", "Value") #not right
    
#     for i in range(10):
#         principal = principal * (1 + apr)
#         print("{0:>6}{$1:>8.2f}".format(i, principal)) #not right

#     print("The value in 10 years is:", principal)

# main()