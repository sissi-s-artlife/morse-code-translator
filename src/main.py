from morse_alphabet import morse_code

def encode(message):
    """Adds spaces between each letter in message and replaces spaces between words with '/'."""
    formatted_message = ""
    words = message.split()
    for word in words:
        for char in word:
            formatted_message += morse_code[char.upper()] + " "
        formatted_message += "/"
    return formatted_message.strip()

def decode(morse_code, message):
    """Decodes Morse code into the Latin Alphabet with specific formatting."""
    reverse_morse_code = {v: k for k, v in morse_code.items()}
    words = message.split("/")
    decoded_message = ""
    for word in words:
        letters = word.split()
        for i, letter in enumerate(letters):
            decoded_message += reverse_morse_code[letter]
        decoded_message += " "
    decoded_message = decoded_message.strip()
    return decoded_message

print("P.S.Remember to format your message! In order to get the correct output, always put slashes between words without any spaces in between words and put spaces in between letters if you are decoding. This program uses slashes instead of spaces for words and single space in between letters as coding convention. Enjoy encoding & decoding!")
print("Hello world!Welcome to morse code translator!")
print(".... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.-- .-- . .-.. -.-. --- -- . / - --- / -- --- .-. ... . / -.-. --- -.. . / - .-. .- -. ... .-.. .- - --- .-. -.-.--")
game_continue = "yes"
while game_continue=="yes":
    
    choice = input("Decode or encode? ").lower()
    if choice == "encode":
        message = input("Enter your message: ")
        encoded_message = encode(message)
        print("Encoded message:", encoded_message)
    elif choice == "decode":
        message = input("Enter your message: ")
        decoded_message = decode(morse_code, message)
        print("Decoded message:", decoded_message)
    game_continue = input("Do you want to type another message? Enter 'yes' if you want to, or 'no' if you don't want: ").lower()

if game_continue == "no":
    print("Goodbye!")







        