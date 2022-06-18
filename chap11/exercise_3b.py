#A program to sort student information into GPA order

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

def sortData(data, sort, order):
    if order == 'ASCENDING':
        if sort == 'GPA':
            return data.sort(key=Student.gpa)
        elif sort == 'NAME':
            return data.sort(key=Student.getName)
        elif sort == 'CREDITS':
            return data.sort(key=Student.getHours)
    else:
        if sort == 'GPA':
            return data.sort(key=Student.gpa).reverse()
        elif sort == 'NAME':
            return data.sort(key=Student.getName).reverse()
        elif sort == 'CREDITS':
            return data.sort(key=Student.getHours).reverse()

def getOrder():
    validData = False
    while validData == False:
        try:
            order = input("Sort in ascending or descending order: ")
            order = order.upper()
            if order == "ASCENDING" or order == "DESCENDING":
                validData = True
            else: 
                print("Type ascending or descending")
        except ValueError:
            print("Please enter an appropriate value")
    return order

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
    order = getOrder()
    return filename, sort, order

def main():
    print("This program sorts student grade information by GPA")
    filename, sort, order = inputs()
    data = readStudents(filename)
    sortedData = sortData(data, sort, order)
    filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been written to", filename)

if __name__ == '__main__': main()