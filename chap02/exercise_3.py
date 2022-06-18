# ME Computer, Mandalay.
# June 12, 2022
# exercise_3.py

#  3. Modify the avg2.py program (Section 2.5.3) to find the average of three exam scores.
#
# avg3.py
'''
A simple program to average three exam scores  
Illustrates use of multiple input
'''

def main():
    
    print("This program computes the average of three exam scores.")
    score1, score2, score3 = eval(input("Enter three scores separated by a comma: "))
    
    average = (score1 + score2 + score3) / 3

#    print("The average of the scores is:", average)
    print(f"The average of the scores is {average:3.2f}.")

main()
