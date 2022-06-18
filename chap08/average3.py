# average3.py
# Sentinel Loop

def main():
    total = 0
    count = 0
    
    x = eval(input("Enter a number (negative to quit) >> "))
    while x >= 0:
        total = total + x
        count = count + 1
        x = eval(input("Enter a number (negative to quit) >> "))
    
    
    print("\nThe average of the numbers is", total / count)

main()
