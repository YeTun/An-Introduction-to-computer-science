# average7.py
# nested loop

def main():
    fileName = input("What file are the  numbers in? ")
    
    infile = open(fileName, "r")
    total = 0
    count = 0
    
    line = infile.readline()
    while line != "":
        for xStr in line.split(","):
            total = total + eval(xStr)
            count = count + 1
        line = infile.readline()
    
    print("\nThe average of the numbers is", total / count)

main()
