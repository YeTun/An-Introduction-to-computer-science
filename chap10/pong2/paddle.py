###########################
#Paddle class for Pong game

from graphics import *

class Paddle:
    
    bottom = 0.05
    initialCenter = 0.5
    center = initialCenter
    width = 0.2
    height = 0.05
    color = 'blue'

    rect = None
    window = None

    def __init__(self, window):
        self.window = window
        self.create()

    def create(self):
        print "Creating Paddle: ", self.center, self.width, self.height
        self.rect = Rectangle(Point(self.center - self.width/2, self.bottom),
                        Point(self.center + self.width/2, self.bottom + self.height))
        self.rect.setFill(self.color)
        self.rect.draw(self.window)

    def destroy(self):
        print "Destroying paddle"
        self.rect.undraw()

    def reset(self):
        print "Resetting paddle"
        self.destroy()
        self.center = self.initialCenter
        self.create()

    def move(self, X):
        print "Moving paddle", X
        self.center = X
        self.destroy()
        self.create()

    def getWindow(self):
        return self.window

    def getTop(self):
        #Returns the Y coordinate of the top right corner (P2)
        return self.rect.getP2().getY()

    def getRight(self):
        #Returns the X coordinate of top right corner (P2)
        return self.rect.getP2().getX()

    def getBottom(self):
        #Returns the Y coordinate of the bottom left corner (P1)
        return self.rect.getP1().getY()
        
    def getLeft(self):
        #Returns the X coordinate of the bottom left corner (P1)
        return self.rect.getP1().getX()

