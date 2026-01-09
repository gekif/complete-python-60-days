'''
Implement a function that:
(1) takes a person's name (e.g. 'john') as a parameter
(2) returns a greeting (e.g. Hi John)

Note that the first letter of the person's name should be capitalized by the function.
'''

def greet(name):
    capitalized_name = name.capitalize()
    greeting = f"Hi {capitalized_name}"
    return greeting

# Example usage:
name = input("Enter your name: ")
print(greet(name))  # Output: Hi John