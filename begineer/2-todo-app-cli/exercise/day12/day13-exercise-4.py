'''
Define a function that:
(1) takes a person's name as a parameter
(2) greets the person with Hi Person.

For example, if I call your function using foo("lisa") the function should return Hi lisa .
'''

def greet(name):
    return f"Hi {name.capitalize()}"

# Example usage:
name = input("Enter your name: ")
print(greet(name))  # Output: Hi lisa