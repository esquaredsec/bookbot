from stats import word_counter

def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    words_final = word_counter(text)
    print(f"Found {words_final} total words")

if __name__ == "__main__":
    main()