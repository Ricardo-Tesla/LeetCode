# change characters to lowercase
# remove  non-alphanumeric characters 
# compared the filtered characters to the reverse of  the characters 
# if they are equivalent, return True, and false otherwise


def is_palindrome(s):
    filtered_chars = ''.join([char.lower() for char in s if char.isalnum()])
    return filtered_chars == filtered_chars[::-1]

s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))  # Output: True
