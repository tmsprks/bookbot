import sys
from stats import get_num_words, get_num_chars, sort_dict

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = get_num_chars(text)
    sorted_array = sort_dict(characters)

    # print("============ BOOKBOT ============")
    # print("Analyzing book found at books/frankenstein.txt...")
    # print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    # print("--------- Character Count -------")
    for entry in sorted_array:
        if entry["char"].isalpha():
            print(f'{entry["char"]}: {entry["num"]}')
    # print("============= END ===============")


main()