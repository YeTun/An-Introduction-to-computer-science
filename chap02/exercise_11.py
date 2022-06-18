# ME Computer, Mandalay.
# June 13, 2022
# exercise_11.py

# 11. Write a program to perform a unit conversion of your own choosing. 
#     Make sure that the program prints an introduction that explains what it is.

'''
1 Gallon [Fluid, US] = 3.7854118 Liters, 1 Liter = 0.264172052
1 Gallon [Dry, US] = 4.4048838 Liters
1 Gallon [UK] = 4.54609 Liters
'''
def main():
    print("This program converts gallons to liters.")
    gallons = eval(input("How many gallons? "))
    
    liters = gallons * 3.7854118
    
    print("The fluid volume in liters is", liters, "liters.")
    
main()

# def main():

#     print("This program converts tablespoons to gram equivalent.")
#     tablespoons = float(input("Enter the number of tablespoons: "))

#     grams = 14.3 * tablespoons

#     print(tablespoons, " tablespoon(s) are equal to ", grams, " grams.", sep="")
#     input("[ Press the <Enter> key to quit. ]")

# main()