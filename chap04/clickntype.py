# clickntype.py
# June 15, 2022
# Page - 109

from graphics import *

def main():
  win = GraphWin("Click and Type", 400, 400)

  for i in range (10):
    pt = win.getMouse()
    key = win.getKey()

    print("You clicked at:", pt.getX(), ":", pt.getY())

    label = Text(pt, key)
    label.draw(win)
  
  win.close()

main()
