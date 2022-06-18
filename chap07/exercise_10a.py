# Me Computer, Mandalay.
# June 18, 2020
# exercise_10.py
# 1954, 1981, 2049, 2076 one week too late

def easterDate(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7

    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        if 22 + d + e - 7 <= 31:
            date = "Easter falls on March " + str((22 + d + e - 7))
        else:
            date = "Easter falls on April " + str((22 + d + e - 31 - 7))
        return date
    else:
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
#     if 1900 <= year <= 2099:
#         a = year % 19
#         b = year % 4
#         c = year % 7
#         d = (19 * a + 24) % 30
#         e = (2 * b + 4 * c + 6 * d + 5) % 7
#         if (d + e) > 9:
#             if year == 1954 or 1981 or 2049 or 2076:
#                 d = d - 7
#                 print("Easter falls on April {}.".format(d + e - 9))
#             else:
#                 print("Easter falls on April {}.".format(d + e - 9))
#         else:
#             if year == 1954 or 1981 or 2049 or 2076:
#                 d = d - 7
#                 print("Easter falls on March {}.".format(22 + d + e))
#             else:
#                 print("Easter falls on March {}.".format(22 + d + e))
#     else:
#         print("Year is out of range")


# def main():
#     #year = eval(input("Input a year: "))
#     year = 2049
#     Easter(year)
# main()

