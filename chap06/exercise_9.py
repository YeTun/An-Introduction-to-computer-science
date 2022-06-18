# Me Computer, Mandalay.
# June 17, 2022
# exercise_9.py
# Ptogram take a 100 point score and converts it into a grade

def grade(score):
    return "FFDCBA"[score]

def main():
    print("Quiz Grader")
    score = int(input("Enter the score (0-5): "))
    print("The grade is", grade(score))

main()