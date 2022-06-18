# ME Computer, Mandalay.
# June 14, 2022
# exercise_2.py
# This program calculate the cost per square inch of a circular pizza

#  2. Write a program that calculates the cost per square inch of a circular pizze,
#     given its diameter and price. The formula for area is A = pir^2.

import math as m

def main():
    print("This program computes the cost per square inch of a pizza.")
    
    # inputs
    diameter = int(input("Enter the diameter of the pizza in inches: "))
    price = float(input("Enter the price of the pizza: "))

    # calculate
    area = m.pi * (diameter/2.0)**2
    cost = round(price/area, 2)

    # output
    print(f"The pizza's price is ${cost} cents per square inch.")

main()
