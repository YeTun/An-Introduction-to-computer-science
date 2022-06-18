# Me Computer, Mandalay.
# June 18, 2020
# exercise_13.py

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

def main():
    date = str(input("Enter date (formatted mm/dd/yyyy): "))
    first = date.find("/")
    second = date.find("/", first+1)
    month = int(date[:first])
    day = int(date[first+1:second])
    year = int(date[second+1:])
    thirty = [4, 6, 9, 11]
    thirtyOne = [1, 3, 5, 7, 8, 10, 12]
    
    if 1 <= month <= 12:
        if month in thirty:
            if 1 <= day <= 30:
                yearValid(year)
            else:
                print("Month {0}: days must fall between 1 and 30.".format(month))
        
        elif month in thirtyOne:
            if 1 <= day <= 31:
                yearValid(year)
            else:
                print("Month {0}: days must fall between 1 and 31.".format(month))
        elif month == 2:
            if leapYear(year) == True:
                if 1 <= day <= 29:
                    yearValid(year)
                else:
                    print("February is a leap year in {0}. Days must fall between 1 and 29.".format(year))
            else:
                if 1 <= day <= 28:
                    yearValid(year)
                else:
                    print("February days must fall between 1 and 28.".format(year))
    else:
        print("Month must be 1-12.")

main()
