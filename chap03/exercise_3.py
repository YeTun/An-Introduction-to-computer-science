# ME Computer, Mandalay.
# June 14, 2022
# exercise_3.py
# This program determines the moleculer weight of a hydrocarbon

#  3. Write a program that computes the molecular weight of a carbohydrate 
#     (in grams per mole) based on the number of hydrogen, carbon, and oxygen atoms 
#     in the molecule. The program should prompt the user to enter the number of 
#     hydrogen atomes, the number of carbon atoms, and the number of oxygen atoms. 
#     The program then prints the total combined molecular weight of all the atoms 
#     based on these individual atom weights:
#                  Atom      Weight
#                            (grams/mole)
#                  ______________________
#                  H         1.00894
#                  C         12.0107
#                  O         15.9994
#
#     For example, the molecular weight of water (H20) is 2(1.00794) + 15.9994 = 18.01528.


def main():
    print("Program calculates the molecular weight of a carbohydate")
    print("based on the number of hydrogen, carbon & oxygen atoms.")
    
    hydrogen = int(input("Enter the number of hydrogen atoms: ")) * 1.00794
    carbon = int(input("Enter the number of carbon atoms: ")) * 12.0107
    oxygen = int(input("Enter the number of oxygen atoms: ")) * 15.9994
    
    molecularWeight = hydrogen + carbon + oxygen

    print(f"The molecular weight is {molecularWeight} grams.")
    
main()
