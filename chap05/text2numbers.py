# text2numbers.py
# A program to convert a texual message into a sequence of
# numbers, utilizing the underlying Unicode encoding.

def main():
    
    print("This program converts a textual message into a sequence")
    print("of numbers representing the Unicode encoding of the message.")

    # Get the message to encode
    message = input("Please enter the message to encode: ")

    print("\nHere are the Unicode codes:")

    # Loop through the message and print out the Unicode values
    count = 0
    for ch in message:
        print(ord(ch), end=" ")
        if ch != " ":
            count += 1

    print(f"\nThe number of charachers is {count}.")

main()
