def encode(phrase, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    x = ""
    for letter in phrase:
        value = alphabet.index(letter)
        value = value + shift
        shifted_alphabet = alphabet[value]
        x = x + shifted_alphabet
    return x
def decode(phrase, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    x = ""
    for letter in phrase:
        value = alphabet.index(letter)
        value = (value + shift)%26
        shifted_alphabet = alphabet[value]
        x = x + shifted_alphabet
    return x
def main():
    choice = input("press e, to encode, d to decode, or q to quit.")
    if choice == e:
        phrase = input("please enter text to be encoded:")
        return encode()
    elif choice == d:

        return decode()
    elif choice == q:
        quit()
if __name__ == '__main__':
    main()
