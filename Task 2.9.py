#9)write a program that takes a string and returns the number words in it

import re

def count_words(input_string):
    # Use regex to find words (handles punctuation and extra spaces correctly)
    words = re.findall(r'\b\w+\b', input_string)
    return len(words)

# Example usage:
input_string = input("Enter a string: ")
word_count = count_words(input_string)
print(f"Number of words: {word_count}")

