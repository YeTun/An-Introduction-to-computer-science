# Me Computer, Mandalay.
# June 19, 2022
# exercise_10.py
# This program computes the fuel efficiency of a multi-leg journey

from tkinter.filedialog import askopenfilename

def main():
    print("This program calcuates MPG for a trip using initial odometer reading")
    print("follow up odometer readings and gallons used for each leg.")

    # open file
    infileName = askopenfilename()
    infile = open(infileName, "r")

    # sentinel loop instead of for loop to get data
    initialMilage = infile.readline()
    mileage = [float(initialMilage)]
    gas = [0]
    line = infile.readline()
    while line != "":
        mileage.append(float(line.split(" ")[0]))
        gas.append(float(line.split(" ")[1]))
        line = infile.readline()

    # calculate and print MPG for each leg as well as total trip
    totalMileage = 0
    totalGas = 0
    i = 1
    while i < len(mileage):
        # calculate leg distance
        legMileage = mileage[i] - mileage[i-1]
        # add leg distance to total and gas used to total
        totalMileage += legMileage
        totalGas += gas[i]
        # calculate MPG for leg
        MPG = legMileage / gas[i]
        # print leg results
        print("Leg {0}  Miles driven: {1:0.2f}  Gallons of Gas: {2:0.2f}  MPG: {3:0.2f}".format(
            i, legMileage, gas[i], MPG))
        # increment i
        i += 1

    # print results for the entire trip
    MPG = totalMileage / totalGas
    print("Total legs driven: {0}  Miles driven: {1:0.2f}  Gallons of Gas: {2:0.2f}  MPG: {3:0.2f}".format(
        i-1, totalMileage, totalGas, MPG))

main()