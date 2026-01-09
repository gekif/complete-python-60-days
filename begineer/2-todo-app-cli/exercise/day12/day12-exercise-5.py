'''
Implement a function that:
(1) takes two strings as parameters,
(2) concatenates the strings
(3) returns the concatenated string.

For example, if I called your function with foo('hello', 'hi') it would return hellohi.
'''

def concatenate_strings(str1, str2):
    concatenated = str1 + str2
    return concatenated

# Example usage:
result = concatenate_strings('hello', 'hi')
print(result)  # Output: hellohi