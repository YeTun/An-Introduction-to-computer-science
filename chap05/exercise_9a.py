# Me Computer, Mandalay.
# June 16, 2022
# exercise_9.py
# this program counts the number of words in a sentence

#  9. Write a program that counts the number of words in a sentence entered by the user.
#
#  Given a sentence, the program will count the number of words.
#  input = a sentence defined as a string
#  output = the number of words defined as an int
#
#  Prompt user for input.
#  Use split method to split string into list of words.
#  Print length of list.

def main():
    # intro
    print("This program counts the nuber of words in a sentence.")
    
    # prompt for phrase
    sentence = str(input("Enter a sentence: "))
    
    # split phrase and count words
    wordCount = 0
    for word in sentence.split():
        wordCount += 1
    
    # print out the wordCount
    print("There are {0} words in the sentence".format(wordCount))

main()


# def main():
#     print("This program counts the number of words in a sentence")
#     sentence = input("Enter your sentence: ")

#     count = len(sentence.split())

#     print(f"There are {count} words.")

# main()

# def main():
#     sentence = input("Please enter your sentence here: ")
#     sentence_in_towords = sentence.split()
#     number_of_words = len(sentence_in_towords)
    
#     print("The number of words in", end = "\n")
#     print(sentence, end = "\n")
#     print("is", end = "\n")
#     print(str(number_of_words) + ".")

# main()
