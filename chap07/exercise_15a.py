# Me Computer, Mandalay.
# June 18, 2022
# exercise_15.py

from graphics import *
import math

def main():
    # Open line window
    win = GraphWin("Line", 500, 500)
    win.setBackground("white")
    win.setCoords(-11, -11, 11, 11)
    center = Point(0, 0)

    # Draw x and y axis
    xAxis = Line(Point(0, -10), Point(0, 10))
    xAxis.setArrow("both")
    xAxis.setWidth(3)
    xAxis.draw(win)
    yAxis = Line(Point(-10, 0), Point(10, 0))
    yAxis.setArrow("both")
    yAxis.setWidth(3)
    yAxis.draw(win)

    # Draw x grid
    for i in range(-10, 10):
        xGrid = Line(Point(i, -10), Point(i, 10))
        xGrid.setFill(color_rgb(125, 140, 136))
        xGrid.draw(win)
    # Draw y grid
    for i in range(-10, 10):
        yGrid = Line(Point(-10, i), Point(10, i))
        yGrid.setFill(color_rgb(125, 140, 136))
        yGrid.draw(win)

    # Take input clicks
    l1 = Text(center, "Click anywhere in window.")
    l1.setFill(color_rgb(153, 92, 102))
    l1.setSize(32)
    l1.draw(win)
    pt1 = win.getMouse()
    l1.undraw()

    l2 = Text(pt1, "Click anywhere in window.")
    l2.setFill(color_rgb(153, 92, 102))
    l2.setSize(32)
    l2.draw(win)
    pt2 = win.getMouse()
    l2.undraw()

    # Draw midpoint and line through click points
    lineDraw = Line(pt1, pt2)
    midpt = Circle(lineDraw.getCenter(), .2)
    midpt.setFill("cyan")
    midpt.draw(win)
    lineDraw.draw(win)

    # calculate slope
    slopeX = pt2.getX() - pt1.getX()
    slopeY = pt2.getY() - pt1.getY()
    if slopeX != 0:
        slope = slopeY / slopeX
        # calculate length
        length = math.sqrt(slopeX**2 + slopeY**2)
        # print slope and length
        Text(Point(7, 10), "Slope is: " + str(round(slope, 2))).draw(win)
        Text(Point(7, 9), "Length is: " + str(round(length, 2))).draw(win)
    else:
        Text(Point(7, 10), "Slope is 0. Length is: " + str(round(slopeY))).draw(win)

    # End Program
    endText = Text(center, "Click again to quit.")
    endText.setSize(32)
    endText.setFill(color_rgb(237, 215, 19))
    endText.draw(win)
    win.getMouse()
    win.close()

main()


# import math as m
# from graphics import *

# def main():
#     win = GraphWin("Line Drawing Tool", 400, 400)
#     win.setCoords(-10, -10, 10, 10)
# #Prompt the User for 2 mouse clicks
#     message = Text(Point(-5, 8), "Click on 2 points to create a line")
#     message.draw(win)
# #Store coordinates in variables x1, x2 etc
#     point1 = win.getMouse()
#     point2 = win.getMouse()
#     x1 = point1.getX()
#     x2 = point2.getX()
#     y1 = point1.getY()
#     y2 = point2.getY()

# #Create a Line w/ midpoint "cyan"
#     line = Line(point1, point2)
#     line.draw(win)
#     mx, my = (x1+x2)/2, (y1+y2)/2
#     win.plot(mx, my, "cyan")

# #Calculate the length and slope of the Line
#     length = m.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#     if (x2 - x1) == 0:
#         message3 = Text(Point(-5,6), ("The slope of the line is vertical."))
#     else:
#         slope = (y2-y1)/(x2 -x1)
#         message3 = Text(Point(-5, 6), ("The slope of the line is: ", round(slope, 2)))
# #Print length and slope of line
#     message2 = Text(Point(-5, 7), ("The length of the line is: ", round(length, 2)))
#     message2.draw(win)
#     message3.draw(win)

# main()
