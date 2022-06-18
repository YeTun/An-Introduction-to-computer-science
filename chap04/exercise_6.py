# Me Computer, Mandalay.
# June 15, 2022
# exercise_6.py
# A simple graphics program that modify the graphical future value

from graphics import *

def main():
    # Create a graphics window
    win = GraphWin("Investment Growth Chart", 400, 300)
    win.setBackground("gray")
    win.setCoords(-1.75, -200, 11.5, 10400)

    # Introduction
    intro = Text(Point(5, 9500), "Plots the growth of a 10-year investment.")
    intro.draw(win)

    # Get principal and interest rate
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))

    # Create labels on left edge
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5k').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)

    # Draw bar for initial principal
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw a bar for each subsequent year
    for year in range(1, 11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    # End Program
    intro.setText("Click again to quit.")
    intro.setFill("red")
    intro.setSize(18)
    win.getMouse()
    win.close()

main()
