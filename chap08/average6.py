# average6.py
# average6.txt

def main():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName, "r")
    
    total = 0
    count = 0
    line = infile.readline()
    while line != "":
        total = total + eval(line)
        count = count + 1
        line = infile.readline()
    
    print("\nThe average of the numbers is", total / count)

main()
