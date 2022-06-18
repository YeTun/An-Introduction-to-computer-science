#! /usr/bin/python
# Exercise No.   01
# File Name:     hw12project1.py
# Programmer:    John Rollinson
# Date:          11/13/2019
#
# Problem Statement:
# Modify the dice poker program from this chapter to include any or all of the following features:
#   Splash screen. When the program first fires up, have it print a short introductory message about
#   the program and buttons for "Let's Play" and "Exit". The main interface shouldn't appear unless
#   the user selects "Let's Play".
#   
#   Add a help button that pops up another window displaying the rules of the game (the payoffs table
#   is the most important part).
#   
#   Add a high score feature. The program should keep track of the 10 best scores. When a user quits
#   with a good enough score, he/she is invited to type in a name for the list. The list should be
#   printed in the splash screen whent he program first runs. The high-scores list will have to be stored
#   in a file so that it persists between program invocations.
#
# Overall Plan:
# 1. Import all the required classes given in the book, Here the required classes are: pokerapp.py,
#       graphicsinterface.py, button.py, graphics.py, dieview2.py.
# 2. Define a method splashScreen() to show the splash screen.
# 3. Define a method main() which will start the splash screen first.
# 4. The features for the help button, close window of help screen and asking for the name of the
#       user for having a high score are listed in graphicsinterface.py
# 5. Define method help() to set up a help screen.
# 6. Define a method inputName_HighScore() to set up a screen for entering a name.
# 7. To track the list of persons having high scores the methods should be defined in a pokerapp.py.
# 8. Define a method make_ScoreList() to make the list of scores.
# 9. Define a method is_HighScore() to check the high score.
# 10. Define a method add_Person() to add a person in the list of high scores.
# 11. Define a method remove_Person() to remove a person from the list of high scores.
# 12. Define a method printTo_File() to print the name and score of a person in a file.
#
# import the necessary python libraries
from random import *
from graphics import *

class Dice:
    def __init__(self):
        self.dice = [0] * 5
        self.rollAll()

    def roll(self, which):
        for pos in which:
            self.dice[pos] = randrange(1, 7)

    def rollAll(self):
        self.roll(range(5))

    def values(self):
        return self.dice[:]

    def score(self):
        counts = [0] * 7
        for value in self.dice:
            counts[value] = counts[value] + 1

        if 5 in counts:
            return "Five of a Kind", 30
        elif 4 in counts:
            return "Four of a Kind", 15
        elif (3 in counts) and (2 in counts):
            return "Full House", 12
        elif 3 in counts:
            return "Three of a Kind", 8
        elif not (2 in counts) and (counts[1] == 0 or counts[6] == 0):
            return "Straight", 20
        elif counts.count(2) == 2:
            return "Two Pairs", 5
        else:
            return "Garbage", 0

class dieview2:
    def __init__(self, win, center, size):
        self.win = win
        self.background = "white" #color of the die face
        self.foreground = "black" #color of the pips
        self.psize = 0.1 * size   #radius of each pip
        hsize = size / 2.0  
        offset = 0.6 * hsize

        #create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx - hsize, cy - hsize)
        p2 = Point(cx + hsize, cy + hsize)
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)

        self.pips = [self.__makePip(cx - offset, cy - offset),
                     self.__makePip(cx - offset, cy),
                     self.__makePip(cx - offset, cy + offset),
                     self.__makePip(cx, cy),
                     self.__makePip(cx + offset, cy - offset),
                     self.__makePip(cx + offset, cy),
                     self.__makePip(cx + offset, cy + offset)]

        self.onTable = [ [], [3], [2, 4], [2, 3, 4], [0, 2, 4, 6],
                         [0, 2, 3, 4, 6], [0, 1, 2, 4, 5, 6] ]

        self.setValue(1)

    def __makePip(self, x, y):
        pip = Circle(Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        for pip in self.pips:
            pip.setFill(self.background)

        for i in self.onTable[value]:
            self.pips[i].setFill(self.foreground)
    
class Button:
    def __init__(self, win, center, width, height, label):
        w, h = width / 2.0, height / 2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <=self.xmax and
                self.ymin <= p.getY() <=self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

    
class PokerApp:
    def __init__(self, interface):
        self.dice = Dice()
        self.money = 100
        self.interface = interface
        
    def run(self):
        while self.money >= 10 and self.interface.wantToPlay():
            self.playRound()
        self.interface.close()

    def playRound(self):
        self.money = self.money - 10
        self.interface.setMoney(self.money)
        self.doRolls()
        result, score = self.dice.score()
        self.interface.showResult(result, score)
        self.money = self.money + score
        self.interface.setMoney(self.money)

    def doRolls(self):
        self.dice.rollAll()
        roll = 1
        self.interface.setDice(self.dice.values())
        toRoll = self.interface.chooseDice()
        while roll < 3 and toRoll != []:
            self.dice.roll(toRoll)
            roll = roll + 1
            self.interface.setDice(self.dice.values())
            if roll < 3:
                toRoll = self.interface.chooseDice()

    def make_ScoreList(self):
        score_List = []
        infile = open('HighScores.txt', 'r')
        for line in infile:
            name1, score = line.split()
            tuple = (name1, score)
            score_List.append(tuple)
        return score_List

    def is_HighScore(self):
        new_Score = self.getMoney()
        list = self.make_ScoreList()
        flag = False
        if len(list) == 10:
            for tuple in list:
                score = int(tuple[1])
                if new_Score > score:
                    flag = True
                else:
                    flag = True
        return flag

    def add_Person(self):
        score = self.getMoney()
        name1 = self.interface.inputName_HighScore()
        if name1 == "":
            name1 = "guest"
            tuple = (name1, score)
            list = self.remove_Person()
            list.append(tuple)
        return list

    def remove_Person(self):
        list = self.make_ScoreList()
        if len(list) == 10:
            tracker_Number = 10000
            tracker_Tuple = None
            for tuple in list:
                score = int(tuple[1])
                if score < tracker_Number:
                    tracker_Number = score
                    tracker_Tuple = tuple
                    list.remove(tracker_Tuple)
        return list

    def printTo_File(self, list):
        outfile = open('HighScores.txt', 'w')
        for tuple in list:
            name1, score = tuple
            print(name1, score, file = outfile)
        outfile.close()

class GraphicsInterface:
    def __init_(self):
        self.win = GraphWin("Dice Poker", 600, 400)
        self.win.setBackground("green3")
        
        banner = Text(Point(300, 30), "Python Poker Parlor")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)
        
        self.msg = Text(Point(300, 380), "Welcome to the Dice Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        
        self.createDice(Point(300, 100), 75)
        self.buttons = []
        self.addDiceButtons(Point(300, 170), 75, 30)
        
        b = Button(self.win, Point(300, 230), 400, 40, "Roll Dice")
        self.buttons.append(b)
        b = Button(self.win, Point(300, 280), 150, 40, "Score")
        self.buttons.append(b)
        b = Button(self.win, Point(570, 375), 40, 30, "Quit")
        self.buttons.append(b)
        
        self.money = Text(Point(300, 325), "$100")
        self.money.setSize(18)
        self.money.draw(self.win)

    def createDice(self, center, size):
        center.move(-3 * size, 0)
        self.dice = []
        for i in range(5):
            view = DieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5 * size, 0)

    def addDiceButtons(self, center, width, height):
        center.move(-3 * width, 0)
        for i in range(1, 6):
            label = "Die {0}".format(i)
            b = Button(self.win, center, width, height, label)
            self.buttons.append(b)
            center.move(1.5 * width, 0)

    def setMoney(self, amt):
        self.money.setText("${0}".format(amt))

    def showResult(self, msg, score):
        if score > 0:
            text = "{0}! You win ${1}".format(msg, score)
        else:
            text = "You rolled {0}".format(msg)
        slef.msg.setText(text)

    def setDice(self, values):
        for i in range(5):
            self.dice[i].setValue(values[i])

    def wantToPlay(self):
        ans = self.choose(["Roll Dice", "Quit"])
        self.msg.setText("")
        return ans == "Roll Dice"

    def chooseDice(self):
        choices = []
        while True:
            b = self.choose(["Die 1", "Die 2", "Die 3", "Die 4", "Die 5", "Roll Dice", "Score"])
            if b[0] == "D":
                i = eval(b[4]) - 1
                if i in choices:
                    choices.remove(i)
                    self.dice[i].setColor("black")
                else:
                    choices.append(i)
                    self.dice[i].setColor("gray")
            else:
                for d in self.dice:
                    d.setColor("black")
                if b == "Score":
                    return[]
                elif choices != []:
                    return choices

    def choose(self, choices):
        buttons = self.buttons

        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()
        
    def close(self):
        self.win.close()

    def help(self):
        help_Win = GraphWin("Help", 700, 400)
        help_Win.setBackground("white")
        rules_Text = Text(Point(300, 30), "Rules for the Game:")
        rules_Text.setSize(20)
        rules_Text.draw(help_Win)
        rule = [Text(Point(290, 100), "A player initially has $100. Each round deducts $10 from cost to play."),
                Text(Point(180, 120), "A player initially rolls a dice randomly."),
                Text(Point(245, 140), "Dice can be rolled up again for twice (any number of dice)."),
                Text(Point(200, 240), "Pay for game Schedule:")]
        for rule in rule:
            rule.draw(help_Win)
            rule.setSize(14)
            payout = [Text(Point(135, 280), "2 Pairs, $5"),
                      Text(Point(148, 300), "3 of a Kind, $8"),
                      Text(Point(150, 320), "Full House, $12"),
                      Text(Point(150, 340), "4 of a Kind, $15"),
                      Text(Point(135, 360), "Straight, $20"),
                      Text(Point(150, 380), "5 of a Kind, $30")]
            for num in payout:
                num.draw(help_Win)
                num.setSize(16)
        close_Button = Button(help_Win, Point(60, 40), 80, 40, "x")
        close_Button.activate()
        p = help_Win.getMouse()
        if close_Button.clicked(p):
            help_Win.close()

    def inputName_HighScore(self):
        highScore_Win = GraphWin("High Score!", 700, 400)
        highScore_Win.setBackground("lightgray")
        highScore_Msg = Text(Point(300, 125), "You got a high score!")
        highScore_Msg.setSize(22)
        highScore_Msg.draw(highScore_Win)
        input_Msg = Text(Point(140, 250), "Please enter your name with no spaces:")
        input_Msg.setSize(12)
        input_Msg.draw(highScore_Win)
        input = Entry(Point(500, 250), 35)
        input.draw(highScore_Win)
        enter_Button = Button(highScore_Win, Point(350, 325), 45, 30, "Enter")
        enter_Button.activate()
        highScore_Win.getMouse()
        name = input.getText()
        highScore_Win.close()
        return name

def splashScreen():
    firstWin = GraphWin("Dice Poker", 600, 400)
    firstWin.setBackground("pink1")

    die = dieview2(firstWin, Point(80, 180), 100)
    die.setValue(4)
    die2 = dieview2(firstWin, Point(520, 270), 100)
    die2.setValue(6)

    Title_Message = Text(Point(195, 40), "Dice Poker:")
    Title_Message.setSize(20)
    Title_Message.draw(firstWin)

    Intro_Message = Text(Point(365, 40), "A game of dice")
    Intro_Message.setSize(20)
    Intro_Message.draw(firstWin)

    High_Scores = Text(Point(290, 100), "High Scores List:")
    High_Scores.setSize(20)
    High_Scores.draw(firstWin)

    play_Button = Button(firstWin, Point(520, 50), 120, 60, "Let's Play!")
    quitButton = Button(firstWin, Point(70, 350), 100, 60, "Quit!")
    play_Button.activate()
    quitButton.activate()

    x = 290
    y = 110
    infile = open('HighScores.txt', 'r')
    for line in infile:
        name, score = line.split()
        y += 25
        msg = Text(Point(x, y), name + ": " + str(score))
        msg.setSize(12)
        msg.draw(firstWin)
    while Ture:
        p = firstWin.getMouse()
        if quitButton.clicked(p):
            firstWin.close()
            return False
        elif play_Button.clicked(p):
            firstWin.close()
            return True

def main():
    x = splashScreen()
    if x:
        inter = GraphicsInterface()
        app = PokerApp(inter)
        app.run()
main()
