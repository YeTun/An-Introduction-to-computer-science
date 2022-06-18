# average2.py
# Interactive Loop

def main():
    total = 0
    count = 0
    moredata = "yes"
    while moredata[0] == "y":
        x = eval(input("Enter a number >> "))
        
        total = total + x
        count += 1
        
        moredata = input("Do you have more numbers (yes or no)? ")
    
    print("\nThe average of the numbers is", total / count)

main()
