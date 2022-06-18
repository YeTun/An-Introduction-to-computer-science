# average1.py

def main():
    n = eval(input("How many numbers do you have? "))

    total = 0
    for i in range(n):
        x = eval(input("Enter a number >> "))
        total += x
    
    print("\nThe average of the numbers is", total / n)

main()
