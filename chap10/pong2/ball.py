#########################
#Ball class for Pong game

from graphics import *
import paddle

class Ball:

    initialX = 0.3
    initialY = 0.5
    radius = 0.02
    color = 'red'
    
    velocity = 0.01
    dx = velocity
    dy = velocity

    window = None
    circle = None
    paddle = None
    edges = None

    def __init__(self, paddle, edges):
        self.paddle = paddle
        self.edges = edges
        self.window = paddle.getWindow()
        self.create()

    def create(self):
        print "Creating ball", self.initialX, self.initialY, self.radius, self.color
        self.circle = Circle(Point(self.initialX, self.initialY), self.radius)
        self.circle.setFill(self.color)
        self.circle.draw(self.window)

    def destroy(self):
        print "Destroying ball"
        self.circle.undraw()

    def reset(self):
        print "Resetting ball"
        self.destroy()
        self.dx = self.velocity
        self.dy = self.velocity
        self.create()

    def move(self):
        print "Moving ball: ", self.circle.getCenter(), self.dx, self.dy
        self.circle.move(self.dx, self.dy)
        where = self.circle.getCenter()

        #Check left/right edges
        if where.getX() < self.edges['left'] or where.getX() > self.edges['right']:
            self.dx = self.dx * -1.0

        #Check top edge
        if where.getY() > self.edges['top']:
            self.dy = self.dy * -1.0

        #Bounce off the paddle if we collide with it
        if self.collides():
            self.dy = self.dy * -1.0
            self.circle.move(self.dx, self.dy)

    def collides(self):
        #Check against paddle
        where = self.circle.getCenter()
        return  where.getX() > self.paddle.getLeft() and \
                where.getX() < self.paddle.getRight() and \
                where.getY() < self.paddle.getTop() + self.radius

    def outOfPlay(self):
        #Check if we're below the paddle
        #Move handles hits, so we just check the Y coordinate
        where = self.circle.getCenter()
        return where.getY() < self.edges['bottom']
        #return  where.getY() < self.paddle.getBottom() + self.radius

