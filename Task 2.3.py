#3 ) To write a program that takes a string and returns a new string containing only the vowels, 

def extract_vowels(input_string):
    # Define the set of vowels (both uppercase and lowercase)
    vowels = "aeiouAEIOU"
    
    # Use a list comprehension to filter out the vowels
    result = ''.join([char for char in input_string if char in vowels])
    
    return result

# Example usage
input_string = "Hello, World!"
vowel_string = extract_vowels(input_string)
print("Original string:", input_string)
print("Vowel string:", vowel_string)

