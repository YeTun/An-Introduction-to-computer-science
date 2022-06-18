# Me Computer, Mandalay.
# June 18, 2022
# exercise_12.py

def yearValid(year):
    if year > 0:
        print("Date is valid.")
    else:
        print("Year must be greater than 0.")

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
                yearValid(year)
                return True
            else:
                print("Invalid date")
                return False
        
        elif month in thirtyOne:
            if 1 <= day <= 31:
                yearValid(year)
                return True
            else:
                return False
        elif month == 2:
            if leapYear(year) == True:
                if 1 <= day <= 29:
                    yearValid(year)
                    return True
                else:
                    return False
            else:
                if 1 <= day <= 28:
                    yearValid(year)
                    return True
                else:
                    return False
    else:
        print("Invalid month")
        return False

def main():
    date = str(input("Enter date (formatted mm/dd/yyyy): "))

    first = date.find("/")
    second = date.find("/", first+1)
    month = int(date[:first])
    day = int(date[first+1:second])
    year = int(date[second+1:])
    
    print(dateValid(month, day, year))

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

# def main():
#     dateStr = '6/29/1100'
#     dateStr = '6/31/2020'

#     monthStr, dayStr, yearStr = dateStr.split("/")
#     month = int(monthStr)
#     day = int(dayStr)
#     year = int(yearStr)

#     if month > 12 or day > 31:
#         print("This date is invalid.")
#     else:
#         if day <= 28:
#             print("This date is valid.")
#         elif month == 2 and day == 29:
#             if leapYear(year) == False:
#                 print("This date is invalid.")
#             else:
#                 print("This date is valid.")
#         elif day == 31:
#             if month == 2 or 4 or 6 or 11:
#                 print("This date is invalid")
#             else:
#                 print("This date is valid")
#         else:
#             print("The date is valid.")
# main()
