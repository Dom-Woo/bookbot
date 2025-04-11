
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()
    word_count = len(words) 
    print(f"{word_count} words found in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()