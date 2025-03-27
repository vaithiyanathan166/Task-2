#To write a Python program that calculates the total number of vowels and counts the occurrences of each individual vowel (a, e, i, o, u) in a given string, 

def count_vowels(text):
    vowels = "aeiou"
    text = text.lower()  # Convert the text to lowercase for case-insensitive counting
    vowel_counts = {v: 0 for v in vowels}  # Initialize a dictionary to store vowel counts
    total_vowels = 0  # Initialize total vowel count

    # Loop through each character in the text
    for char in text:
        if char in vowels:
            vowel_counts[char] += 1  # Increment the count of the specific vowel
            total_vowels += 1  # Increment total vowel count

    return total_vowels, vowel_counts

# Example usage
input_text = input("Enter a string: ")
total, counts = count_vowels(input_text)

# Display the results
print(f"\nTotal number of vowels: {total}")
print("Occurrences of each vowel:")
for vowel, count in counts.items():
    print(f"{vowel}: {count}")
