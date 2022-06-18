# Me Computer, Mandalay.
# June 17, 2022
# exercise_2.py
# This program prints this first ten verses of "The Ants Go Marching"

def verse(n, action):
    print("The ants go marching", n + " by " + n + ",", "hurrah! hurrah!")
    print("The ants go marching", n + " by " + n + ",", "hurrah! hurrah!")
    print("The ants go marching", n + " by " + n + ",")
    print("The little one stops to", action + ",")
    print("And they all go marching down...")
    print("In the ground...")
    print("To get out...")
    print("Of the rain.")
    print("Boom! "*3)
    print()

def main():
    verse("one", "eat a plum")
    verse("two", "enquire who")
    verse("three", "climb a tree")
    verse("four", "hold the door")
    verse("five", "keep it live")
    verse("six", "get its fix")
    verse("seven", "throw his arms toward heaven")
    verse("eight", "jump the gate")
    verse("nine", "draw a line")
    verse("ten", "bite the hen")

main()

# def ants():
#     num = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
#     rhyme = ['suck his thumb', 'tie his shoe', 'take a pee', 'shut the door',
#             'call the hive','pick up sticks', 'look to heaven',
#             'make a date', 'get outta line', 'sing it again']

#     for i in range (10):
#         print(f"The ants go marching {num[i]} by {num[i]}, hurrah! hurrah!")
#         print(f"The ants go marching {num[i]} by {num[i]}, hurrah! hurrah!")
#         print(f"The ants go marching {num[i]} by {num[i]},")
#         print(f"The little one stops to {rhyme[i]},")
#         print("And they all go marching down...")
#         print("In the ground...")
#         print("To get out...")
#         print("Of the rain.")
#         print("Boom! Boom! Boom!")
#         print()

# def main():
#     print("The Ants Go Marhing.")
#     ants()

# main()

# def verses(i, rhyme):
#     print("The ants go marching", i+1, "by", i+1, "Hoorah! Hoorah!")
#     print("The ants go marching", i+1, "by", i+1, "Hoorah! Hoorah!")
#     print("The ants go marching", i+1, "by", i+1)
#     print(rhyme)
#     print("And they all go marching down...")
#     print("In the ground...")
#     print("To get out...")
#     print("Of the rain.")
#     print("Boom! "*3)
#     print("\n")

# rhyme = [
#         "The little one stops to suck his thump",
#         "The little one stops to tie his shoe",
#         "The little one stops to climb a tree",
#         "The little one stops to close the door",
#         "The little one stop to take a dive",
#         "The little one stops to pick up sticks",
#         "The little one stops to pray to heaven",
#         "The little one stops to rollerskate",
#         "The little one stops to check the time"
#         ]

# def main():
#     for i in range(9):
#         verses(i, rhyme[i])

#     print("The ants go marching 10 by 10 Hoorah! Hoorah!")
#     print("The ants go marching 10 by 10 Hoorah! Hoorah!")
#     print("The ants go marching 10 by 10")
#     print('The little one stops to shout\n"THE END!"')

# main()