# ME Computer, Mandalay.
# June 13, 2022
# exercise_10.py

# 10. Write a program that converts distances measured in kilometers to miles. 
#     One kilometer is approximately 0.62 miles.

# convert3.py
#     A program to convert distances measured in kilometers to miles
# by: Susan Computewell

def main():
    
    print("This program converts distances measured in kilometers to miles.")
    
    kilometers = eval(input("What is the distance in kilometers? "))
    miles = kilometers * 0.62
    
    print("The distance is", miles, "miles.")
          
main()