# Me Computer, Mandalay.
# June 16, 2022
# exercise_6.py
# A program that determines the numeric value of a name where a = 1, b = 2, etc.

#  6. Expand your soluation to the previous problem to allow the calcualtion of 
#     a complete name such as "John Marvin Zelle" or "John Jacob Jingleheimer Smith." 
#     The total value is just the sum of the numberic values of all the names.
#
#  Algorithm same as above, but need to use split method to make a list, then loop through each list element with above
#  process for determining numeric value
# numerology.py

def main():
    # print into
    print("This program calculcates the numeric value of a name.")
    
    # prompt for name
    name = str(input("Enter a name: "))
    
    words = name.split()
    # loop through names
    total = 0
    for word in words:
        for ch in word.lower():
            total += ord(ch) - ord('a') + 1
    
    # print final result
    print("The sum of the name '{0}' is equal: {1}".format(name, total))

main()


# def main():
#     # Get name from user and store as a string
#     name = input("What is your name? \n")

#     # Convert to all lower, and account for user input
#     fullName = "".join(name.lower().split()).replace(".", "")

#     # Convert to numbers, subtract 96 from each, and accumulate
#     x = 0
#     for ch in fullName:
#         x += int(ord(ch)) - 96

#     print(f"The numeric value of your name is {x}.")

# main()

# def main():
#     lookup = "0abcdefghijklmnopqrstuvwxyz"
#     inputnames = input("Please use letters only to enter your name.\n")

#     name = ''.join(inputnames.lower().split())
#     length = len(name)
#     totalvalue = 0
#     for i in range(length):
#         letter = name[i]
#         lettervalue = lookup.find(letter)
#         totalvalue += lettervalue
    
#     print("The numeric value of {0} is {1}.".format(inputnames, totalvalue))

# main()


