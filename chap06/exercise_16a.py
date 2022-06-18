# Me Computer, Mandalay.
# June 17, 2022
# exercise_16.py
# This program will draw simple (or grim) face

from graphics import *
from math import sqrt

def drawFace(center, size, win):
    # center is a point - generated with a click
    # size is an int
    # win is a GraphWin

    # draw face outline
    face = Oval(Point(center.getX() - size, center.getY() - size), 
        Point(center.getX() + size, center.getY() + size))
    face.setFill(color_rgb(37, 31, 35))
    face.draw(win)

    # draw chest
    chest = Oval(Point(center.getX() - size * .50, center.getY() + size * .50), 
        Point(center.getX() + size * .45, center.getY() + size))
    chest.setFill(color_rgb(223, 222, 222))
    chest.draw(win)

    # draw eyes
    lEye = Oval(Point(center.getX() - size * .80, center.getY() - size * .20), 
        Point(center.getX() - size * .50, center.getY() + size * .20))
    lEye.setFill(color_rgb(223, 222, 222))
    lEye.draw(win)

    rEye = lEye.clone()
    rEye.move(size * .5, 0)
    rEye.draw(win)    
    # draw pupils
    lPupil = Oval(Point(center.getX() - size * .75, center.getY() - size * .10), 
        Point(center.getX() - size * .55, center.getY() + size * .20))
    lPupil.setFill(color_rgb(37, 31, 35))
    lPupil.draw(win)

    rPupil = lPupil.clone()
    rPupil.move(size * .5, 0)
    rPupil.draw(win)
    # draw beak
    topBeak = Polygon(Point(center.getX() - size * .80, center.getY() + size * .40), 
        Point(center.getX() - size * .40, center.getY() - size * .05), 
        Point(center.getX(), center.getY() + size * .40), 
        Point(center.getX() - size * .60, center.getY() + size * .50))
    topBeak.setFill(color_rgb(252, 210, 2))
    topBeak.draw(win)
    # draw nose
    lNostril = Oval(Point(center.getX() - size * .45, center.getY() + size * .10), 
        Point(center.getX() - size * .50, center.getY() + size * .18))
    lNostril.setFill(color_rgb(37, 31, 35))
    lNostril.draw(win)

    rNostril = lNostril.clone()
    rNostril.move(size * .12, 0)
    rNostril.draw(win)

def drawPointAtClick(center, win):
    centerPoint = Circle(center, 3)
    centerPoint.setFill("red")
    centerPoint.draw(win)
    return centerPoint

def textStyle(textObj, win):
    textObj.setTextColor(color_rgb(252, 85, 2))
    textObj.setStyle("bold")
    textObj.setSize(14)
    textObj.setFace("helvetica")
    textObj.draw(win)

def main():
    # open grapics win
    win = GraphWin("Faces", 666, 500)
    center = Point(333, 250)
    base = Point(333, 450)

    # load photo
    imageImported = Image(center, "exercise_16.gif")

    # display image in graphwin same width and height as image
    imageImported.draw(win)

    # how many faces are being blocked
    prompt = Text(Point(300, 100), "How many faces do you want to block?")
    textStyle(prompt, win)
    # create input box
    inputBox = Entry(Point(500, 100), 3)
    inputBox.setText("2")
    inputBox.draw(win)
    # create button & get click
    button = Text(base, "< Click to continue >")
    textStyle(button, win)
    win.getMouse()
    nFaces = int(inputBox.getText())

    # loop to create faces
    inputBox.undraw()
    button.undraw()
    for i in range(1, nFaces + 1):
        # click center
        prompt.setText("Click the center of face number {0}.".format(i))
        centerFace = win.getMouse()
        cfPoint = drawPointAtClick(centerFace, win)

        # click edge
        prompt.setText("Click the edge of face number {0}.".format(i))
        edgeFace = win.getMouse()
        efPoint = drawPointAtClick(edgeFace, win)

        # draw graphics in graphwin
        slopeX = edgeFace.getX() - centerFace.getX()
        slopeY = edgeFace.getY() - centerFace.getY()
        size = sqrt(slopeX**2 + slopeY**2)
        drawFace(centerFace, size, win)

        cfPoint.undraw()
        efPoint.undraw()
    prompt.undraw()

    # End Program
    endText = Text(base, "Click Again To Quit!")
    textStyle(endText, win)
    win.getMouse()
    win.close()

main()

# from graphics import *

# def drawFace(center, size, window):
#     x1 = center.getX()
#     y1 = center.getY()
#     p1 = Point(x1-(.7 * size), y1 - size)
#     p2 = Point(x1+(.7 * size), y1 + size)

#     head = Oval(p1, p2)
#     head.setFill("white")
#     head.draw(window)

#     lc = Point(x1 - .2 * size, y1 + .6 * size)
#     rc = Point(x1 + .2 * size, y1 + .6 * size)

#     leftEye = Circle(lc, .13 * size)
#     leftEye.setFill("white")
#     leftEye.draw(window)

#     rightEye = Circle(rc, .13 * size)
#     rightEye.setFill("white")
#     rightEye.draw(window)

#     m1 = Point(x1 - .3 * size, y1 - .5 * size)
#     m2 = Point(x1 + .3 * size, y1 - .25 * size)
#     m3 = Point(x1 + .3 * size, y1 - .5 * size)

#     mouth = Rectangle(m1, m2)
#     mouth.setFill("white")
#     mouth.draw(window)

#     leftLip = Line(m1, Point(x1- .3 * size, y1 - .25 * size))
#     mLeftCent = leftLip.getCenter()

#     mLCx = mLeftCent.getX()
#     mLCy = mLeftCent.getY()

#     mRightCent = Point(x1 + .3 * size, mLCy)

#     lip = Line(mLeftCent, mRightCent)
#     lip.draw(window)

#     m1x = m1.getX()
#     m3x = m3.getX()
#     m1y = m1.getY()
#     m2y = m2.getY()

#     t = m1x - m3x
#     t1 = Point(m1x - (1/8 * t), m2y)
#     teeth = Rectangle(m1, t1)
#     teeth.draw(window)

#     for i in range (7):
#         t2 = teeth.clone()
#         t2.move(-i * (1/8 * t), 0)
#         t2.draw(window)

# def main():
#     fname = input("Enter filename: ")
#     infile = Image(Point(10, 10), fname)
#     wWidth = infile.getWidth()
#     wHeight = infile.getHeight()
    
#     window = GraphWin('Smile!', wWidth,wHeight)
#     window.setCoords(0, 0, 20, 20)
#     infile.draw(window)
#     #get file    

#     #save number of faces as (n)
#     n = eval(input("How many faces should we block? "))    

#     for i in range(n):
#         point = window.getMouse()
#         drawFace(point, 3, window)

#     input("Press <Enter> to quit")
#     window.close()    

# main()
