# Me Computer, Mandalay.
# June 16, 2022
# exercise_8.py
# This program encodes and decodes a message using Ceaser Cipher

#  8. One problem with the previous exercise is that it does not deal with the case when we "drop off the end" of the alphabet. A
#     true Caesar cipher does the shifting in a circular fashion where the next character after "z" is "a." Modify your solution
#     to the previous problem to make it circular. You may assume that the input consists only of letters and paces.
#     Hint: Make a string containing all the cahracters of your alphabet and use positions in this string as your code. You do not
#     have to shift "z" int "a"; jsut make sure that you use a circular shift over the entire sequence of characters in your alphabet
#     string.

# cipher.py

# def encode():
#     print("You are encoding a message.")
#     key = int(input("Enter a key number that will encode your message: "))
#     uncodedMessage = input("Enter your message: ")

#     encodedMessage = []
#     for ch in uncodedMessage:
#         codecharacter = chr(ord(ch) + key)
#         if codecharacter > 'Z' and codecharacter < 'a':
#             codecharacter = chr((ord(codecharacter)%90)+64)
#         if codecharacter > 'z':
#             codecharacter = chr((ord(codecharacter)%122)+96)
#         encodedMessage.append(codecharacter)

#     joinencodedmessage = "".join(encodedMessage)
#     print(f"The encoded message is: {joinencodedmessage}")

# def decode():
#     print("You are decoding a message.")
#     key = int(input("Enter a key number that will decode your message: "))
#     encodedMessage = input("Enter your message: ")

#     decodedMessage = []
#     for num in encodedMessage:
#         decodecharcter = chr(ord(num) - key)
#         decodedMessage.append(decodecharcter)

#     joindecodedMessage = "".join(decodedMessage)
#     print(f"The decoded message is: {joindecodedMessage}")

# def main():
#     print("This program Encodes and Decodes a message into random numbers.")
#     choice = input("Do you want to encode a message or decode a message?: ")
#     if choice == "encode":
#         encode()
#     elif choice == "decode":
#         decode()
#     else:
#         print("Invalid choice")

# main()


def encode():
    # Get plaintext(p_text) and key(x) from the user
    p_text = input("Enter the message you'd like encrypted.\n")
    key = eval(input("What's the key? : "))

    p_text = ''.join(p_text.lower().split())
    
    # Create string of letters
    table = "abcdefghijklmnopqrstuvwxyz"

    # Convert plaintext to ciphertext(c_text) using cipher loop
    c_text = ""
    for ch in p_text:
        c_text += table[((ord(ch) - 97) + key) %26]

    print("Your encoded message is {0}.".format(c_text))

def decode():
    # Get ciphertext(c_text) and key(x) from the user
    c_text = input("Enter the message you'd like decrypted.\n")
    key = eval(input("What's the key? : "))

    c_text = ''.join(c_text.lower().split())
    
    # Create string of letters
    table = "abcdefghijklmnopqrstuvwxyz"

    # Convert ciphertext to plaintext(p_text) using cipher loop
    p_text = ""
    for ch in c_text:
        p_text += table[((ord(ch) - 97) - key) %26]

    print("Your encoded message is {0}.".format(p_text))

def main():
    print("This program Encodes and Decodes a message into random numbers.")
    choice = input("Do you want to encode a message or decode a message?: ")
    if choice == "encode":
        encode()
    elif choice == "decode":
        decode()
    else:
        print("Invalid choice")

main()
