# Me Computer, Mandalay.
# June 15, 2022
# exercise_11.py

# 11. Five-click House.
#     You are to write a program that allows the user to draw a simple house using five mouse clicks. The fisrt two clicks will be the opposite
#     corners of the rectangular frame of the house. The third click will indicate the center of the otp ege of a rectangular door. The door should
#     have a total width that is 1/5 the wdith of the house frame. The sides of the door should have extend from the corners of the top down to the
#     bottom of the frame. The fourth click will indicate the center of a square window. The window is half as wide as the door. The last click will
#     indicate the peak of the roof. The edges of the roof will extend from the point at the peak to the corners of the top edge of the house frame.

from graphics import *

def main():
    win = GraphWin("Design a House",500,500)
    win.setCoords(0, 0, 200, 200)
    message = Text(Point(100,5),"")
    message.draw(win)

    # Draw the frame of the house
    message.setText("Click on lower left corner of the frame")
    frameLL = win.getMouse()
    frameLL.draw(win)
    message.setText("Click upper right corner of the frame")
    frameUR = win.getMouse()
    frameLL.undraw()
    Rectangle(frameLL, frameUR).draw(win)

    # Draw a door
    houseWidth = frameUR.getX() - frameLL.getX()
    doorWidth = 0.2 * houseWidth
    halfDoor = doorWidth/2.0
    message.setText("Click on the center of the top of the door")
    doorPt2 = win.getMouse()
    doorPt2.move(halfDoor, 0)
    doorX1 = doorPt2.getX() - doorWidth
    doorY1 = frameLL.getY()
    door = Rectangle(Point(doorX1,doorY1), doorPt2)
    door.setFill("red")
    door.draw(win)

    # Draw a window
    message.setText( "Click on the center of the window")
    windowCenter = win.getMouse()
    w1 = windowCenter.clone()
    winOff = 0.5 * halfDoor
    w1.move(-winOff,winOff)
    w2 = windowCenter.clone()
    w2.move(winOff, -winOff)
    Rectangle(w1,w2).draw(win)

    # Draw the roof
    message.setText( "Click on the peak of the roof")
    peak = win.getMouse()
    frameUL = frameUR.clone()
    frameUL.move(-houseWidth,0)
    roof = Polygon(frameUL, peak, frameUR)
    roof.draw(win)
    roof.setFill("black")
    
    message.setText( "Click anywhere to quit." )
    win.getMouse()
    win.close()

main()
