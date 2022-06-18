# Me Computer, Mandalay.
# June 17, 2022
# exercise_5.py
# This program calculate the cost per square inch of a circular pizza

from math import pi

def pieArea(r):
    return round((pi * r**2), 2)        # returns area of pie in sqin

def sqinCost(price,r):
    return round(price/(pi * r**2), 2)  # returns  price per sqin

def main():
    print("This program calculates the cost per square inch of a circular pizza")
    print("from given price and diameter")
    price = float(input("How much is the pizza: "))
    diameter = float(input("What is the pizza diameter: "))

    radius = diameter/2

    print(f"The pizza's area is {pieArea(radius)} square inches")
    print(f"and the price is ${sqinCost(price, radius)} per square inch.")

main()

# import math as m

# def pizzArea(diameter):
#     area = m.pi * ((.5 * diameter) ** 2)
#     return area

# def pizzPrice(cost, area):
#     price_sqin = cost / area
#     return price_sqin

# def main():
#     price, d = eval(input("Please enter the cost of the Pizza, and how big it was: "))
    
#     A = pizzArea(d)
#     price_sqin = pizzPrice(price, A)
    
#     print("The pizza has an area of {0} square inches".format(round(A, 2)))
#     print("The price per square inch is about ${0}.".format(round(price_sqin, 2)))

# main()
