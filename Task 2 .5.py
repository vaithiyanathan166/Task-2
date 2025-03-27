#5)write a program that takes a string returns True if it is a palindrome ,false otherwise

#A palindrome is a string that reads the same forwards and backwards. To determine if a given string is a palindrome,  compare the string to its reverse. 
def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for uniform comparison
    cleaned_string = ''.join(input_string.split()).lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Example usage
input_string = "A man a plan a canal Panama"
result = is_palindrome(input_string)
print("Original string:", input_string)
print("Is palindrome:", result)
