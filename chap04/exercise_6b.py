# Me Computer, Mandalay.
# June 15, 2022
# exercise_6b.py
# A simple graphics program that modify the graphical future value

from graphics import *

def main():
    # Create a graphics window
    win = GraphWin("Investment Growth Chart", 600, 600)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)
    center = Point(5, 5000)
    centerX = 5
    centerY = 5000

    # Introduction
    intro = Text(center, "This program plots the growth of a 10-year investment.")
    intro.draw(win)

    # Get principal and interest rate
    p = Text(Point(centerX, centerY + 3000), "Enter beginning principal & click anywhere:")
    p.draw(win)
    enterPrincipal = Entry(Point(centerX, centerY + 2500), 7)
    enterPrincipal.setText("2750")
    enterPrincipal.draw(win)

    # wait for a click
    win.getMouse()
    principal = float(enterPrincipal.getText())

    # get interest rate
    a = Text(Point(centerX, centerY - 3000), "Enter APR & click anywhere:")
    a.draw(win)
    enterAPR = Entry(Point(centerX, centerY - 2500), 5)
    enterAPR.setText("0.01")
    enterAPR.draw(win)

    # wait for a click
    win.getMouse()
    apr = float(enterAPR.getText())
    p.undraw()
    enterPrincipal.undraw()
    a.undraw()
    enterAPR.undraw()

    # Create labels on left edge
    intro.undraw()
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
        Text(Point(year + 0.5, principal + 100), round(principal, 2)).draw(win)

    # End Program
    endText = Text(center, "Click again to quit.")
    endText.draw(win)
    win.getMouse()
    win.close()

main()
