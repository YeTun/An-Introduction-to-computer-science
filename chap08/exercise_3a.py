# Me Computer, Mandalay.
# June 19, 2022
# exercise_3.py
# While loop to determine rule of 72

def main():
    interest = float(input("Enter an interest rate [ie 2.5% -> (0.025)]: "))
    
    principal = 1000
    futureVal = 0
    years = 0
    while futureVal <= 2*principal:
        years += 1
        if years == 1:
            futureVal = principal * (1+interest)
        else:
            futureVal = futureVal * (1+interest)
        print(f"After year {years} the value is: ${futureVal:0.2f}")

main()
