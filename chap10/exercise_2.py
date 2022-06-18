# Me Computer, Mandalay.
# June 21, 2022
# exercise_2.py
# graphical program for Celsius Converter

from graphics import *

from button import Button

def main():
    win = GraphWin("Celsius Converter", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    Text(Point(1, 3), " Celsius Temperature: ").draw(win)
    Text(Point(1, 1), " Fahrenheit Temperature: ").draw(win)
    input = Entry(Point(2, 3), 5)
    input.setText("0.0")
    input.draw(win)
    output = Text(Point(2, 1), "")
    output.draw(win)

    convertButton = Button(win, Point(0.75, 2.0), 1, 1, "Convert")
    quitButton = Button(win, Point(2.25, 2.0), 1, 1, "Quit")

    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if convertButton.clicked(pt):
            celsius = eval(input.getText())
            fahrenheit = 9.0 / 5.0 * celsius + 32
            output.setText(fahrenheit)
        pt = win.getMouse()
    
    win.close()

if __name__ == '__main__': main()
