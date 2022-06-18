# Me Computer, Mandalay.
# June 18, 2020
# exercise_5.py
# This program caluclates a person's BMI

def main():
    print("This program calculates your BMI and checks if it falls in, below, or above the healthy range.")
    weight = float(input("Enter your weight in lbs: "))
    feet = float(input("Enter how many whole feet tall you are: "))
    inches = float(input("Enter how many inches (partial feet) tall you are: "))

    bmi = weight * 720 / ((feet * 12 + inches) ** 2)

    if bmi < 19:
        bmiRange = "below the healthy range."
    elif bmi <= 25:
        bmiRange = "in the healthy range."
    else:
        bmiRange = "above the healthy range."

    print(f"Your BMI is {bmi} and it falls {bmiRange}")

if __name__ == '__main__':
    main()

# def main():
#     print("This program calculates the BMI and will tell if they are in a healthy range.")

#     # requests weight and height. calculates BMI and decised health class.
#     try:
#         weight = float(input("What is the persons weight in LBS? "))
#         height = float(input("What is the persons height in inches? "))

#         bmi = (weight * 720)/(height*height)

#         if bmi < 19:
#             print("Your BMI is {0:0.2f}, this is below the healthy range.".format(bmi))
#         elif bmi >= 19 and bmi <= 25:
#             print("Your BMI is {0:0.2f}, this is in the healthy range.".format(bmi))
#         elif bmi > 25:
#             print("Your BMI is {0:0.2f}, this is above the helthy range.".format(bmi))
#         else:
#             print("Something went wrong.")
    
#     # Costume error message
#     except TypeError:
#         print("\nYour inputs were not all numbers")
#     except:
#         print("Something went wrong.")

# if __name__ == '__main__':
#     main()
