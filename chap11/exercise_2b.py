# Me Computer, Mandalay.
# June 22, 2020
# exercise_2.py
# A program to sort student information into GPA order

from gpa import Student, makeStudent

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQPoints()), file=outfile)
    outfile.close()

def sortData(data, sort):
    if sort == 'GPA':
        return data.sort(key=Student.gpa)
    elif sort == 'NAME':
        return data.sort(key=Student.getName)
    elif sort == 'CREDITS':
        return data.sort(key=Student.getHours)

def getSort():
    validData = False
    while validData == False:
        try:
            sort = input("What would you like to sort the data by? (GPA, name, or credits: ")
            sort = sort.upper()
            if sort == 'GPA' or sort == "NAME" or sort == "CREDITS":
                validData = True
            else:
                print("Please enter gpa, name, or credits")
        except ValueError:
            print("Please enter an appropriate value")
    return sort

def getFile():
    validFile = False
    while validFile == False:
        try:
            filename = input("Enter the name of the data file: ")
            if filename != '':
                validFile = True
            else:
                print("Please enter a filename")
        except ValueError:
            print("Please enter an approriate value")
    return filename

def inputs():
    filename = getFile()
    sort = getSort()
    return filename, sort

def main():
    print("This program sorts student grade information by GPA")
    filename, sort = inputs()
    data = readStudents(filename)
    sortedData = sortData(data, sort)
    filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been written to", filename)

if __name__ == '__main__': main()