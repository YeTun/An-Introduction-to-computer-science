# Me Computer, Mandalay.
# June 16, 2022
# exercise_10.py
# this program calculates the average word length in a sentence

# 10. Write a program that calculates the average word length in a sentence 
#     entered by the user. 
#     Same as above, but also count lenght of each words, add up all the numbers, 
#     divide by number of words.

def main():
    # print intro
    print("This program calculates the average word length in a sentence.")
    
    # prompt for sentence
    sentence = str(input("Enter a sentence: "))
    
    # split phrase
    wordList = sentence.split()
    # loop words for total characters
    totalChars = 0
    for word in wordList:
        totalChars += len(word)
    
    # calculate total characters / number of words
    averageChars = totalChars / len(wordList)
    
    # print result
    print("The average length of words in the sentence:", sentence,
          "\nis {0:0.1f} characters".format(averageChars))

main()

# def main():
#     print("This program calculates the average word length in a sentence")
#     sentence = input("Enter your sentence: ")
    
#     words = sentence.split()
#     count = len(words)
#     sumWords = 0
#     for word in words:
#         wordLength = len(word)
#         sumWords += wordLength
    
#     average = sumWords/count
    
#     print(f"The average length of words is {average} letters.")

# main()

# def main():
#     sentence = input("Please enter your sentence here: ")
#     sentenceIntoWords = sentence.split()
#     n = len(sentenceIntoWords)
    
#     wordLengthTotal = 0
#     for word in sentenceIntoWords:
#         wordLength = len(word)
#         wordLengthTotal += wordLength
    
#     averageWordLength = wordLengthTotal / n

#     print("The average word length in the sentence", end = "\n")
#     print(sentence, end = "\n")
#     print("is ", end = "")
#     print(str(averageWordLength) + ".")

# main()
