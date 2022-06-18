# Me Computer, Mandalay.
# June 18, 2020
# exercise_9.py

def easterDate(year):
    if year < 1982 or year > 2048:
        return "Year entered is out of date range."
    else:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        if 22 + d + e <= 31:
            date = "Easter falls on March " + str((22 + d + e))
        else:
            date = "Easter falls on April " + str((22 + d + e - 31))
        return date

def main():
    y = int(input("Enter the year: "))
    print(easterDate(y))

main()

# def Easter(year):
#     if 1982 <= year <= 2018:
#         a = year % 19
#         b = year % 4
#         c = year % 7
#         d = (19 * a + 24) % 30
#         e = (2 * b + 4 * c + 6 * d + 5) % 7
#         if (d + e) > 9:
#             print("Easter falls on April {}.".format(d + e - 9))
#         else:
#             print("Easter falls on March {}.".format(22 + d + e))
#     else:
#         print("Year is out of range")


# def main():
#     #year = eval(input("Input a year: "))
#     year = 2018
#     Easter(year)
# main()
