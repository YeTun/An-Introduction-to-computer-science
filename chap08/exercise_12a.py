# Me Computer, Mandalay.
# June 19, 2020
# exercise_12.py

#This program accepts a sequence of average daily temps and computes
#the running total of cooling and heating degree days

from tkinter.filedialog import askopenfilename

def main():
    print("Program takes input of avg degrees on a given day in Farenheit.")
    print("If < 60, 60 - n = heating degrees. If > 80, n - 80 = cooling degrees.")
    print("Enter an average when prompted. To quit leave blank and hit <Enter>.")

    # open file
    infileName = askopenfilename()
    infile = open(infileName, "r")

    n = 0
    coolingN = 0 
    coolingTotal = 0
    heatingN = 0
    heatingTotal = 0

    for line in infile:
        dailyAvg = float(line)

        if dailyAvg < 60:
            heatingN += 1
            heatingTotal += 60 - dailyAvg
        elif dailyAvg > 80:
            coolingN += 1
            coolingTotal += dailyAvg - 80
        n += 1

    print(f"Out of {n} total days. {coolingN} days were cooling days for a total of {coolingTotal:0.2f} degrees.")
    print(f"{heatingN} days were heating days for a total of {heatingTotal:0.2f} degrees.")

main()
