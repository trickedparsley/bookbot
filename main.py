def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
def main():
    num_words = 0
    for word in get_book_text("./books/frankenstein.txt").split():
        num_words += 1
    print(f"Found {num_words} total words")

    
main()