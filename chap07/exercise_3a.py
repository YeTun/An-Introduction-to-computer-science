# Me Computer, Mandalay.
# June 18, 2020
# exercise_3.py
# This program accepts a quiz score and calculates a correspodning grade

def main():
    print('This program gives letter grades for quiz scores 0-5.')
    examScore = int(input('Enter a quiz score 0-100: '))

    if examScore < 60:
        letterGrade = 'F'
    elif examScore < 70:
        letterGrade = 'D'
    elif examScore < 80:
        letterGrade = 'C'
    elif examScore < 90:
        letterGrade = 'B'
    else:
        letterGrade = 'A'
    
    print(f'The score of {examScore} is a letter grade of {letterGrade}.')

if __name__ == "__main__":
    main()


# # Grade list
# grades=["F","D","C","B","A"]

# # defining grade functions
# def printGrade(num):
#     print("Your letter grade is a",grades[num])

# def main():
#     print("This program takes a 100-point grade and converts it into a letter grade")

#     # converts number grade to letter grade
#     try:
#         numGrade = int(input("What is the number grade? "))
#         if numGrade < 60 and numGrade >= 0:
#             printGrade(0)
#         elif numGrade >=60 and numGrade < 70:
#             printGrade(1)
#         elif numGrade >=70 and numGrade < 80:
#             printGrade(2)
#         elif numGrade >=80 and numGrade < 90:
#             printGrade(3)
#         elif numGrade >=90 and numGrade <= 100:
#             printGrade(4)
#         else:
#             print("That number is out of range")
#     # custome error message
#     except:
#         print("Something went wrong")

# # Calling program
# if __name__ == '__main__':
#     main()
