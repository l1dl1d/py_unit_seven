def actual_printing(word):
    print(word.upper())
    print(word.lower())
def main():
    word = input("type in a sentence.")
    actual_printing(word)
if __name__ == '__main__':
    main()