# Me Computer, Mandalay.
# June 15, 2022
# exercise_1b.py
# Move squares at mouse click point

from graphics import *

def main():
    win = GraphWin()
    win.setCoords(0, 0, 10, 10)
    
    square = Rectangle(Point(4, 4), Point(5, 5))
    square.setOutline("red")
    square.setFill("red")
    square.draw(win)
    
    for i in range(10):
        square = square.clone()                
        p = win.getMouse()
        c = square.getCenter()

        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()

        square.move(dx, dy)
        square.draw(win)
        
    # Wait for another click to exit
    message = Text(Point(5, 9),"Click again to quit.")
    message.draw(win)
    win.getMouse()
    win.close()

main()

