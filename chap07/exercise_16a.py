# Me Computer, Mandalay.
# June 18, 2022
# exercise_16.py

from graphics import *
from math import sqrt

def calculateDistance(pointObj, center):
    # calculate slope
    slopeX = pointObj.getX() - center.getX()
    slopeY = pointObj.getY() - center.getY()
    if slopeX != 0:
        slope = slopeY / slopeX
        # calculate length
        length = sqrt(slopeX**2 + slopeY**2)
    else:
        length = pointObj.getY() - center.getY()
    return length

def main():
    # Creates the window for the Archery Target
    win = GraphWin("Archery Target", 500, 500)
    win.setCoords(-5, -5, 5, 5)
    center = Point(0, 0)

    # Draws 1st ring - white - maximum radius
    radius = 5
    first = Circle(center, radius)
    first.setFill("white")
    first.setOutline("black")
    first.draw(win)

    # Draws 2nd Ring - black - radius-1
    radius -= 1
    second = Circle(center, radius)
    second.setFill("black")
    second.setOutline("black")
    second.draw(win)

    # Draws 3nd Ring - blue - radius-1
    radius -= 1
    third = Circle(center, radius)
    third.setFill("blue")
    third.setOutline("black")
    third.draw(win)

    # Draws 4nd Ring - red - radius-1
    radius -= 1
    fourth = Circle(center, radius)
    fourth.setFill("red")
    fourth.setOutline("black")
    fourth.draw(win)

    # Draws 5nd Ring (center) - yellow - radius-1
    radius -= 1
    fifth = Circle(center, radius)
    fifth.setFill("yellow")
    fifth.setOutline("black")
    fifth.draw(win)

    # 5 rounds of clicks
    score = 0
    for i in range(1, 6):
        prompt = Text(Point(3, 4), "Click to take shot #{0}...".format(i))
        prompt.setFill("red")
        prompt.setSize(16)
        prompt.draw(win)
        scoreBox = Text(Point(-4, -4), "Score: {0}".format(score))
        scoreBox.setFill("black")
        scoreBox.setSize(16)
        scoreBox.draw(win)
        shot = win.getMouse()
        mark = Circle(shot, 0.1)
        mark.setFill("green")
        mark.draw(win)
        if calculateDistance(shot, center) < 1:
            score += 9
        elif calculateDistance(shot, center) < 2:
            score += 7
        elif calculateDistance(shot, center) < 3:
            score += 5
        elif calculateDistance(shot, center) < 4:
            score += 3
        elif calculateDistance(shot, center) < 5:
            score += 1
        else:
            score += 0
        prompt.undraw()
        scoreBox.undraw()

    # Get click to quit and close window
    scoreBox = Text(Point(-4, -4), "Score: {0}".format(score))
    scoreBox.setFill("black")
    scoreBox.setSize(16)
    scoreBox.draw(win)
    endText = Text(center, "Click again to quit.")
    endText.draw(win)
    win.getMouse()
    win.close()

main()


# from graphics import *
# import math as m

# def main():
#     win = GraphWin()
#     win.setCoords(-5, -5, 5, 5)
#     c = Circle(Point(0,0), 5)
#     c.setOutline("green4")
#     c.setFill("white")
#     c.setWidth(1)
#     c.draw(win)

#     c2 = Circle(Point(0,0), 4)
#     c2.setOutline("green4")
#     c2.setFill("red")
#     c2.setWidth(1)
#     c2.draw(win)

#     c3 = Circle(Point(0,0), 3)
#     c3.setOutline("green4")
#     c3.setFill("blue")
#     c3.setWidth(1)
#     c3.draw(win)

#     c4 = Circle(Point(0,0), 2)
#     c4.setOutline("green4")
#     c4.setFill("black")
#     c4.setWidth(1)
#     c4.draw(win)

#     c5 = Circle(Point(0,0), 1)
#     c5.setOutline("green4")
#     c5.setFill("white")
#     c5.setWidth(1)
#     c5.draw(win)

#     sum = 0
#     for x in range (5):
#         arrow = win.getMouse()
#         x = arrow.getX()
#         y = arrow.getY()
#         z = m.sqrt(x ** 2 + y ** 2)
        
#         if 5 >= z > 4:
#             y = 1
#             sum = y + sum
#         elif 4 >= z > 3:
#             y = 3
#             sum = y + sum
#         elif 3 >= z > 2:
#             y = 5
#             sum = y + sum
#         elif 2 >= z > 1:
#             y = 7
#             sum = y + sum
#         elif 1 > z:
#             y = 9
#             sum = y + sum
#         else:
#             y = 0
#             print("You missed!")
#         print("Point: {0}    Total: {1}".format(y, sum))

# main()
