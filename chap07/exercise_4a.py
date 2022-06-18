# Me Computer, Mandalay.
# June 18, 2020
# exercise_4.py
# This program calculates the class standing from number of credits earned

def main():
    print("This program classifies students based on the number of credits earned.")
    credits = int(input("Enter the number of credits earned: [0-100] "))

    if credits < 7:
        year = "Freshman"
    elif credits < 16:
        year = "Sophomore"
    elif credits < 26:
        year = "Junior"
    else:
        year = "Senior"
   
    print(f"{credits} credits is a {year} student.")

main()

# def main():
#     print("This program takes number of credits earned by a student and returns their standing")

#     # converts number grade to letter grade
#     try:
#         credits = int(input("How many credits were earned? "))
#         if credits < 7 and credits >= 0:
#             print("The student is a Freshman")
#         elif credits >= 7 and credits < 16:
#             print("The student is a Sophomore")
#         elif credits >= 16 and credits < 26:
#             print("The student is a Junior")
#         elif credits >= 26:
#             print("The student is a Senior")
#         else:
#             print("That number is out of range")
    
#     # custome error message
#     except TypeError:
#         print("\nYour inputs were not all numbers")
#     except:
#         print("Something went wrong")

# # Calling program
# if __name__ == '__main__':
#     main()
