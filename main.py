import sys
from stats import * # pyright: ignore[reportMissingImports]
def main():
    if len(sys.argv) != 2:
          print("Usage: python3 main.py <path_to_book>")
          exit(1)
    #book = "./books/frankenstein.txt"
    book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print(get_num_words(book))
    #print(count_symbols(book))
    for item in sort_list(count_symbols(book)):
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    
main()