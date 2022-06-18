# Me Computer, Mandalay.
# June 17, 2022
# exercise_17.py
# This program will draw a circle

from graphics import *

def moveTo(shape, newCenter):
    # shape is a graphics object that supports the getCenter method
    # newCenter is a point
    # moves shape so that newCenter is its center
    shape.undraw()
    shape = Circle(newCenter, 20)
    shape.setOutline("red")
    shape.setFill("red")
    return shape

def main():
    win = GraphWin("Shape Space", 500, 500)
    center = Point(250, 250)
    base = Point(250, 450)

    shape = Circle(center, 20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    
    prompt = Text(base, "Click new center point...")
    prompt.draw(win)
    for i in range(10):
        p = win.getMouse()
        shape = moveTo(shape, p)
        shape.draw(win)
    prompt.undraw()

    endText = Text(base, "Click again to quit.")
    endText.draw(win)
    win.getMouse()
    win.close()

main()

# from graphics import *

# def moveTo(shape, newCenter, win):
#     dx = oldCenter.getX() - newCenter.getX()
#     dy = oldCenter.getY() - newCenter.getY()

#     shape.move(dx, dy)
#     #shape.draw(win)

# def main():
#     win = GraphWin("Move Shape", 400, 400)
#     win.setCoords(0, 0, 100, 100)

#     oldCenter = win.getMouse()
#     shape = Circle(oldCenter, 3)
#     shape.setOutline("red")
#     shape.setFill("red")
#     shape.draw(win)

#     for i in range(10):
#         newCenter = win.getMouse()
#         moveTo(shape, newCenter, win)

#     input("Press <Enter> to quit")
#     window.close()

# main()
