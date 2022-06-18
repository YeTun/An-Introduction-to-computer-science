# ME Computer, Mandalay.
# June 14, 20222
# exercise_4.py
# This program determines the distance of a lightening bolt.

#  4. Write a program that determines the distance to a lightning strike based on 
#     the time elapsed between the flash and the sound of thunder. The speed of sound 
#     is approximately 1100 ft/sec and 1 mile is 5280 ft.

def main():
    print("This program calculates the distance from a lightning strike.")    
    timeElapsed = int(input("Enter number of seconds between flash and crash: "))

    distanceToLightning = timeElapsed * 1100 / 5280
    
    print(f"The lightning is {round(distanceToLightning, 1)} miles away.")

main()
