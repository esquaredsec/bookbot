from stats import word_counter, char_counter

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    total_words = word_counter(text)
    char_dict_count = char_counter(text)
    print(f"Found {total_words} total words")
    print(char_dict_count)

def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    main()