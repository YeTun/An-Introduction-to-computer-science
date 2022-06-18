# Me Computer, Mandalay.
# June 17, 2022
# exercise_11.py
# Square each value in a list

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2


def test():
    nums = list(range(10))
    squareEach(nums)
    print(nums)

test()