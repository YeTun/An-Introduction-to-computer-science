# Me Computer, Mandalay.
# June 16, 2022
# exercise_1.py
# Convert day month and year numbers into two date formats
'''
1. As discussed in the chapter, string formatting could be used to simplify 
the dateconvert2.py program. Go back and redo this program making use of 
the string-formatting method.
'''
def main():
    # get the day month and year
    day, month, year = eval(input("Enter day, month, and year numbers: "))

    date1 = str(month) + "/" + str(day) + "/" + str(year)

    # Months
    months = ["January", "Febuarary", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"]

    monthStr = months[int(month)-1]
    date2 = monthStr + " " + str(day) + ", " + str(year)

    # Output result in month day, year format
    print(f"The converted date is {date1} or {date2}.")

    print("The date is {1:02}/{0:02}/{2} or".format(day, month, year),
           monthStr, "{0:02}, {2}.".format(day, month, year))
    
    print("The date is {1:02}/{0:02}/{2} or {3} {0:02}, {2}."
          .format(day, month, year, monthStr))

main()
