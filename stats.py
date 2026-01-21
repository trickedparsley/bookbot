def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def get_num_words(filepath):
    num_words = 0
    for word in get_book_text(filepath).split():
        num_words += 1
    print("----------- Word Count ----------")
    return (f"Found {num_words} total words")

def count_symbols(filepath):
    symbols = {
    }
    lowercase_temp = get_book_text(filepath).lower()
    for character in lowercase_temp:
        if character not in symbols:
            symbols[character] = 1
        else:
            symbols[character] = symbols[character] + 1
    return symbols

def sort_list(dictionary):
    list = []
    for key, value in dictionary.items():
        if key.isalpha():
            list.append({"char": key, "num": value})
    print("----------- Character Count ----------")
    return sorted(list, key=lambda item: item["num"], reverse=True)