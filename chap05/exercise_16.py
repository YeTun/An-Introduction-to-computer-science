# Me Computer, Mandalay.
# June 16, 2022
# exercise_16.py
# Program to count the number of all possible grades from 0 to 10 and output a histogram
# open: quizScores/scores.txt

# 16. Write a program to draw a quiz score histogram. Your program should read data from a file. Each line of the file contains a number
#     in the range 0-10. Your program must count the number of occurences of each score and then draw a vertical bar chart with a bar for
#     each possible score (0-10) with height corresponding to the count of that score. For example, if 15 students got an 8, then the
#     the height of the bar for 8 should be 15.
#     Hint: Use a list that stores the count for each possible score.

#     1. Problem analysis:
#        How to count number of occurences of possible test scores and represent the count on a vertical chart.
#
#     2. Specification:
#        Inputs: file with test scores
#        Output: histogram representing occurences of each score
#
#     3. Design (algorithm)
#        import graphics library
#        import dialog box for opening file
#        get the file name
#        open the file
#        read file
#        create empty list for scores
#        process each line of the input file
#        get each score
#        append each score to empty list in output file
#        count the number of occurences of each score
#        store each count in a new list
#        create graphical template for histogram using a loop
#        define one rectangle (bar) and use variable for height
#        define space between bars as equal to width of one bar
#        label each bar from 0 to 10 using loop count
#        use
#
#     4. Implement

from graphics import *
from tkinter.filedialog import askopenfilename

def main():
    # get filenames
    infileName = askopenfilename()

    # open the files & create objects
    infile = open(infileName, "r")

    # create histogram count by line
    histogramData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for line in infile:
        histogramData[int(line)] += 1

    # Create a graphics window
    win = GraphWin("Student Quiz Score Histogram", 800, 700)
    win.setBackground("white")
    win.setCoords(-1, -1, 11, 11)

    # draw student names
    incrementX = 10 / len(histogramData)
    posX = 0
    for i in range(len(histogramData)):
        Text(Point(posX+0.5, -0.5), i).draw(win)
        count = Rectangle(Point(posX+0.1, 0), Point(posX+0.8, 0+histogramData[i]))
        count.draw(win)
        posX += incrementX

    # End Program
    endText = Text(Point(5, 5), "Click again to quit.")
    endText.setTextColor("red")
    endText.draw(win)
    win.getMouse()
    win.close()

    # Close file
    infile.close()

main()


# # import graphics library
# from graphics import *

# # import dialog box for opening file
# from tkinter.filedialog import askopenfilename

# def main():
#     print("This program creates a histogram from a file of grades.")
#     print("Please select the file containing the grades.")

#     # get the file name
#     infileName = askopenfilename()

#     # create empty list to store scores
#     scores = []
#     # open and read file
#     infile = open(infileName, "r")
#     # process each line of the input file
#     for line in infile:
#         # get the score from line by converting it to int and appending to scores list
#         scores.append(int(line[:-1])) #THIS LINE IS GIVING ME TROUBLE
#     # close file
#     infile.close()
   
#     # create empty list to store score counts
#     scorecounts = []
#     # count the number of occurences of each score and store in a new list
#     for score in range(11):
#         scorecount = [scores].count(score)
#         scorecounts.append(scorecount)
    
#     # creates graphics window
#     histogram = GraphWin("Histogram", 400, 200)
#     histogram.setBackground("yellow")
#     # sets coordinates to simplify drawing of images
#     # note that yur is determined by number of scores + 10
#     histogram.setCoords(0, 0, 115, (len(scores) + 10))

#     # use loop to create graphical template for histogram
#     for i in range(11):
#         bar = Rectangle(Point((5 + (10 * i)), 5), Point((10 + (10 * i)), (scorecounts[i] + 5)))
#         bar.setFill("red")
#         bar.setWidth(3)
#         bar.setOutline("blue")
#         bar.draw(histogram)
#         label = Text(Point((7 + (10 * i)), 2), str(i))
#         label.draw(histogram)

#     print("Histogram has been created.")
#     print("Click anywhere on yellow window to close.")
#     histogram.getMouse()
#     histogram.close()

# main()

# #ERROR: FOR SOME REASONS I AM GETTING EMPTY SCORECOUNTS LIST


# #     5. Test/Debug
# #        create file with 50 different test scores
# #        above version did not work
# #        version below works

# # histogram.py
# # Program to count the number of all possible grades from 0 to 10 and output a histogram
# # this version works

# # import graphics library
# from graphics import *

# # import dialog box for opening file
# from tkinter.filedialog import askopenfilename

# def main():
#     print("This program creates a histogram from a file of grades.")
#     print("Please select the file containing the grades.")
#     print()

#     # get the file name
#     infileName = askopenfilename()

#     # create empty list to store scores
#     scores = []
#     # open and read file
#     infile = open(infileName, "r")
#     # process each line of the input file
#     for line in infile:
#         # get the score from line by removing newline character
#         score = line[:-1]
#         # store score by appending to scores list
#         scores.append(score)
#     # close file
#     infile.close()

#     # verify list of scores
#     print("Verifying scores")
#     verifyscores = " ".join(scores)
#     print(verifyscores, end='\n')
#     print()
   
#     # create empty list to store score counts
#     scorecounts = []
#     # count the number of occurences of each score and store in a new list
#     for i in range(11):
#         scorecheck = str(i)
#         scorecount = verifyscores.count(scorecheck)
#         scorecounts.append(scorecount)
#     # Question: Why does count() method not work when looping through the list of items
#     # after they are converted from str to int? The scorecounts list ends up empty.

#     # verify list of score counts
#     print("Verifying score counts")
#     strscorecounts = []
#     for intscorecount in scorecounts:
#         strscorecount = str(intscorecount)
#         strscorecounts.append(strscorecount)
#     verifyscorecounts = " ".join(strscorecounts)
#     print("counts", verifyscorecounts, end='\n')
#     print("scores", "0 1 2 3 4 5 6 7 8 9 10", end='\n')
#     print()
    
#     # creates graphics window
#     histogram = GraphWin("Histogram", 400, 200)
#     histogram.setBackground("yellow")
#     # sets coordinates to simplify drawing of images
#     # note that yur is determined by number of scores + 10
#     histogram.setCoords(0, 0, 115, (len(scores) + 10))

#     # use loop to create graphical template for histogram
#     for j in range(11):
#         bar = Rectangle(Point((5 + (10 * j)), 5), Point((10 + (10 * j)), (scorecounts[j] + 5)))
#         bar.setFill("red")
#         bar.setWidth(3)
#         bar.setOutline("blue")
#         bar.draw(histogram)
#         label = Text(Point((7 + (10 * j)), 2), str(j))
#         label.draw(histogram)

#     print("Histogram has been created.")
#     print("Click anywhere on yellow window to close.")
#     histogram.getMouse()
#     histogram.close()

# main()

# #   Note that when a text file created with native mac iOS text editor is used
# #   Scores are verified erroneously:
# ##Verifying scores
# ##{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470 {\fonttbl\f0\fswiss\fcharset0 Helvetica;} {\colortbl;\red255\green255\blue255;} \margl1440\margr1440\vieww10800\viewh8400\viewkind0 \pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0  \f0\fs24 \cf0 1\ 1\ 1\ 1\ 1\ 10\ 10\ 10\ 10\ 10\ 10\ 10\ 10\ 10\ 10\ 10\ 10\ 10\ 10\ 10\ 5\ 5\ 5\ 5\ 5\ 5\ 5\ 5\ 5\ 5
# ##
# ##Verifying score counts
# ##counts 45 28 12 2 15 19 5 5 6 1 16
# ##scores 0 1 2 3 4 5 6 7 8 9 10

# #   This program only works for text files created with IDLE.


                    
# #     6. Maintain


# #this program draws a quiz score histogram
# from graphics import *

# def main():
#     #read file from disk
#     fname = input("Enter filename: ")
#     infile = open(fname, "r")

#     #create 11 items in List as accumulator variable for scores 0-10
#     scores = [0,0,0,0,0,0,0,0,0,0,0]

#     #for counting total students
#     students = 0

#     #loop through each line and use list index as counter for
#     #each scores number
#     for line in infile.readlines():
#         scores[int(line)] = scores[int(line)]+1
#         students = students + 1

#     #draw a bar graph to represent each occurance of possible scores
#     height = max(scores)

#     # 1 Coord = 10px
#     # each score bar height increse 10px too.
#     win = GraphWin('Quiz Histogram', 640, 480)
#     win.setCoords(0, 0, 35, height * 1.5)

#     #show total students
#     students = 'Total Students: '+str(students)

#     totalStudent = Text(Point(8,.1 * height), students)
#     totalStudent.draw(win)

#     pos = 2
#     hgt = .2 * height
#     for i in range(11):
#         bar = Rectangle(Point(pos, hgt),Point(pos + 2, scores[i] + hgt))
#         bar.setFill('red')
#         bar.draw(win)

#         pos = pos+3

#     #bar number 0-10
#     position = 3
#     hgt = .1 * height +  1
#     for i in range(11):
#         Text(Point(position, hgt), i).draw(win)
#         position = position + 3

#     win.getMouse()
#     win.close()

#     infile.close()

# main()
