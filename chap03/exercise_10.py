# ME Computer, Mandalay.
# June 14, 2022
# exercise_10.py

# This program determines the length of a ladder required given 
# the height of house and angle of ladder.

# 10. Write a program to determine the length of a ladder required to reach a 
#     given height when leaned against a house. The height and angle of the
#     ladder are given as inputs. To compute length use:
#       length = height / sin angle
#
#     Note: The angle must be in radians. Prompt for an angle in degrees and 
#     use this formula to convert:
#       radians = (pi / 180) degrees

import math

def main():
    print("This program helps to determine the length of ladder needed")
    print("to reach a given height.")

    height = float(input("How high must you reach? "))
    angle = float(input("What will the ladder angle be (in degrees)? "))

    radians = math.pi * angle / 180
    # note: can also use radians = math.radians(angle)
    length = height / math.sin(radians)

    print()
    print("Length of ladder required:", length)

main()
