# Me Computer, Mandalay.
# June 16, 2022
# exercise_2.py
# Quiz grader

def main():
    print("Five point quiz grader")
    score = int(input("Enter the score: "))
    grade = "FFDCBA"[score]
    print("The grade is", grade)

main()