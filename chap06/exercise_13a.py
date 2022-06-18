# Me Computer, Mandalay.
# June 17, 2022
# exercise_13.py
# Fuction converts each string into a number in a list of strings

def toNumbers(strList):
    # nums is a list of strings, function modifies list by converting to floats
    for i in range(len(strList)):
        strList[i] = float(strList[i])

def main():
    # Get list of numbers
    strings = input("Enter a list of numbers separated by commas: ")
    myList = strings.split(",")
    
    # square list
    toNumbers(myList)
    
    # check transformation
    print(myList)

main()

# def toNumbers(nums):
#     for i in range(len(nums)):
#         nums[i] = int(nums[i])

# def main():
#     numlist = ["2", "3", "5", "5"]
#     toNumbers(numlist)
#     print(numlist)

# main()


# def toNumbers(strList):
#     for x in range (len(strList)):
#         strList[x] = int(strList[x])
#     return(strList)

# def test():
#     list = ['1', '2', '3', '4', '5']
#     z = toNumbers(list)
#     print(z)

# test()
