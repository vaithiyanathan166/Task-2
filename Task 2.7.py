#7)write a program that takes a string and returns the most frequent character on it

from collections import Counter

def most_frequent_character(s):
    s = s.replace(" ", "")  # Remove spaces (optional)
    if not s:
        return None  # Handle empty string case
    
    freq_count = Counter(s)  # Count character occurrences
    most_frequent = max(freq_count, key=freq_count.get)  # Find the most frequent character
    return most_frequent, freq_count[most_frequent]

# Example usage
input_string = input("Enter a string: ")
char, count = most_frequent_character(input_string)

if char:
    print(f"Most frequent character: '{char}' (occurs {count} times)")
else:
    print("Empty string provided!")
