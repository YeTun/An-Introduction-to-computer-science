# Me Computer, Mandalay.
# June 22, 2022
# exercise_11.py
# censorship program

def writeFile(infile, outfile):
    for line in infile:
        words = line.split(' ')
        for word in words:
            if len(word) == 4:
                index = words.index(word)
                words.pop(index)
                words.insert(index, "****")
        censored = " ".join(words)
        print(censored, file=outfile)    
    print(f"Censored file has been saved at {outfile.name}")

def getFile():
    try:
        inFileName = input("Enter the name of a file you would like to open: ")
    except ValueError:
        "Please enter a valid filename"
    
    try:
        outFileName = input("Enter the name of a file you would like to write: ")
    except ValueError:
        "Please enter a valid filename"
    
    infile = open(inFileName, 'r')
    outfile = open(outFileName, 'w')
    return infile, outfile

def intro():
    print("This program finds four letter words from a file")
    print("and censors them with **** and then outputs them")
    print("to another file.")

def main():
    intro()
    infile, outfile = getFile()
    writeFile(infile, outfile)

main()

