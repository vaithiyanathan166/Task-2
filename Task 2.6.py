#6)write a program that takes a two string returns the longest common substring between them 
    # Initialize a 2D list with zeros
def longest_common_substring(str1, str2):
    len1, len2 = len(str1), len(str2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]  # 2D list initialized with zeros
    max_length = 0  # To store the length of the longest common substring
    end_index = 0  # To track where the substring ends in str1

    # Fill the dp table
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:  # If characters match
                dp[i][j] = dp[i - 1][j - 1] + 1  # Extend the previous match
                if dp[i][j] > max_length:  # Update max_length and end_index
                    max_length = dp[i][j]
                    end_index = i  # Store the ending index in str1

    # Extract the longest common substring
    longest_substring = str1[end_index - max_length:end_index]  
    return longest_substring

# Example usage
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

result = longest_common_substring(str1, str2)
print(f"Longest Common Substring: '{result}'")
