# average5.py
# average5.txt

def main():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName, 'r')
    
    total = 0
    count = 0
    for line in infile:
        total = total + eval(line)
        count = count + 1
    
    print("\nThe average of the numbers is", total / count)

main()
