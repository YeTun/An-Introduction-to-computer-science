# Me Computer, Mandalay.
# June 18, 2020
# exercise_2.py
# This program accepts a quiz score and calculates a correspodning grade

def main():
    print('This program gives letter grades for quiz scores 0-5.')
    quizScore = int(input('Enter a quiz score 0-5: '))

    if quizScore <= 1:
        letterGrade = 'F'
    elif quizScore == 2:
        letterGrade = 'D'
    elif quizScore == 3:
        letterGrade = 'C'
    elif quizScore == 4:
        letterGrade = 'B'
    else:
        letterGrade = 'A'
    
    print(f'The score of {quizScore} is a letter grade of {letterGrade}.')

if __name__ == '__main__':
    main()


# #Grade list
# grades=["F","F","D","C","B","A"]

# # defining grade functions
# def printGrade(num):
#     print("Your letter grade is a", grades[num])

# #defining main function
# def main():
#     print("This program takes a grade 0 - 5 and converts it into a letter grade")

#     # converts number grade to letter grade
#     try:
#         numGrade = int(input("What is the number grade? "))
#         if numGrade < 6 and numGrade >= 0:
#             printGrade(numGrade)
#         else:
#             print("That number is out of range")
#     # custome error message
#     except:
#         print("Something went wrong")

# # Calling program
# if __name__ == '__main__':
#     main()
