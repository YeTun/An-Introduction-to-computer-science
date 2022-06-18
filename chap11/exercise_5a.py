# Me Computer, Mandalay.
# June 22, 2022
# exercise_5.py

# (a) count(myList,  x)  (like myList.count(x))
def count(myList, x):
    """ count the occurences of x in myList """
    count = 0
    for i in myList:
        if i == x:
            count += 1
    return count

# (b) isin(myList, x)    (like x in myList)
def isin(myList, x):
    """ return True if x is an item in myList, otherwise return False """
    return count(myList, x) > 0

# (c) index(myList, x)   (like myList.index(x))
def index(myList, x):
    """ return the index of the first occurence of x in myList
        returns error if x does not occur in myList
    """
    counter = 0 # to keep track of current index as we loop thru
    tracker = 0 # how many times x has been found in myList as we loop thru
    for i in myList:
        if i == x:
            tracker +=1
            if tracker == 1: # only save the current index position of the first occurence
                ans = counter
        counter += 1
    return ans

# (d) reverse(myList)    (like myList.revers())
def reverse(myList):
    """" reverse the order of myList items """
    newlist = []
    i = len(myList) - 1
    while i >=0:
        newlist.append(myList[i])
        i -= 1
    return newlist

# (e) sort(myList)       (like myList.sort())
def sort(myList):
    """ sorts the items in myList
        returns error if myList includes non-numeric items
    """
    sortedlist = []
    i = 0
    while i < len(myList):
        j = 0
        while j <= len(sortedlist):
            if j == len(sortedlist) or myList[i] <= sortedlist[j]:
                # loops through the sortedlist stopping either at the end or the first time it
                # reaches an element of sortedlist less than the current element of myList
                # the check for end of list has to be first in the 'or' statement because
                # it will throw an index error in sortedlist[j]
                sortedlist.insert(j, myList[i])
                break
            j += 1
        i += 1
    return sortedlist

def main():
    myList = [8, 6, 7, 5, 3, 0, 9]
    print("Original myList", myList, ", x =", 3)
    myList = myList * 3
    x = 3
    
    print("Count of x: ", count(myList, x))
    print("x in myList: ", isin(myList, x))
    print("Index of x: ", index(myList, x))
    print("Reverse list: ", reverse(myList))
    print("Sort List: ", sort(myList))

if __name__ == '__main__': main()