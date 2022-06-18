# Me Computer, Mandalay.
# June 17, 2022
# exercise_14.py
# This program will print the sum of squared numbers read from a file (exercise_14.txt).

from tkinter.filedialog import askopenfilename, asksaveasfilename

def squareEach(nums):
    # nums is a list of numbers, function modifies the list by squaring each
    for i in range(len(nums)):
        nums[i] = float(nums[i]) ** 2

def sumList(nums):
    # nums is a list of numbers, function returns the sum of the list
    tot = 0
    for i in range(len(nums)):
        tot += float(nums[i])
    return tot

def main():
    # get filenames
    infileName = askopenfilename()

    # open the files & create objects
    infile = open(infileName, "r")

    # create list from text file
    dataList = []
    for line in infile:
        dataList.append(line[:-1])

    # square items
    squareEach(dataList)

    # print result
    print(sumList(dataList))
    
    infile.close()

main()

# def toNumbers(nums):
#     for i in range(len(nums)):
#         nums[i] = int(nums[i])

# def squareEach(nums):
#     for i in range(len(nums)):
#         nums[i] = nums[i]**2

# def sumList(nums):
#     return sum(nums)

# def main():
#     # Get the file name
#     infileName = input("What file are the names in? ")
#     infile = open(infileName,"r")
#     for line in infile:
#         numList = line.split()
#         toNumbers(numList)
#         squareEach(numList)
#     print(sumList(numList))

# main()


# def toNumbers(strList):
#     for x in range (len(strList)):
#         strList[x] = int(strList[x])
#     return(strList)

# def squareEach(nums):
#     for x in range (len(nums)):
#         nums[x] = nums[x] ** 2
#     return(nums)

# def sumList(nums):
#     y = 0
#     for x in range (len(nums)):
#         y = nums[x] + y
#     return(y)

# def main():
#     fname = input("Enter filename: ")
#     infile = open(fname, "r")

#     lines = []
#     for line in infile.readlines():
#         lines.append(line)

#     x = toNumbers(lines)
#     y = squareEach(x)
#     z = sumList(y)
#     print(z)

#     infile.close()
# main()
