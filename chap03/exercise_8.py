# ME Computer, Mandalay.
# June 14, 2022
# exercise_8.py
# This program figures out the date of easter

#  8. The Gregorian epact is the number of days between Janaury 1st and the previous 
#     new moon. This value is used to figure out the date of Easter. It is calculated 
#     by these formulas (using int arithmetic):
#       C = year//100
#       epact = (8 + (C//4) - C + ((8C + 13)//25) + 11(year%19))%30

def main():
    print("This program calculates the Gregorian epact value of year.")
    year = int(input("Enter 4 digit year (e.g. 2022): "))
    
    c = year // 100
    epact = (8+(c//4) - c + ((8*c + 13)//25) + 11 * (year % 19)) % 30
    
    print("The epact value is", epact, "days.")

main()
