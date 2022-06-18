# Me Computer, Mandalay.
# June 18, 2022
# exercise_4.py
# College classification

def main():
    print("College Classification\n")
    credits = float(input("Enter number of credits: "))
    if credits < 7:
        cls = "Freshman"
    elif credits < 16:
        cls = "Sophomore"
    elif credits < 26:
        cls = "Junior"
    else:
        cls = "Senior"
    print("The classification is", cls)

if __name__ == '__main__': main()