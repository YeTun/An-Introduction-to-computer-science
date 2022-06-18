# Me Computer, Mandalay.
# June 18, 2020
# exercise_11.py
#if year is divisible by 4, it's a leap years
#unless it's a century year not divisible by 400
#leap year yes or no

def main():
    year = int(input("Enter a year: "))
    century = year // 100

    if year % 4 == 0:
        if century % 4 == 0:
            print("{0} is a leap year.".format(year))
        else:
            print("{0} is not a leap year.".format(year))
    else:
        print("{0} is not a leap year.".format(year))

main()


# def leapYear(year):
#     if (year %4) != 0:
#         print("{} is not a leap year.".format(year))
#     else:
#         if (year % 100) == 0:
#             if (year % 400) ==0:
#                 print("{} is a leap year.".format(year))
#             else:
#                 print("{} is not a leap year.".format(year))
#         else:
#             print("{} is a leap year.".format(year))


# def main():
#     year = 1900
#     leapYear(year)
# main()
