#4)write a program that takes a string returns a number of unique characteres in it

def count_unique_characters(input_string):
    # Use a set to store unique characters
    unique_characters = set(input_string)
    
    # Return the number of unique characters
    return len(unique_characters)

# Example usage
input_string = "Hello, World!"
unique_count = count_unique_characters(input_string)
print("Original string:", input_string)
print("Number of unique characters:", unique_count)
