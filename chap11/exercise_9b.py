#A program to sort student information into GPA order

from gpa import Student, makeStudent

def sorter(gpaStudents):
    return gpaStudents[0]

def gpaSort(students):
    gpaStudents = []
    for student in students:
        tuple = (student.gpa(), student.getName(), student.getQPoints())
        gpaStudents.append(tuple)
    return gpaStudents

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    students.sort(key=sorter, reverse=True)
    for s in students:
        print("{0}\t{1}\t{2}".format(s[0], s[1], s[2]), file=outfile)
    outfile.close()

def main():
    print("This program sorts student grade information by GPA")
    filename = input("Enter the name of the data file: ")
    students = readStudents(filename)
    # print(students)
    gpaStudents = gpaSort(students)

    filename = input("Enter a name for the output file: ")
    writeStudents(gpaStudents, filename)
    print("The data has been written to", filename)

if __name__ == '__main__': main()