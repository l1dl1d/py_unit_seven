def half_slice(word):
    mid = len(word)//2
    half_two = word[mid:]
    half_one = word[0:mid]
    slice = half_two + half_one
    return slice
def no_first_last(str):
    length = len(str)
    str_one = str[1:-1]
    return str_one
def longest(phrase):
    pass


def title_case(sentence):
    pass
def main():
    str = input("type in a word")
    word = input("type in a word")
    print(half_slice(word))
    print(no_first_last(str))
if __name__ == '__main__':
    main()
