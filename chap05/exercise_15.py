# Me Computer, Mandalay.
# June 16, 2022
# exercise_15.py
# This program plots student exam scores on a horizontal bar chart
#    open student_test.txt, studentExamScores.txt

# open student_test.txt/studentExamScores.txt
# 15. Write a program to plot a horizontal bar chart of student exam scores. Your program should get input from a file. The first line
#     of the file contains the count of the number of students in the file, and each subsequent line contains a student's last name
#     followed by a score in the range 0-100. Your program should draw a horizontal rectangle for each student where the length of the
#     bar represents the student's score. The bars should all line up on their left-hand edges.
#
#     Hint: Use the number of students to determine the size of the window and its coordinates. [Note to self: point of control.]
#     Bonus: label the bars at the left with the students' names.


from graphics import *
from tkinter.filedialog import askopenfilename

def main():
    # get filenames
    infileName = askopenfilename()

    # open the files & create objects
    infile = open(infileName, "r")

    # enter n to determine window size
    nStudents = int(infile.readline())

    # Create a graphics window
    win = GraphWin("Student Exam Scores", 800, 700)
    win.setBackground("white")
    maxY = 100*nStudents
    win.setCoords(-1, -1, 120, maxY)

    # draw student names
    posY = 0
    increment = maxY / nStudents
    for i in range(nStudents):
        line = infile.readline()
        content = line.split()
        name = content[0]
        score = int(content[1])
        Text(Point(10, posY+increment/2), name).draw(win)
        scoreGraph = Rectangle(Point(15, posY), Point(score+15, posY+increment))
        scoreGraph.draw(win)
        posY += increment

    # End Program
    endText = Text(Point(50, maxY/2), "Click again to quit.")
    endText.setTextColor("red")
    endText.draw(win)
    win.getMouse()
    win.close()

    # Close file
    infile.close()

main()


# from graphics import *

# def main():
#     fname = input("Enter filename: ")
#     infile = open(fname, "r")

#     # grab number of students and assign to numStud
#     numStud = int(infile.readline())
    
#     # grab name and grade and assign to lists studName and grade
#     studName = []
#     grade = []
#     lines = []
#     for line in infile.readlines():
#         x, y = line.split(": ")
#         # strip \n
#         y = y[0:-1]
#         studName.append(x)
#         grade.append(y)

#     print(studName)
#     print(grade)
    
#     # initialize graphWin of size 400, (100 x numStud)
#     win = GraphWin("Student Grade Chart", 400, 50 * numStud)

#     # setCoords: -10, 0, 100, (10 x (numStud + 2))
#     win.setCoords(-30, (10 * numStud + 2), 120, 0)

#     # draw text studName
#     for i in range (numStud):
#         s = studName[i].rjust(10)
#         Text(Point(-20, 15 + numStud * .8 * i), s).draw(win)
#     # draw Rectangle and clone
#     for i in range (numStud):
#         r = Rectangle(Point(0, 13 + numStud * .8 *i), Point(grade[i], 17 + numStud * .8 * i))
#         r.draw(win)

#     input("Preess Enger to quit.")
#     # close file
#     infile.close()

# main()
