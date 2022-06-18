# Me Computer, Mandalay.
# June 15, 2022
# exercise_11b.py

# 11. Five-click House.
#     You are to write a program that allows the user to draw a simple house using five mouse clicks. The fisrt two clicks will be the opposite
#     corners of the rectangular frame of the house. The third click will indicate the center of the otp ege of a rectangular door. The door should
#     have a total width that is 1/5 the wdith of the house frame. The sides of the door should have extend from the corners of the top down to the
#     bottom of the frame. The fourth click will indicate the center of a square window. The window is half as wide as the door. The last click will
#     indicate the peak of the roof. The edges of the roof will extend from the point at the peak to the corners of the top edge of the house frame.

from graphics import *
import math

def main():
    # Draw window
    win = GraphWin("5 Click House", 400, 300)
    win.setBackground("white")
    win.setCoords(-11, -11, 11, 11)

    # Prompt with directions
    intro = Text(Point(-0, 10), "Draws a house based on 5 clicks. Click to continue...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(13)
    intro.draw(win)
    win.getMouse()
    intro.undraw()
    intro = Text(Point(0, 10), "The first 2 clicks are opposite corners of a rectangular frame")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(13)
    intro.draw(win)
    intro.undraw()
    intro = Text(Point(-6.5, 8.5), "Click bottom left corner of rectangle...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(13)
    intro.draw(win)

    # Get bottom left corner of frame
    one = win.getMouse()
    intro.undraw()

    # Get top right corner
    intro = Text(Point(-6.5, 8.5), "Click top right corner of rectangle...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)
    two = win.getMouse()
    intro.undraw()
    # Draw rectangle
    frame = Rectangle(one, two)
    frame.setOutline(color_rgb(153, 92, 102))
    frame.setWidth(3)
    frame.draw(win)

    # Get top center of door - 1/5 width of house frame
    intro = Text(Point(-6.5, 8.5), "Click top center of the doorway...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)
    three = win.getMouse()
    intro.undraw()
    # Calculate frame width
    doorWidth = abs( one.getX() - two.getX() ) / 5
    # Draw door
    door = Rectangle(Point(three.getX() + doorWidth / 2, three.getY()),
           Point(three.getX() - doorWidth / 2, one.getY()))
    door.setOutline(color_rgb(153, 92, 102))
    door.setWidth(3)
    door.draw(win)

    # Get center of window, 1/2 width of door
    intro = Text(Point(-6.5, 8.5), "Click center of the window...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)
    four = win.getMouse()
    intro.undraw()
    # Calculate frame width
    windowWidth = doorWidth / 2
    # Draw window
    window = Rectangle(Point(four.getX()- windowWidth/2, four.getY() - windowWidth/2),
             Point(four.getX()+ windowWidth/2, four.getY() + windowWidth/2))
    window.setOutline(color_rgb(153, 92, 102))
    window.setWidth(3)
    window.draw(win)

    # Get tip of roof
    intro = Text(Point(-6.5, 8.5), "Click tip of the triangular roof...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)
    five = win.getMouse()
    intro.undraw()
    # Draw roof
    roof = Polygon(two, five, Point(one.getX(), two.getY()))    
    roof.setOutline(color_rgb(153, 92, 102))
    roof.setWidth(3)
    roof.draw(win)

    # End Program
    endText = Text(Point(0, -10), "Click again to quit.")
    endText.setSize(16)
    endText.setFill(color_rgb(237, 215, 19))
    endText.draw(win)
    win.getMouse()
    win.close()

main()


# # import libraries
# from graphics import *

# def main():
#     win = GraphWin("Welcome Home", 400, 400)
#     win.setCoords(-10, -10, 10, 10)

#     #2 clicks for the frame of the house
#     message = Text(Point(0, 8), "Click on 2 diagonal points to create the rectangular frame of your house.")
#     message.draw(win)
#     point1 = win.getMouse()
#     point2 = win.getMouse()
#     x1 = point1.getX()
#     y1 = point1.getY()
#     x2 = point2.getX()
#     y2 = point2.getY()
#     r = Rectangle(point1, point2)
#     r.draw(win)
#     message.undraw()

#     #The third click will show the center of the top of the door
#     message = Text(Point(0, y1-1), "Excellent! Click the top of the door frame.")
#     message.draw(win)
#     point3 = win.getMouse()
#     x3 = point3.getX()
#     y3 = point3.getY()

#     #door width is 1/5 house width
#     r_width = x2 - x1
#     door = Rectangle(Point(x3-(1/10 * r_width), y1), Point(x3+(1/10 * r_width), y3))
#     door.draw(win)
#     message.setText("Now click to place a window.")

#     #Click four will print a square window
#     point4 = win.getMouse()
#     x4 = point4.getX()
#     y4 = point4.getY()
    
#     #window is 1/2 width door (z is variable for distance off center)
#     z = 1/20 * r_width
#     window = Rectangle(Point((x4-z), (y4-z)), Point((x4+z), (y4+z)))
#     window.draw(win)
#     message.setText("Finally, click the crown of the roof!")

#     #Click five will indicate peak of roof
#     point5 = win.getMouse()
#     line1 = Line(point2, point5)
#     line1.draw(win)
#     line2 = Line(point5, Point(x1, y2))
#     line2.draw(win)
#     message.setText("Welcome, to your new home.")

#     win.getMouse()
#     win.close()

# main()


# # def main():
# #     win = GraphWin("Triangle Information", 400, 400)

# #     p1 = win.getMouse()
# #     p2 = win.getMouse()
# #     p3 = win.getMouse()
# #     p4 = win.getMouse()
# #     p5 = win.getMouse()

# #     houseWidth = p2.getX() - p1.getX()
# #     doorWidth = houseWidth/10
# #     windowWidth = doorWidth/2
# #     house = Rectangle(Point(p1.getX(),p1.getY()), Point(p2.getX(),p2.getY())).draw(win)
# #     door = Rectangle(Point((p3.getX()+doorWidth),p3.getY(), Point((p3.getX()+doorWidth),p1.getY()))).draw(win)
# #     window = Rectangle(Point((p4.getX()+windowWidth),(p4.getY()+windowWidth), Point((p4.getX()-windowWidth),(p4.getY()-windowWidth)))).draw(win)
# #     roof = Polygon(Point(p1.getX(),p2.getY()), Point(p2.getX(),p2.getY()), Point(p5.getX(),p5.getY())).draw(win)

# #     quit = Text(Point(200, 10), "Click again to quit")
# #     quit.setStyle("bold")
# #     quit.draw(win)
# #     win.getMouse()
# #     win.close()

# # main()

