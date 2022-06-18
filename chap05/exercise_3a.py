# Me Computer, Mandalay.
# June 16, 2022
# exercise_3.py
# Ptogram take a 100 point score and converts it into a grade

#  3. A certain CS professor gives 100-point exams that are graded on the scale
#     90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F. Write a program that accepts 
#     an exam score as input and prints out the corresponding grade.
#
#     Input: an exam score defined as an int from 0 t0 100
#     Output: a letter grade defined as one of 5 possible strings: A, B, C, D, F where 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F
#
#     Define int ranges for each letter grade
#     For a number  grade entered by user, use if elif statements to determine letter grade
#
#     Note: Another possible solution, but much less efficient, would be to create a sequence as a string or list where each
#     list grade would be a list item indexed at its coresponding value, so in the indeces from 90 to 100, there would be an "A"
#
#     Since I don't feel like typing a lot, I will use the more efficient solution even if decision structures have not been
#     covered yet.
#
#     Then again, I will stick with the book's plan and write up the less efficient version.
#

def main():
    # print scale
    print("This program converts a test score (0-100) to the corresponding letter grade.")

    # ask for input
    score = int(input("Enter a test score 0 - 100: "))

    # convert // lookup letter
    grades = ["F", "F", "F", "F", "F", "F", "D", "C", "B", "A", "A"]
    
    # print result
    print(f"The score: {score} equals the letter grade of {grades[score // 10]}.")

main()


# def main():
#     lettergradescale = "F" * 60 + "D" * 10 + "C" * 10 + "B" * 10 + "A" * 11
#     examgrade = int(input("Please enter the quiz grade on a scale from 0 to 100: "))

#     lettergrade = lettergradescale[examgrade]
  
#     print("Your grade of {0} corresponds to the letter grade of {1}.".format(examgrade, lettergrade))

# main()

