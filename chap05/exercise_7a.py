# Me Computer, Mandalay.
# June 16, 2022
# exercise_7.py and exercise_8.py
# This program encodes and decodes a message using Ceaser Cipher

#  7. A Caesar cipher is a simple substitution cipher based on the idea of shifting 
#     each letter of the plaintext message a fixed number (called the key) of positions 
#     in the alphabet. For example, if the key is 2, the word "Sourpuss" would be encoded 
#     as "Uqwtrwuu." The original message can be recovered by "reencoding" it using the negative of the key.
#
#   Write a program that can enconde and decode Caesar ciphers. The input to the program 
#   will be a string of plaintext and the value of the key. The output will be an encoded 
#   message where each character in the original message is replaced by shifting it key 
#   characters in the Unicode character set. For exmaple, if ch is a character in the string 
#   and key is the amount to shift, then the character that replaces ch can be calculated 
#   as: chr(ord(ch) + key).

# cipher.py

def encodeDecode(ed):
    # intro message
    print("This program creates a Caesar cipher.")
    print("For a message entered it will shift the characters by a specified")
    print("number. A shift of [1] changes A->B B->C, [25] A->Z, B->A.")
    
    # enter word to encode
    message = str(input("Enter a message to encode: "))
    message = message.lower()    
    # enter key
    key = int(input("Enter the number of characters to shift by [0 - 25]: "))

    # for loop creating encoded and decoded word
    encodedMessage = []
    lookup = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    for word in message.split():
        encodedWord = ""
        for ch in word:
            encodedCh = ""
            encodedCh += lookup[lookup.find(ch) + key*ed]
            encodedWord += encodedCh
        encodedMessage.append(encodedWord)

    # print result
    print(" ".join(encodedMessage))

def main():
    choice = input("Do you want to encode a message or decode a message?: ")
    if choice == "encode":
        encodeDecode(1)
    elif choice == "decode":
        encodeDecode(-1)
    else:
        print("Invalid choice.")

main()


# def encode():
#     print("You are encoding a message.")
#     key = int(input("Enter a key number that will encode your message: "))
#     uncodedMessage = input("Enter your message: ")

#     encodedMessage = []
#     for ch in uncodedMessage:
#         codecharacter = chr(ord(ch) + key)
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


# def encode():

#     # Get plaintext(p_text) and key(x) from the user
#     p_text = input("Enter the message you'd like encrypted.\n")
#     key = eval(input("What's the key? : "))
   
#     # Convert plaintext to ciphertext(c_text) using cipher loop
#     c_text = ""
#     for ch in p_text:
#         c_text += chr(ord(ch) + key)

#     print("Your encoded message is {0}.".format(c_text))

# def decode():

#     # Get plaintext(p_text) and key(x) from the user
#     c_text = input("Enter the message you'd like decrypted.\n")
#     key = eval(input("What's the key? : "))
   
#     # Convert plaintext to ciphertext(c_text) using cipher loop
#     p_text = ""
#     for ch in c_text:
#         p_text += chr(ord(ch) - key)

#     print("Your decoded message is {0}.".format(p_text))

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