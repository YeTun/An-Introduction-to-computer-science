# Me Computer, Mandalay.
# June 19, 2022
# exercise_3.py
#    Years for investment to double (rule of 72)

def main():
    print("Number of years for an investment to double.\n")

    apr = float(input("What is the annual interest rate? "))
    principal = 1
    years = 0
    while principal < 2:
        principal = principal*(1+apr)
        years = years + 1

    print("Years to double:", years)

if __name__ == '__main__': main()