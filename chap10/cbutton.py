from graphics import *
import math

class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method 
    returns true if the button is and active and p is inside it."""

    def __init__(self, win, center, radius, label):
        """Creates a circular button, eg:
        qb = Button(myWin, centerPoint, radius, 'Quit')"""
        self.x, self.y = center.getX(), center.getY()
        self.radius = radius
        self.circle = Circle(Point(self.x, self.y), radius)
        self.circle.setFill('lightgrey')
        self.circle.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.activate()

    def activate(self):
        "Sets this button to 'active' "
        self.label.setFill('black')
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive' "
        self.label.setFill('darkgrey')
        self.active = False

    def clicked(self, p):
        "Returns true if button is active and p is inside"
        dist = math.sqrt((self.x - p.getX()) ** 2 + (self.y - p.getY()) ** 2)
        return self.active and dist <= self.radius

    def getLabel(self):
        "Returns the label string of this button"
        return self.label.getText()
        