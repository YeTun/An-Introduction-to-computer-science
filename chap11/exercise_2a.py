# Me Computer, Mandalay.
# June 22, 2022
# exercise_2.py
# A program to sort student information into GPA order

from gpa import Student

def makeStudent(infoStr):
    # inforStr is a tap-separated line: name hours getQPoints
    # returns a corresponding Student object
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    # students is a list of Student object
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQPoints()), file = outfile)
    outfile.close()

def main():
    print("This program sorts student grade information by GPA, name, or credits.")
    # filename = input("Enter the name of the data file: ")
    filename = 'exercise_2.txt'
    data = readStudents(filename)
    
    while True:
        x = (input('Type "GPA", "name", or "credits" >>>  '))
        if x == 'g' or x == 'GPA':
            data.sort(key=Student.gpa)
            s = "_(GPA)"
            break
        elif x == 'n' or x == 'name': 
            data.sort(key=Student.getName)
            s = "_(name)"
            break 
        elif x == 'c' or x == 'credits':
            data.sort(key=Student.getQPoints)
            s = "_(credits)"
            break
        else:
            print("Please try again.")
    
    # filename = input("enter a name for the outputfile: ")
    filename = "exercise_2" + s + ".txt"
    writeStudents(data, filename)
    print("The data has been written to", filename)

if __name__ == '__main__': main()



