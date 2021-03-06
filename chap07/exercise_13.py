# Me Computer, Mandalay.
# June 18, 2022
# exercise_13.py
# Day number calculation

from exercise_11 import isLeap
from exercise_12 import isValidDate

def dayNumber(month, day, year):
    dayNum = 31*(month-1) + day
    
    if month > 2:
        dayNum = dayNum - (4 * month + 23) // 10
        
    if isLeap(year):
        if month > 2:
            dayNum = dayNum + 1

    return dayNum

def main():
    print("Day number calculation\n")
    
    month, day, year = input("Enter date (mm/dd/yyyy): ").split("/")
    day, month, year = int(day), int(month), int(year)

    if isValidDate(month, day, year):
        print("The day number is", dayNumber(month, day, year))
    else:
        print("That's an invalid date!")

if __name__ == '__main__': main()