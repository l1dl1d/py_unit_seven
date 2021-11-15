def encode(phrase, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    x = ""
    for letter in phrase:
        value = alphabet.index(letter)
        value = value + shift
        shifted_alphabet = alphabet[value]
        x = x + shifted_alphabet
    return x