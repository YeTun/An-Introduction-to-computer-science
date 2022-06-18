# Me Computer, Mandalay.
# June 21, 2022
# exercise_5.py

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

def getGradePoint():
    validData = False
    while validData == False:
        try:
            gradePoint = float(input("Please enter a grade point for your class (0-4): "))
            if gradePoint >= 0 and gradePoint <= 4:
                validData = True
            else:
                validData = False
        except ValueError:
            print("Please enter a floating number")
    return gradePoint

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
    gradePoint = getGradePoint()
    credits = getCredits()
    return gradePoint, credits

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
    gradePoint, credits = addGrades()
    
    exitProgram = False
    while exitProgram == False:
        student.addGrade(gradePoint, credits)
        leave = input("Would you like to enter another grade (yes or no): ")
        if leave == 'no':
            exitProgram = True
            break
        gradePoint, credits = addGrades()


    print("Student: ", student.getName())
    print("hours: ", student.getHours())
    print("GPA: {0:0.1f}".format(student.gpa()))

if __name__ == '__main__': main()
