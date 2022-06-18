# ME Computer, Mandalay.
# June 14, 2022
# exercise_5.py
# This program calculates the cost of shipping bags of coffee

#  5. The Konidtorei coffee shop sells coffee at $10.50 a pound plus the cost of shipping. 
#     Each order ships for $.086 per pound + $1.50 fixed cost for overhead. Write a program 
#     that calculates the cost of an order.

def main():
    print("This program calculates the cost of an order.")
    pounds = float(input("Enter the number of pounds of coffee ordered: "))
    
    coffeeCost = pounds * 10.50    
    shippingCost = 0.86 * pounds + 1.50
    
    print()
    print("Cost of coffee:", coffeeCost)
    print("Shipping:      ", shippingCost)
    print("Total due:     ", coffeeCost + shippingCost)

main()
