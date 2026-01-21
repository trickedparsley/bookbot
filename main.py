from stats import * # pyright: ignore[reportMissingImports]
def main():
    book = "./books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print(get_num_words(book))
    #print(count_symbols(book))
    for item in sort_list(count_symbols(book)):
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    
main()