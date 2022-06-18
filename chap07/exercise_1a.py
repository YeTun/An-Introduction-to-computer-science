# Me Computer, Mandalay.
# June 18, 2020
# exercise_1.py
# This program calculate the hourly rate and number of hours worked per week

# defining salary functions
def overtimePay(hours, hourlyRate):
    pay = (hours-40) * (hourlyRate * 1.5) + 40 * hourlyRate
    print(f"The total wages are {pay} dollars")

def regPay(hours, hourlyRate):
    pay = hours * hourlyRate
    print(f"The total wages are {pay} dollars")

# defining main function
def main():
    print("This program gives wages earned in a week period.")
    rate = float(input("What is the hourly rate? "))
    numberHours = float(input("How many hours were worked? "))

    # determines if overtime pay is included
    if numberHours > 40:
        overtimePay(numberHours, rate)
    elif numberHours <= 40:
        regPay(numberHours, rate)
    else:
        print("Something went wrong")

if __name__ == '__main__': main()


# def main():
#     # summary of program
#     print("This program calculates weekly wages based on 40 hr work week plus",
#             "1.5x for time in excess of 40 hours.")
#     # input number of hours worked
#     hrs = float(input("Enter the number of hours worked: "))
#     # input hourly rate
#     rate = float(input("Enter the hourly salary rate: "))

#     # calculate total wages for the week
#     if hrs <= 40:
#         wages = hrs * rate
#     else:
#         wages = 40 * rate + (hrs - 40) * rate * 1.5
#     # print result
#     print("The total wages due are ${0:0.02f}".format(wages))

# main()

# c07ex1.py
#    overtime pay

# def main():
#     print("Weekly pay calculator \n")
#     hours = float(input("Enter hours worked: "))
#     wage = float(input("hourly wage: "))
    
#     if hours <= 40:
#         pay = hours * wage
#     else:
#         pay = 40 * wage + (hours-40) * 1.5 * wage

#     print("Your week's pay is ${0:0.2f}.".format(pay))

# if __name__ == '__main__':
#     main()

