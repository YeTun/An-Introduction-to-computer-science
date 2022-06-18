# Me Computer, Mandalay.
# June 17, 2022
# exercise_10.py
# Program take takes in a phrase and output an acronym in uppercase letters.

def acronym(phrase):
    # split string
    words = phrase.split()
    # transverse list: get 1st letter and uppercase
    acronym = ""
    for word in words:
        acronym += word.upper()[0]
    return acronym

def main():
    # intro
    print("This program creates an acronym using the 1st letters of each word entered.")
    
    # get phrase
    phrase = str(input("Type in a phrase and hit <Enter>: "))

    # print acronym
    print("The acronym for '{0}' is '{1}'.".format(phrase, acronym(phrase)))

main()

# def acronym(phrase):
#     # create acronym List
#     letters = []
#     # Loops through phrase and splits into one word pieces.
#     for word in phrase.split(" "):
#         firstLetter = str(word[0].upper())
#         letters.append(firstLetter)

#     acronym = "".join(letters)
#     return acronym

# def main():
#     print("This program takes in a phrase and outputs a acronym in upper case letters")

#     phrase = input("Enter your phrase: ")

#     print(f"The phrase '{phrase.title()}' is summerized to '{acronym(phrase)}'.")

# main()


# def acronym(phrase):
#     words = []
#     #loop for duration of input list split
#     for string in phrase.split():
#         #create a temporary variable to store the first letter of each word in upper case
#         x = string[0].upper()
#         words.append(x)

#     #conjoin listed output strings and print
#     acro = "".join(words)
#     return acro

# def main():
#     phrase = input("What would you like acronymized? \n")

#     x = acronym(phrase)

#     print(x)

# main()
