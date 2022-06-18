# Me Computer, Mandalay.
# June 19, 2020
# exercise_3.py
# While loop to determine rule of 72

def main():
    principal = eval(input("What is the initial principal? "))
    apr = eval(input("Enter the annualized interest rate [ie 15% -> (0.15)]: "))

    p = principal
    interest = 0
    years = 0
    
    while principal > .5 * p:
        years += 1
        interest = p * apr
        p = p + interest

    print(round(p, 2))
    print(f"It takes {years} years to double.")

main()
