# Me Computer, Mandalay.
# June 17, 2022
# exercise_15.py
# This program will draw simple (or grim) face

from graphics import *

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

def main():
    # open grapics win
    win = GraphWin("Faces", 600, 600)
    center = Point(300, 300)
    base = Point(300, 550)

    # draw face 1
    face1 = drawFace(Point(300, 300), 150, win)
    # draw face 2
    face2 = drawFace(Point(450, 400), 20, win)
    # draw face 3
    face2 = drawFace(Point(100, 200), 50, win)
    # draw face 4
    face2 = drawFace(Point(100, 400), 75, win)

    # End Program
    endText = Text(base, "Click again to quit.")
    endText.draw(win)
    win.getMouse()
    win.close()

main()
