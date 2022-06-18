# Me Computer, Mandalay.
# June 18, 2022
# exercise_17.py

from graphics import *

def main():
    # Creates the window for the bouncing ball
    win = GraphWin("Bouncing Ball", 500, 500)
    center = Point(250, 250)

    # draw ball
    ball = Circle(center, 50)
    ball.setFill("yellow")
    ball.draw(win)

    # ball movement
    dx = 2
    dy = 1
    for i in range(1000):
        ballX = ball.getCenter().getX()
        ballY = ball.getCenter().getY()
        if ballX == 450:
            dx = -1
        if ballY == 450:
            dy = -1
        if ballX == 50:
            dx = 2
        if ballY == 50:
            dy = 1
        ball.undraw()
        ball.move(dx, dy)
        ball.draw(win)
        update(30) # pause so rate is not more than 30 times a second

    # wait for click to end
    endText = Text(center, "Click again to quit.")
    endText.draw(win)
    win.getMouse()
    win.close()

main()


# from graphics import *
# from time import sleep
# import math as m

# def main():
#     win = GraphWin("Bouncing Ball", 500, 500)
#     win.setCoords(-100, -100, 100, 100)

#     shape = Circle(Point(0,-80),20)
#     shape.setOutline("red")
#     shape.setFill("red")
#     shape.draw(win)

#     dx = 1
#     dy = 1

#     for i in range(10000):
#         c = shape.getCenter()
        
#         if c.getX() > 80:
#             dx = -1
#         elif c.getX() < -80:
#             dx = 1
#         elif c.getY() > 80:
#             dy = -1
#         elif c.getY() < -80:
#             dy = 1
           
#         sleep(0.005)
#         shape.move(dx,dy)
# main()
