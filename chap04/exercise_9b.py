# Me Computer, Mandalay.
# June 15, 2022
# exercise_9b.py
# This program displays information about a rectangle drawn by the user.

from graphics import *
import math

def main():
    # Draw window
    win = GraphWin("Line", 400, 400)
    win.setBackground("white")
    win.setCoords(-11, -11, 11, 11)

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

    # Prompt with directions
    intro = Text(Point(0, 10),
        "Draw a rectangle based on 2 clicks. Click to continue...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(13)
    intro.draw(win)
    win.getMouse()
    intro.undraw()
    intro = Text(Point(-4, 10), "Click first corner of rectangle")
    intro.setFill(color_rgb(0, 0, 255))
    intro.setSize(12)
    intro.draw(win)

    # Get top left corner
    top = win.getMouse()
    top.setFill("red")
    top.draw(win)

    # Get bottom right corner
    intro.setText("Click opposite corner of rectangle")
    bottom = win.getMouse()
    bottom.setFill("red")
    bottom.draw(win)
    intro.undraw()
    
    # Draw rectangle
    rect = Rectangle(top, bottom)
    rect.setOutline(color_rgb(153, 92, 102))
    rect.setWidth(3)
    rect.draw(win)

    # Calculate length
    xRect = abs(top.getX() - bottom.getX())
    # Calculate width
    yRect = abs(top.getY() - bottom.getY())
    # perimeter = 2(length + width)
    perimeter = str(round(2 * (xRect + yRect), 2))
    # area = length * width
    area = str(round(xRect * yRect, 2))

    # Print perimeter
    perimeterWin = Text(Point(-3, 10), 
        "The rectangle perimeter is:" + perimeter)
    perimeterWin.setFill(color_rgb(153, 92, 102))
    perimeterWin.setSize(13)
    perimeterWin.draw(win)
    # Print area
    areaWin = Text(Point(-4, 8), 
        "The rectangle area is:" + area)
    areaWin.setFill(color_rgb(153, 92, 102))
    areaWin.setSize(13)
    areaWin.draw(win)

    # End Program
    endText = Text(Point(0, 0), "Click again to quit.")
    endText.setSize(14)
    endText.setFill(color_rgb(255, 0, 0))
    endText.draw(win)
    win.getMouse()
    win.close()

main()


# from graphics import *

# def main():
#     win = GraphWin("Rectangle Information", 400, 400)
    
#     p1 = win.getMouse()
#     p2 = win.getMouse()

#     # rectangle shape
#     rect = Rectangle(Point(p1.getX(), p1.getY()), Point(p2.getX(), p2.getY())).draw(win)
    
#     # variables needed
#     rectLen = p2.getY() - p1.getY()
#     rectWidth = p2.getX() - p1.getX()
#     area = rectWidth*rectLen
#     perimeter = (rectLen*2) + (rectWidth*2)
   
#     # textual information
#     Text(Point(200,50), f"Area of the Rectangle is {area}").draw(win)
#     Text(Point(200,100),f"Perimeter of the Rectangle is {perimeter}").draw(win)

#     #quiting prompt
#     quit = Text(Point(200, 10),"Click again to quit")
#     quit.setStyle("bold")
#     quit.draw(win)
#     win.getMouse()
#     win.close()

# main()


# def main():
#     win = GraphWin("Line Drawing Tool", 400, 400)
#     win.setCoords(-10, -10, 10, 10)
# #Prompt the User for 2 mouse clicks
#     message = Text(Point(-5, 8), "Click on 2 points to create a Rectangle")
#     message.draw(win)

# #Store coordinates in variables x1, x2 etc
#     point1 = win.getMouse()
#     point2 = win.getMouse()
#     x1 = point1.getX()
#     x2 = point2.getX()
#     y1 = point1.getY()
#     y2 = point2.getY()
# #Calculate Perimeter and Area
#     area = (x2 - x1)*(y2 - y1)
#     perimeter = 2 * ((x2-x1)+(y2-y1))
# #Draw Rectangle
#     r = Rectangle(point1, point2)
#     r.draw(win)
# #Print the Perimeter and area of the rectangle
#     message2 = Text(Point(-5, 7), ("The area of the rectangle is", round(area, 2)))
#     message2.draw(win)
#     message3 = Text(Point(-5, 6), ("The perimeter of the rectangle is", round(perimeter, 2)))
#     message3.draw(win)

# main()

