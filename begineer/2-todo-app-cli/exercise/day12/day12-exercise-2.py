'''
Complete the strength function. The function will check the strength of a given password. Specifically, the function should:

(1) get a password argument
(2) return the string "Strong Password" if all of the following conditions are true:
Password is 8 or more characters
Password has at least one uppercase letter
Password has at least one digit.

(3) if one or more of the above conditions are not met, the function should return "Weak Password".
'''

def strength(password):
    if (len(password) >= 8 and
        any(char.isupper() for char in password) and
        any(char.isdigit() for char in password)):
        return "Strong Password"
    else:
        return "Weak Password"

# Example usage:
password = input("Enter your password: ")
print(strength(password))