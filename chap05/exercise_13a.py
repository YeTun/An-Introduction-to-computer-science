# Me Computer, Mandalay.
# June 16, 2022
# exercise_13.py
# Calculates the average length of words in sentences

# 13. Redo any of the previous programming exercises to make them batch-oriented 
#     (using text files for input and output).

from tkinter.filedialog import askopenfilename, asksaveasfilename

def main():
    print("This program creates a file of average word length in sentences.")

    # get filenames
    infileName = askopenfilename()
    outfileName = asksaveasfilename()

    # open the files & create objects
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # process each line of the input file
    for line in infile:
        wordList = line.split()
        # loop words for total characters
        totalChars = 0
        for word in wordList:
            totalChars += len(word)
        # calculate total characters / number of words
        averageChars = totalChars / len(wordList)
        # print result
        print("The average length of words in the sentence:", "'"+line+"'",
              "is {0:0.1f} characters".format(averageChars)+".", file=outfile)

    # close both files
    infile.close()
    outfile.close()

main()

# def main():
#     fname = input("Enter filename: ")
#     infile = open(fname, "r")
#     data = infile.read()

#     #initialize output list
#     numWords = []

#     #loop for duration of input list split
#     for string in data.split():
#         #create a temporary variable to store the first
#         #letter of each word
#         x = string[0]
#         numWords.append(x)

#     letTotal = 0
#     for string in data.split():
#         letTotal = len(string) + letTotal
#         wordAvg = letTotal / (len(numWords))
    
#     #conjoin listed output strings and print
#     print("The Avg word lenth is {0}".format(wordAvg))
#     print("The total number of letters is {0}".format(letTotal))
#     print("The number of words is {0}".format(len(numWords)))

# main()
