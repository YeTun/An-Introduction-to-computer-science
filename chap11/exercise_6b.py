import random

def shuffle(myList): 
    shuffledList = []
    while len(myList) != 0:
        value = random.choice(myList)
        myList.remove(value)
        shuffledList.append(value)
    return shuffledList

def main():
    myList = [1,2,2,3,3,3,4,5,5,6,7,8,8,8,8,9,10]
    print(myList)
    shuffledList = shuffle(myList)
    print(shuffledList)

main()