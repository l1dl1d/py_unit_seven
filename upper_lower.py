def actual_printing(word):
    print(word.upper())
    print(word.lower())
def printing_letters(word):
    for letter in word:
        print(letter)

def main():
    word = input("type in a sentence.")
    actual_printing(word)
    printing_letters(word)
if __name__ == '__main__':
    main()