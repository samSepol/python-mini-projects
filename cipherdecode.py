import pyfiglet

ascii_banner = pyfiglet.figlet_format("Ceasar Cipher")
print(ascii_banner)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '?', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]


def Caesar(start_text, shift, cipher_direction):
    generated_text = ""
    for letter in start_text.replace(" ", ""):
        if cipher_direction == "encode":
            position = alphabet.index(letter)
            new_pos = position + shift
            generated_text += alphabet[new_pos]
        elif direction == "decode":
            position = alphabet.index(letter)
            new_pos = position - shift
            generated_text += alphabet[new_pos]
        else:
            print("please type proper direction.")
    print(f"The {cipher_direction} text is {generated_text}")


player_continue = True
while player_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26

    Caesar(start_text=text, shift=shift, cipher_direction=direction)
    playerChoice = input("Do you want to continue yes or no . ")
    if playerChoice == "no":
        player_continue = False
        print("Bye 👋")
