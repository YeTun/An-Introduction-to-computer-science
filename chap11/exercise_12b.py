def getWordLength(word):
    word_length = len(word)
    censored_word = "*" * word_length
    return censored_word

def writeFile(infile, censoredWords, outfile):
    cwords = []
    for cline in censoredWords:
        cwords.append(str(cline.strip()))
    for line in infile:
        words = line.split(' ')
        for word in words:
            if word in cwords:
                censored_word = getWordLength(word)
                index = words.index(word)
                words.pop(index)
                words.insert(index, censored_word)
        censored = " ".join(words)
        print(censored, file=outfile)    
    # print("Censored file has been saved at", filename)

def getFile():
    try:
        inFileName = input("Enter the name of a file you would like to censor: ")
    except ValueError:
        "Please enter a valid filename"
    try:
        inFileNameCensored = input("Enter the name of a file you would that has the words to censor: ")
    except ValueError:
        "Please enter a valid filename"
    try:
        outFileName = input("Enter the name of a file you would like to open: ")
    except ValueError:
        "Please enter a valid filename"
    infile = open(inFileName, 'r')
    censoredWords = open(inFileNameCensored, 'r')
    outfile = open(outFileName, 'w')
    return infile, censoredWords, outfile

def intro():
    print("This program allows users to upload a censored words")
    print("file and then censors them with the correct number")
    print("of **** and then outputs them")
    print("to another file.")

def main():
    intro()
    infile, censoredWords, outfile = getFile()
    writeFile(infile, censoredWords, outfile)

main()