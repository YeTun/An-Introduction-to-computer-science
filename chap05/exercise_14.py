# Me Computer, Mandalay.
# June 16, 2022
# exercise_14.py
# Program to count lines, words and characters in a file.
#    fname = exercise_14.txt


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
