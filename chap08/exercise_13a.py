# Me Computer, Mandalay.
# June 19, 2020
# exercise_13.py
# This program with graphically plot a regression line

from graphics import *

def main():
    # open grapics window
    win = GraphWin("Regression Line", 600, 600)
    win.setCoords(-10, -10, 10, 10)
    win.setBackground(color_rgb(36, 66, 97))
    # draw standard axis
    yAxis = Line(Point(0, 10), Point(0, -10))
    yAxis.draw(win)
    xAxis = Line(Point(10, 0), Point(-10, 0))
    xAxis.draw(win)

    # draw done button
    button = Rectangle(Point(-9.5, -9.5), Point(-7.5, -8.5))
    button.setOutline(color_rgb(47, 177, 186))
    button.setFill(color_rgb(227, 229, 209))
    button.draw(win)
    buttonText = Text(button.getCenter(), "Done")
    buttonText.setTextColor(color_rgb(47, 177, 186))
    buttonText.draw(win)

    # get clicks
    n = 0
    x = 0
    y = 0
    xSquared = 0
    xy = 0
    dataPoint = win.getMouse()

    while not (-9.5 < dataPoint.getX() and dataPoint.getX() < -7.5) \
    or not (-9.5 < dataPoint.getY() and dataPoint.getY() < -8.5):
        # draw point
        newPoint = Circle(dataPoint, .1)
        newPoint.setFill(color_rgb(223, 120, 53))
        newPoint.draw(win)
        # number
        n += 1
        # sum x
        x += dataPoint.getX()
        # sum y
        y += dataPoint.getY()
        # sum x**2
        xSquared += x**2
        # sum xy
        xy += x * y
        print(n)
        print(x)
        print(y)
        print(xSquared)
        print(xy)

        # next click
        dataPoint = win.getMouse()

    # calculate y x at left and right edges of window
    m = ((xy) - (n * (x / n) * (y / n))) / (xSquared - n * (x / n)**2)
    yLeft = (y / n) + m * (-10 - (x / n))
    yRight = (y / n) + m * (10 - (x / n))
    # draw line
    regressionLine = Line(Point(-10, yLeft), Point(10, yRight))
    regressionLine.setOutline(color_rgb(180, 211, 191))
    regressionLine.setWidth(2)
    regressionLine.draw(win)
    # wait for click to quit
    buttonText.setText("Quit")
    end = win.getMouse()

main()
