import sys
from stats import get_book_words, get_char_count, sort_dict


def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    return file_contents


def print_report(input, count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count[1]} total words")
    print("--------- Character Count -------")
    for item in input:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text()
    word_count = get_book_words(text)
    char_count = get_char_count(word_count)
    sorted_dict = sort_dict(char_count)
    print_report(sorted_dict, word_count)


main()
