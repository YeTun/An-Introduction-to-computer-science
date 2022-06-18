# Me Computer, Mandalay.
# June 22, 2022
# exercise_7.py

def innerProd(x, y):
    # x and y must be the same length
    i = 0
    total = 0
    while i < len(x):
        total += x[i] * y[i]
        i += 1
    return total

def main():
    myList = [8,6,7,5,3,0,9]
    newList = [9,0,3,5,7,6,8]

    sum = innerProd(myList, newList)
    print(sum)

main()