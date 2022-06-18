# Me Computer, Mandalay.
# June 16, 2022
# exercise_14.py
# This is a word counting program. The program reads the file, counts the lines, 
# words and letter in the file.

# 14. Word Count. A common utility on Unix/Linux systems is a small program called "wc." 
#     This program analyzes a file to determine the number of lines, words and characters 
#     contained therein. Write your own verison of wc. The program should accept a file name
#     as input and then print three numbers showing the count of lines, words, 
#     and characters in the file.


def main():
    print("This program counts the lines, words, and letters in a file")

    # Get the file name
    infileName = input("What file do you to count:  ")

    linecount = 0
    wordcount = 0
    lettercount = 0
    
    with open(infileName, 'r') as infile:
    # process each line of the input file
        for line in infile:
            linecount += 1
            wordcount += len(line.split())
            lettercount += len(line)
    
    # write it to the outfile
    print(f"Lines in the file: {linecount}")
    print(f"Words in the file: {wordcount}")
    print(f"Letters in the file: {lettercount}")

    # close both files
    infile.close()

main()

# def main():
#     fname = input("Enter filename: ")
#     infile = open(fname, "r")
#     data = infile.read()

#     #initialize output list
#     numWords = []
#     letTotal = 0
    
#     #loop for duration of input list split
#     for string in data.split():
#         #create a temporary variable to store the first
#         #letter of each word
#         x = string[0]
#         numWords.append(x)
#         letTotal = len(string) + letTotal
#         wordAvg = letTotal / (len(numWords))
#     infile.close()

#     infile = open(fname, "r")
#     fileLines = infile.readlines()

#     lines = []
#     for line in fileLines:
#         lines.append(line)
#     print("There are {0} lines in the file.".format(len(lines)))

#     #conjoin listed output strings and print
#     print("The avg word length is {0}".format(wordAvg))
#     print("The total number of letters is {0}".format(letTotal))
#     print("The number of words is {0}".format(len(numWords)))

#     infile.close()

# main()
