def word_counter(text):
    word_list = text
    words = len(word_list.split())
    return words

def char_counter(text):
    char_dict = {}
    char_counts = text.lower()
    for char in char_counts:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict