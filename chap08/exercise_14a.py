# Me Computer, Mandalay.
# June 19, 2020
# exercise_14.py
# This program converts a color image to grayscale

from graphics import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

def openGraphicsWindow(title, width, height, image):
    # open grapics window
    win = GraphWin(title, width, height)
    win.setBackground(color_rgb(56, 54, 53))
    # center image in window
    image.move(width / 2, height / 2)
    image.draw(win)
    return win

def openFile():
    # open file
    infileName = askopenfilename()
    infile = open(infileName, "r")
    return infile

def openImage():
    # open PPM or GIF file
    infileName = askopenfilename()
    # need to update point to center based on size of image
    image = Image(Point(0, 0), infileName)
    return image

def createButton(win):
    button = Rectangle(Point(1, 1), Point(250, 40))
    button.setOutline(color_rgb(244, 188, 15))
    button.setFill(color_rgb(119, 94, 57))
    button.draw(win)
    buttonText = Text(button.getCenter(), "Convert to Greyscale")
    buttonText.setTextColor(color_rgb(244, 188, 15))
    buttonText.draw(win)
    return button, buttonText

def greyscale(win, image, width, height):
    # converts pixels to greyscale and shows progress row by row
    for y in range(height):
        for x in range(width):
            r, g, b = image.getPixel(x, y)
            brightness = int(round(0.299 * r + 0.587 * g + 0.114 * b))
            image.setPixel(x, y, color_rgb(brightness, brightness, brightness))
        image.undraw()
        image.draw(win)

def saveFile(image):
    saveFileName = asksaveasfilename()
    if saveFileName != "":
        image.save(saveFileName)

def main():
    # open and display file
    image = openImage()
    # open window
    width = image.getWidth()
    height = image.getHeight()
    win = openGraphicsWindow("Greyscale Editor", width, height, image)

    # click to convert
    button, buttonText = createButton(win)
    win.getMouse()
    greyscale(win, image, width, height)

    # prompt for filename to save new file
    saveFile(image)

    # wait for click to quit
    button.undraw()
    buttonText.undraw()
    buttonText.setText("Click to quit.")
    button.draw(win)
    buttonText.draw(win)
    win.getMouse()

main()
