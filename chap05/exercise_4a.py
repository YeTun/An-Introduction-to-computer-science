# Me Computer, Mandalay.
# June 16, 2022
# exercise_4.py
# Program takes in a phrase and output an acronym in uppercase letters.

#  4. An acronym is a word formed by taking the first letters of the words in a 
#     phrase and making a word from them. For example, RAM is an acronym 
#     for "random access memory." Write a program that allows the user to type
#     in a phrase and then outputs the acronym for that phrase. Note: The acronym 
#     should be all uppercase, even if the words in the phrase are not capitalized.
#
#     Input: A string of words demarcated by spaces
#     Output: A string that is an acronym of the first letter of each word in the string
#
#     Get input from user as a string
#     Use split method to split string into its component words as demarcated by a space (" ")
#     Get first letter of each word using loop accumulator
#     Join first letter of each word into a new string
#     Capitalize new string
#     Print string for user
#

def main():
    # intro
    print("This program creates an acronym using the 1st letters of each word entered.")
    
    # get phrase
    phrase = str(input("Type in a phrase and hit <Enter>: "))
    
    # split string
    words = phrase.split()
    # transverse list: get 1st letter and uppercase
    acronym = ""
    for word in words:
        acronym += word.upper()[0]
    
    # print acronym
    print("The acronym for:", phrase, "is:", acronym + ".")

main()

# def main():
#     print("This program takes in a phrase and outputs a acronym in upper case letters")

#     phrase = input("Enter your phrase: ")
    
#     # creat acronym List
#     letters = []    
#     # Loops through phrase and splits into one word pieces.
#     for word in phrase.split(" "):
#         firstLetter = str(word[0].upper())
#         letters.append(firstLetter)

#     acronym = "".join(letters)
    
#     print(f"The phrase '{phrase.title()}' is summerized to '{acronym}'.")

# main()

# def main():
#     userstring = input("Please enter the words, separated by a space, that will be used for the acronym: ")

#     words = userstring.title().split()
    
#     newacronym = ""
#     for i in range(len(words)):
#         word = words[i]
#         firstletter = word[0]
#         newacronym += firstletter
    
#     print("The acronym is {0}".format(newacronym))

# main()