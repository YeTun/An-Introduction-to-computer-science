# Me Computer, Mandalay.
# June 18, 2022
# exercise_14.py

from graphics import *
import math

def main():
    # Open circle window
    win = GraphWin("Circle Intersection", 500, 500)
    win.setBackground("white")
    win.setCoords(-11, -11, 11, 11)
    center = Point(0, 0)

    # Take input graphically
    # Input radius of the circle
    r = Text(Point(center.getX(), center.getY() + 4), "Enter radius of the circle (0 - 5) & click anywhere:")
    r.draw(win)
    radiusDialog = Entry(Point(center.getX(), center.getY() + 3), 3)
    radiusDialog.draw(win)
    radiusDialog.setText("0.0")

    # wait for a click
    win.getMouse()
    radius = float(radiusDialog.getText())
    r.undraw()
    radiusDialog.undraw()

    # Input line y-intercept
    l = Text(Point(center.getX(), center.getY() - 4), "Enter y-intercept (-10 - 10) of line & click anywhere:")
    l.draw(win)
    lineDialog = Entry(Point(center.getX(), center.getY() - 5), 3)
    lineDialog.draw(win)
    lineDialog.setText("0.0")

    # wait for a click
    win.getMouse()
    yIntercept = float(lineDialog.getText())
    l.undraw()
    lineDialog.undraw()

    # Draw x and y axis
    xAxis = Line(Point(0, -10), Point(0, 10))
    xAxis.setArrow("both")
    xAxis.setWidth(3)
    xAxis.draw(win)
    yAxis = Line(Point(-10, 0), Point(10, 0))
    yAxis.setArrow("both")
    yAxis.setWidth(3)
    yAxis.draw(win)
    # Draw circle centered at (0,0)
    circle1 = Circle(center, radius)
    circle1.setOutline("blue")
    circle1.draw(win)
    # Draw horizontal line across the window with the given y-intercept
    horizontalLine = Line(Point(-10, yIntercept), Point(10, yIntercept))
    horizontalLine.setArrow("both")
    horizontalLine.setOutline("blue")
    horizontalLine.draw(win)
    # Draw two points of intersection in red
    if radius**2 - yIntercept**2 > 0:
        pt1X = math.sqrt(radius**2 - yIntercept**2)
        pt1 = Point(pt1X, yIntercept)
        pt1.setOutline("red")
        pt1.setFill("red")
        pt1.draw(win)

        pt2X = -1 * math.sqrt(radius**2 - yIntercept**2)
        pt2 = Point(pt2X, yIntercept)
        pt2.setOutline("red")
        pt2.setFill("red")
        pt2.draw(win)

        # Print out x values of the points of intersection
        Text(Point(pt1X, yIntercept - 1), round(pt1X, 2)).draw(win)
        Text(Point(pt2X, yIntercept - 1), round(pt2X, 2)).draw(win)
    else:
        Text(Point(5, 7), "No intersection.").draw(win)

    # End Program
    endText = Text(center, "Click again to quit.")
    endText.setSize(32)
    endText.setFill("green")
    endText.draw(win)
    win.getMouse()
    win.close()

main()

# from graphics import *
# import math as m

# def main():
#     #Create a square window and set coordinates -10,-10 to 10,10
#     win = GraphWin("Intersection of a line through a Circle", 500,500)
#     win.setCoords(-10, -10, 10, 10)

#     #Input: Radius of the circle and the y-intercept of the line
#     r = eval(input("What is the radius of the circle? "))
#     y = eval(input("Where does the line cross the y axis? "))

#     #Draw a circle centered at 0,0
#     c = Circle(Point(0,0), r)
#     c.draw(win)

#     #Draw a horizontal line across the window with teh given y-intercept
#     line = Line(Point(-10, y), Point(10, y))
#     line.draw(win)

#     if r < y:
#         print("The line does not intersect.")
#     else:
#         #Compute x
#         x = m.sqrt(r**2 - y**2)

#         #Print the two x values of intersection textually
#         print(-x, x)

#         #Print the two x values graphically
#         x1 = Text(Point(-x, y + 2),-x)
#         x2 = Text(Point(x, y + 2), x)
#         x1.draw(win)
#         x2.draw(win)

# main()
