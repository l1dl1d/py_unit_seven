def encode(phrase, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    x = ""
    for letter in phrase:
        value = alphabet.index(letter)
        value = (value + shift)%26
        shifted_alphabet = alphabet[value]
        x = x + shifted_alphabet
    return x
def decode(phrase, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    x = ""
    for letter in phrase:
        value = alphabet.index(letter)
        value = (value - shift)%26
        shifted_alphabet = alphabet[value]
        x = x + shifted_alphabet
    return x
def main():
    choice = input("press e to encode, d to decode or q to quit.")
    phrase = input("please enter text to be encoded.")
    shift = input("please enter the key (0-25):")
    if choice == e:
        print(encode())
    elif choice == d:
        print(decode())
    elif choice == q:
        quit()


