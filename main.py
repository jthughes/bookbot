def main():
    book = "frankenstein"
    with open(f"books/{book}.txt") as f:
        file_contents = f.read()
        word_count = get_word_count(file_contents)
        print(f"Words in \"{book.capitalize()}\": {word_count}")
        char_counts = get_char_count(file_contents)
        sorted_counts = dict(sorted(char_counts.items(), key=lambda x:x[1], reverse=True))
        for char in sorted_counts:
            if char.isalpha():
                print(f"'{char}' appears {sorted_counts[char]} times")

def get_word_count(book):
    words = book.split()
    return len(words)

def get_char_count(book):
    formatted_book = book.lower()
    char_counts = {}
    for char in formatted_book:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return char_counts    


main()