# Me Computer, Mandalay.
# June 21, 2022
# exercise_6.py

class Student:
    
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def addGrade(self, gradePoint, credits):
        self.hours = self.hours + credits
        self.qpoints = self.qpoints + (gradePoint * credits)

    def gpa(self):
        return self.qpoints / self.hours

def convertGrades(grade):
    gradePoint = 0.0
    if grade == 'A':
        gradePoint = 4.0
    elif grade == 'B':
        gradePoint = 3.0
    elif grade == 'C':
        gradePoint = 2.0
    elif grade == 'D':
        gradePoint = 1.0
    else:
        gradePoint = 0.0
    return float(gradePoint)

def getGrade():
    validData = False
    while validData == False:
        try:
            grade = input("Please enter a letter grade for your class: ")
            if grade.upper() == 'A' or grade.upper() == 'B' or grade.upper() == 'C' or grade.upper() == 'D' or grade.upper() == 'F':
                validData = True
            else:
                validData = False
                print("Please enter a letter grade A-F")
        except TypeError:
            print("Please enter a letter")
    return grade.upper()

def getCredits():
    validData = False
    while validData == False:
        try:
            credits = float(input("Please enter the number of credits for your class: "))
            if credits >= 0:
                validData = True
            else:
                validData = False
        except ValueError:
            print("Please enter a floating number")
    return credits

def addGrades():
    grade = getGrade()
    credits = getCredits()
    return grade, credits

def getName():
    validName = False
    while validName == False:
        try:
            name = input("Please enter your name: ")
            validName = True
        except ValueError:
            print("Please enter a valid name")
    return name

def makeStudent():
    name = getName()
    hours = 0
    qpoints = 0
    return Student(name, hours, qpoints)

def main():
    student = makeStudent()
    grade, credits = addGrades()
    gradePoint = convertGrades(grade)
    student.addGrade(gradePoint, credits)
    exitProgram = False
    while exitProgram == False:
        leave = input("Would you like to enter another grade (yes or no): ")
        if leave == 'no':
            exitProgram = True
            break
        grade, credits = addGrades()
        gradePoint = convertGrades(grade)
        student.addGrade(gradePoint, credits)


    print("Student: ", student.getName())
    print("hours: ", student.getHours())
    print("GPA: {0:0.1f}".format(student.gpa()))

if __name__ == '__main__':  main()