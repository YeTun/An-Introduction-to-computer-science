# Me Computer, Mandalay.
# June 16, 2022
# exercise_2.py
# Ptogram take a 5 point score and converts it into a grade
'''
2. A certain CS professor gives 5-point quizzes that are graded on the scale
   5-A, 4-B, 3-C, 2-D, 1-F, 0-F. Write a program that accepts a quiz score as
   an input and prints out the corresponding grade.

     Input: quiz score defined as a a number from 1 to 5
     Output: a letter grade defined as a string: A, B, C, D, F

     Create a squence of grades as a string, where index/position corresponds to letter grade 
     For a number supplied by user, convert to int and get the index, print the appropriate grade
'''

def main():
    # print scale
    print("This program converts a quiz score (0-5) to the corresponding letter grade.")

    # ask for input
    score = int(input("Enter a quiz score 0 - 5: "))

    # convert // lookup letter
    grades = ["F", "F", "D", "C", "B", "A"]
    
    # print result
    print(f"The score {score} equals the letter grade of {grades[score]}.")

main()


# def main():

#     # Create list of possible letter grades
#     lettergradescale = "FFDCBA"
    
#     # Prompt user for quiz grade
#     quizgrade = int(input("Please enter the quiz grade on a scale from 0 to 5: "))
    
#     lettergrade = lettergradescale[quizgrade]
    
#     print("Your quiz grade of {0} corrsesponds to the letter grade of {1}.".format(quizgrade, lettergrade))

# main()
