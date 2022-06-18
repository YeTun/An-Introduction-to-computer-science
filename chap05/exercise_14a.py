# Me Computer, Mandalay.
# June 16, 2022
# exercise_14.py
# This is a word counting program. The program reads the file, counts the lines, 
# words and letter in the file.
# open: exercise_14.txt/sentences.txt

# 14. Word Count. A common utility on Unix/Linux systems is a small program called "wc." 
#     This program analyzes a file to determine the number of lines, words and characters 
#     contained therein. Write your own verison of wc. The program should accept a file name
#     as input and then print three numbers showing the count of lines, words, 
#     and characters in the file.


def main():
    print("File wordcount")
    print()

    fname = input("Enter filename: ")
    infile = open(fname, 'r')
    chars = infile.read()
    infile.close()
    
    words = chars.split()
    lines = chars.split("\n")

    print("Characters:", len(chars))
    print("Words:", len(words))
    print("Lines:", len(lines))

main()
