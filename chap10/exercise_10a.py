# Me Computer, Mandalay.
# June 21, 2022
# exercise_10a.py

from cube import Cube

def main():
    print("This program calculates the volume and surface area of a cube.")
    
    side = eval(input("Enter the length of a cube's side: "))
    cube = Cube(side)
    
    print(f"The volume of your cube is {cube.volume()}.")
    print(f"And The area of your cube is {cube.surfaceArea()}.")

main()
