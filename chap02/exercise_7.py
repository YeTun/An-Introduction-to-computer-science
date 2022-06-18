# ME Computer, Mandalay.
# June 13, 2022
# exercise_7.py

'''
7. Suppose you have an investment plan where you invest a certain fixed 
   amount every year. Modify futeval.py to compute the total accumulation 
   of your investment. The inputs to the program will be the amount to invest
   each year, the interest rate, and the number of years for the investment.

     inputs: principle
             APR
             fixed yearly investment
             number of years
     output: total accumulation

     start with principal
     for a given number of years, add fixed yearly investment to principal
     to the resulting sum, calculate APR and add this to the sum
     repeat for specified # of years
     then

 futval.py
    A program to compute the future value of an investment
    with number of years determined by the user
'''

def main():
    print("This program calculates the future value of a yearly investment")
    
    payment = eval(input("Enter amount to invest each year: "))
    apr = eval(input("Enter the annualized interest rate: "))
    years = eval(input("Enter the number of years: "))

    principal = 0.0
    for i in range(years):
        principal = (principal + payment) * (1 + apr)

    print("The amount in", years, "years is:", principal)

main()
