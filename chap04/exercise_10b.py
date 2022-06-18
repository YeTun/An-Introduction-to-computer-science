# Me Computer, Mandalay.
# June 15, 2022
# exercise_10b.py
# This program displays information about a rectangle drawn by the user.

from graphics import *
import math

def main():
    # Draw window
    win = GraphWin("Triangle", 800, 800)
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
    intro = Text(Point(-2.5, 8.5), "This draws a triangle based on 3 clicks. Click to continue...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)
    win.getMouse()
    intro.undraw()
    intro = Text(Point(-6.5, 8.5), "Click first corner of the triangle...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)

    # Get first corner
    a = win.getMouse()
    intro.undraw()

    # Get second corner
    intro = Text(Point(-6.5, 8.5), "Click second corner of the triangle...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)
    b = win.getMouse()
    intro.undraw()

    # Get third corner
    intro = Text(Point(-6.5, 8.5), "Click final corner of the triangle...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)
    c = win.getMouse()
    intro.undraw()

    # Draw rectangle
    tri = Polygon(a, b, c)
    tri.setOutline(color_rgb(153, 92, 102))
    tri.setWidth(3)
    tri.draw(win)

    # Calculate lengths
    ab = math.sqrt( (b.getX() - a.getX()) ** 2 + (b.getY()- a.getY()) ** 2)
    bc = math.sqrt( (c.getX() - b.getX()) ** 2 + (c.getY() - b.getY()) ** 2)
    ca = math.sqrt( (a.getX() - c.getX()) ** 2 + (a.getY() - c.getY()) ** 2)
    # Calculate s
    s = (ab + bc + ca) / 2
    # perimeter = 2(length + width)
    perimeter = str(round(ab + bc + ca, 2))
    # area = length * width
    area = str(round(math.sqrt(s * (s - ab) * (s - bc) * (s - ca)), 2))

    # Print perimeter
    perimeterWin = Text(Point(-6.5, 8.5), "The triangle perimeter is:" + perimeter)
    perimeterWin.setFill(color_rgb(153, 92, 102))
    perimeterWin.setSize(15)
    perimeterWin.draw(win)
    # Print area
    areaWin = Text(Point(-6.5, 7.5), "The triangle area is:" + area)
    areaWin.setFill(color_rgb(153, 92, 102))
    areaWin.setSize(15)
    areaWin.draw(win)

    # End Program
    endText = Text(Point(-4.5, 0.5), "Click again to quit.")
    endText.setSize(32)
    endText.setFill(color_rgb(237, 215, 19))
    endText.draw(win)
    win.getMouse()
    win.close()

main()


# from graphics import *
# from math import sqrt

# def main():
#     win = GraphWin("Triangle Information", 400, 400)

#     p1 = win.getMouse()
#     p2 = win.getMouse()
#     p3 = win.getMouse()

#     # components needed
#     aX = p1.getX()-p2.getX()
#     aY = p1.getY()-p2.getY()
#     bX = p2.getX()-p3.getX()
#     bY = p2.getY()-p3.getY()
#     cX = p3.getX()-p1.getX()
#     cY = p3.getY()-p1.getY()
#     a = sqrt((aX**2)+(aY**2))
#     b = sqrt((bX**2)+(bY**2))
#     c = sqrt((cX**2)+(cY**2))
#     s = ((a + b + c)/2)
   
#     # Calculating area
#     area = sqrt(s*(s-a)*(s-b)*(s-c))
    
#     # triangle shape
#     triangle = Polygon(Point(p1.getX(),p1.getY()), Point(p2.getX(),p2.getY()), Point(p3.getX(),p3.getY())).draw(win)

#     # textual information
#     Text(Point(200,50),f"Area of the Triangle is {area}").draw(win)

#     #quiting prompt
#     quit = Text(Point(200,10),"Click again to quit")
#     quit.setStyle("bold")
#     quit.draw(win)
#     win.getMouse()
#     win.close()

# main()

# from graphics import *
# import math as m

# def main():
#     win = GraphWin("Line Drawing Tool", 400, 400)
#     win.setCoords(-10, -10, 10, 10)
# #Prompt the User for 3 mouse clicks
#     message = Text(Point(-5, 8), "Click on 3 points to create a Triangle")
#     message.draw(win)

# #Store coordinates in variables x1, x2 etc
#     point1 = win.getMouse()
#     point2 = win.getMouse()
#     point3 = win.getMouse()
#     x1 = point1.getX()
#     x2 = point2.getX()
#     y1 = point1.getY()
#     y2 = point2.getY()
#     x3 = point3.getX()
#     y3 = point3.getY()
# #Calculate Perimeter
#     a = m.sqrt((x2-x1)**2 + (y2-y1)**2)
#     b = m.sqrt((x3-x1)**2 + (y3-y1)**2)
#     c = m.sqrt((x3-x2)**2 + (y3-y2)**2)
#     perimeter = a + b + c
# #Calculate Area
#     s = perimeter/2
#     area = m.sqrt(s*(s-a)*(s-b)*(s-c))

# #Draw Rectangle
#     line1 = Line(point1, point2)
#     line1.draw(win)
#     line2 = Line(point2, point3)
#     line2.draw(win)
#     line3 = Line(point3, point1)
#     line3.draw(win)
# #Print the Perimeter and area of the rectangle
#     message2 = Text(Point(-5, 7), ("The area of the triangle is", round(area, 2)))
#     message2.draw(win)
#     message3 = Text(Point(-5, 6), ("The perimeter of the triangle is", round(perimeter, 2)))
#     message3.draw(win)

#     message.setText("click anywhere to quit.")
#     win.getMouse()
#     win.close()

# main()
