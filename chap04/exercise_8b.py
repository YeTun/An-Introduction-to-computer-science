# Me Computer, Mandalay.
# June 15, 2022
# exercise_8b.py
# This program allows the user to draw a line segment and then displays 
# some graphical information about the line Segment

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
    l1 = Text(center, "Click anywhere.")
    l1.setFill(color_rgb(153, 92, 102))
    l1.setSize(16)
    l1.draw(win)
    pt1 = win.getMouse()
    pt1.setFill("red")
    pt1.draw(win)

    pt2 = win.getMouse()
    pt2.setFill("red")
    pt2.draw(win)
    l1.undraw()

    # Draw midpoint and line through click points
    lineDraw = Line(pt1, pt2)
    midpt = Circle(lineDraw.getCenter(), .15)
    midpt.setFill("cyan")
    midpt.draw(win)
    lineDraw.draw(win)

    # calculate slope
    slopeX = pt2.getX() - pt1.getX()
    slopeY = pt2.getY() - pt1.getY()
    slope = slopeY / slopeX
    
    # calculate length
    length = math.sqrt(slopeX**2 + slopeY**2)
    
    # print slope and length
    Text(Point(8, 10), "Slope is: " + str(round(slope, 2))).draw(win)
    Text(Point(8, 9), "Length is: " + str(round(length, 2))).draw(win)

    # End Program
    endText = Text(center, "Click again to quit.")
    endText.setSize(18)
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
    
#     # Prompt the User for 2 mouse clicks
#     message = Text(Point(-5, 8), "Click on 2 points to create a line")
#     message.draw(win)
    
#     # Store coordinates in variables x1, x2 etc
#     point1 = win.getMouse()
#     point2 = win.getMouse()
#     x1 = point1.getX()
#     x2 = point2.getX()
#     y1 = point1.getY()
#     y2 = point2.getY()

#     #Create a Line w/ midpoint "cyan"
#     line = Line(point1, point2)
#     line.draw(win)
#     mx, my = (x1+x2)/2, (y1+y2)/2
#     win.plot(mx, my, "cyan")

#     #Calculate the length and slope of the Line
#     length = m.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#     slope = (y2-y1)/(x2 -x1)
    
#     #Print length and slope of line
#     message2 = Text(Point(-5, 7), ("The length of the line is: ", round(length, 2)))
#     message2.draw(win)
#     message3 = Text(Point(-5, 6), ("The slope of the line is: ", round(slope, 2)))
#     message3.draw(win)
        
#     # Wait for another click to exit
#     message = Text(Point(5, 9),"Click anywhere to close")
#     message.draw(win)
#     win.getMouse()
#     win.close()

# main()

# # import libraries
# from graphics import *
# from math import sqrt

# def main():
#     win = GraphWin("Line Segment Information", 400, 400)
#     for i in range(1):
#         p1 = win.getMouse()
#         p2 = win.getMouse()

#     # variables needed
#     dx = p2.getX()-p1.getX()
#     dy = p2.getY()-p1.getY()
#     m = dy/dx
#     midX = (p1.getX()+p2.getX())/2
#     midY = (p1.getY()+p2.getY())/2
#     lineLength = sqrt((dx**2)+(dy**2))
#     #lines and shapes
#     line = Line(Point(p1.getX(),p1.getY()), Point(p2.getX(),p2.getY()))
#     line.setFill("black")
#     line.draw(win)
#     midPoint=Circle(Point(midX,midY),2)
#     midPoint.setFill("cyan")
#     midPoint.setOutline("cyan")
#     midPoint.draw(win)
#     #textual information
#     Text(Point(200,50),f"Slope of the line is {m}").draw(win)
#     Text(Point(200,100),f"The length of the line is {lineLength}").draw(win)

#     #quiting prompt
#     quit = Text(Point(200,10),"Click again to quit")
#     quit.setStyle("bold")
#     quit.draw(win)
#     win.getMouse()
#     win.close()
# main()
