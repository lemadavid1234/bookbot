from stats import get_num_words
from stats import get_num_char
from stats import get_sorted_list

def get_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()

    return file_contents

def print_report(list, numWords, filePath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filePath}...")
    print("----------- Word Count ----------")
    print(f"Found {numWords} total words")
    print("--------- Character Count -------")
    for item in list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def main():
    
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]

    #print(get_book_text("./books/frankenstein.txt"))
    
    num_words = get_num_words(get_book_text(path_to_book))
    #print(f"Found {num_words} total words")
   
    #print(get_num_char(get_book_text("./books/frankenstein.txt")))

    list = get_sorted_list(get_num_char(get_book_text(path_to_book)))
    print_report(list, num_words, path_to_book)

main()