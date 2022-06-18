########################
#Main file for Pong game

from graphics import *
from paddle import *
from ball import *

edges = dict(top=0.90, right=0.95, bottom=0.05, left=0.05)

win = GraphWin("SI182 - Pong Game", 300,300)
win.setCoords(0,0,1,1)

txt = Text(Point(0.9,0.95), "quit")
txt.draw(win)

txt2 = Text(Point(0.1, 0.95), "Reset")
txt2.draw(win)

paddle = Paddle(win)
ball = Ball(paddle, edges)

gameover = Text(Point(0.5,0.5), "Game Over")

playing = True
win.clearLastMouse()
while True:
    if playing:
        ball.move()
        
        if ball.outOfPlay():
            print "Game over"
            gameover.draw(win)
            playing = False
            continue

    time.sleep(0.05)

    pos = win.getLastMouse()
    if pos != None :
        win.clearLastMouse()
        print "CLICK", pos
        if pos.getX() < 0.2 and pos.getY() > 0.9:
            print "Restarting"
            ball.reset()
            paddle.reset()
            gameover.undraw()
            playing = True
            continue

        if pos.getX() > 0.8 and pos.getY() > 0.9:
            print "Quitting"
            break

        if pos.getY() < 0.2 :
            paddle.move(pos.getX())

win.close()
