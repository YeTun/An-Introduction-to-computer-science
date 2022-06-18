# Me Computer, Mandalay.
# June 18, 2022
# exercise_13.py

# accepts date
# verifies it
# calculates day number

def yearValid(year):
    if year > 0:
        return True
    else:
        return False

def leapYear(year):
    century = year // 100
    if year % 4 == 0:
        if century % 4 == 0:
            return True
        else:
            return False
    else:
        return False

def dateValid(month, day, year):
    thirty = [4, 6, 9, 11]
    thirtyOne = [1, 3, 5, 7, 8, 10, 12]    
    if 1 <= month <= 12:
        if month in thirty:
            if 1 <= day <= 30:
                return yearValid(year)
            else:
                return False
        
        elif month in thirtyOne:
            if 1 <= day <= 31:
                return yearValid(year)
            else:
                return False
        elif month == 2:
            if leapYear(year) == True:
                if 1 <= day <= 29:
                    return yearValid(year)
                else:
                    return False
            else:
                if 1 <= day <= 28:
                    return yearValid(year)
                else:
                    return False
    else:
        return False

def main():
    date = str(input("Enter date (formatted mm/dd/yyyy): "))

    first = date.find("/")
    second = date.find("/", first+1)
    m = int(date[:first])
    d = int(date[first+1:second])
    y = int(date[second+1:])

    if dateValid(m, d, y):
        daynum = 31*(m - 1) + d
        if m > 2:
            daynum - 4*m+23//10
        if leapYear(y):
            if m > 2:
                daynum += 1
        print(daynum)
    else:
        print("Not valid date.")

main()


# def leapYear(year):
#     if (year % 4) != 0:
#         return False
#     else:
#         if (year % 100) == 0:
#             if (year % 400) ==0:
#                 return True
#             else:
#                 return False
#         else:
#             return True

# def verDate(month, day, year):
#     if month > 12 or day > 31:
#         return False
#     else:
#         if day <= 28:
#             return True
#         elif month == 2 and day == 29:
#             if leapYear(year) == False:
#                 return False
#             else:
#                 return True
#         elif day == 31:
#             if month == 2 or 4 or 6 or 11:
#                 return False
#             else:
#                 return True
#         else:
#             return True

# def main():
#     dateStr = '05/25/1885'
#     dateStr = '12/31/2020'

#     monthStr, dayStr, yearStr = dateStr.split("/")
#     month = int(monthStr)
#     day = int(dayStr)
#     year = int(yearStr)

#     if verDate(month, day, year) == False:
#         print("This date is invalid.")
#     else:
#         dayNum = 31 * (month - 1) + day
#         if month == 2:
#             if leapYear(year) == True:
#                 dayNum = dayNum - (4 * (month) + 23)//10 + 1
#             else:
#                 dayNum = dayNum - (4 * (month) + 23)//10
#         else:
#             dayNum = 31 * (month - 1) + day
        
#         print("The numeric value of this date is {}.".format(dayNum))

# main()
