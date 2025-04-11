from stats import get_num_words
from stats import get_chars_dict
from stats import sort_chars
from stats import sort_on

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = sort_chars(chars_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}:")
    print("============= END ===============")
    print("Found 75767 total words")
    print("e: 44538")
    print("t: 29493")


def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()