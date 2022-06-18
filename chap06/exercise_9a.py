# Me Computer, Mandalay.
# June 17, 2022
# exercise_9.py
# Ptogram take a 100 point score and converts it into a grade

def grade(score):
    # convert // lookup letter
    grades = ["F", "F", "F", "F", "F", "F", "D", "C", "B", "A", "A"]
    return grades[score // 10]

def main():
    # print scale
    print("This program converts a test score (0-100) to the corresponding letter grade.")

    # ask for input
    score = int(input("Enter a test score 0 - 100: "))

    # print result
    print(f"The score {score:0.0f} equals the letter grade of {grade(score)}.")

main()

# def grade(score):
#     grades = []
    
#     for x in range(0, 60):
#         grades.append("F")

#     for x in range(60, 70):
#         grades.append("D")

#     for x in range(70, 80):
#         grades.append("C")

#     for x in range(80, 90):
#         grades.append("B")

#     for x in range(90, 101):
#         grades.append("A")

#     return grades[score]

# def main():
#     print("This program takes a 100 point score and converts it into a Letter Grade.")
#     n = (eval(input("Enter a number grade (0 - 100): ")))

#     x = grade(n)

#     print(f"Your grade is {x}.")

# main()
