def printCounts(myList):
    print("COUNTS")
    count1 = count(myList,1)
    count2 = count(myList,2)
    count3 = count(myList,3)
    count4 = count(myList,8)
    print(count1)
    print(count2)
    print(count3)
    print(count4)
    print("******")

def printIsins(myList):
    print("ISINS")
    isin1 = isin(myList, "a")
    isin2 = isin(myList, 4)
    isin3 = isin(myList, 10)
    isin4 = isin(myList, 12)
    print(isin1)
    print(isin2)
    print(isin3)
    print(isin4)
    print("******")

def printIndexes(myList):
    print("INDEXES")
    index1 = index(myList, 1)
    index2 = index(myList, 2)
    index3 = index(myList, 4)
    index4 = index(myList, 9)
    print(index1)
    print(index2)
    print(index3)
    print(index4)
    print("******")

def printReversedList(myList):
    print("REVERSED LIST")
    reversedList = reverse(myList)
    print(reversedList)
    print("******")

def count(myList, x):
    count = 0
    for i in myList:
        if i == x:
            count = count + 1
    return count

def isin(myList, x):
    if x in myList:
        return True
    else:
        return False

def index(myList, x):
    count = -1
    for i in myList:
        count = count + 1
        if i == x:
            return count

def reverse(myList):
    reverseList = []
    for i in myList[::-1]:
        reverseList.append(i)
    return reverseList

def sort(myList2):
    pass

def main():
    myList = [1,2,2,3,3,3,4,5,5,6,7,8,8,8,8,9,10]
    myList2 = [3,5,7,4,6,1,3,2,9,97,65,43,33,21,65,77,8,99]
    printCounts(myList)
    printIsins(myList)
    printIndexes(myList)
    printReversedList(myList)
   
main()
