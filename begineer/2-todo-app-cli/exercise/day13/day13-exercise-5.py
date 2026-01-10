"""
Define a function that:
(1) takes a string as a parameter
(2) returns False if the string contains less than 8 characters
(3) returns True if the string contains 8 or more characters

In other words, if I called your function with foo("mypass") it would return False. If I called it with foo("mylongpassword") it would return True, and so on.
"""

def is_valid_password(password):
    if len(password) >= 8:
        return True
    else:
        return False

# Example usage:
user_password = input("Enter a password: ")
validity = is_valid_password(user_password)
print(validity)