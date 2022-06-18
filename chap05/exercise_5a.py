# Me Computer, Mandalay.
# June 16, 2022
# exercise_5.py
# converts a single sequence of letters into the alphabetical placement

#  5. Numerologists claim to be able to determine a person's character traits 
#     based on the "numeric value" of a name. The value of a name is determined 
#     by summing up the values of the letters of the name where "a" is 1, 
#     "b" is 2, "c" is 3, up to "z" being 26. For example, the name "Zelle" 
#     would have the value 26 + 5 + 12 + 12 + 5 = 60 (which happens to be a very
#     auspicious number, by the way). Write a program that calculates the numeric value of 
#     a single name provided as input.
#
#  input: a last name defined as a string supplied by the user
#  output: a numeric value defined as an int that is the sum of values assigned to the individual strings
#  User inputs a string, and the program outputs the sum of the values of the invidual strings where the values are
#  determined as follows, a = 1, b = 2, etc.

#  Create a sequence of characters as lookup table starting with an empty space at index 0 to align index with value of each letter
#  User supplies string as input
#  For each character in the input string, return where it occurs in the string, and add its index value to an accumulating sum
#  Print sum

def main():
    # print into
    print("This program calculcates the numeric value of a name.")
    
    # prompt for name
    name = str(input("Enter a single name: "))
    
    # loop through characters and sum
    total = 0
    for ch in name.lower():
        total += ord(ch.lower()) - ord('a') + 1
    
    # print final result
    print(f"The sum of the name '{name}' is equal to: {total}")

main()


# def main():
#     # Get name from user and store as a string
#     name = input("What is your name? \n")

#     # Convert to all lower
#     name = name.lower()

#     # Convert to numbers, subtract 96 from each, and accumulate
#     x = 0
#     for ch in name:
#         ch = ord(ch)
#         if ch != 32:
#             x += ch - 96

#     print(f"The numeric value of your name is {x}.")

# main()

# def main():
#     lookup = "0abcdefghijklmnopqrstuvwxyz"
#     inputname = input("Please use letters only to enter your name.\n")

#     formatinputname = inputname.lower()
#     length = len(formatinputname)
#     wordvalue = 0
#     for i in range(length):
#         letter = formatinputname[i]
#         lettervalue = lookup.find(letter)
#         wordvalue += lettervalue
    
#     print("The numeric value of {0} is {1}.".format(inputname, wordvalue))
    
# main()



