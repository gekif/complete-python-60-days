"""
Implement/code the User.get_name method,
so the method returns
the capitalized version of the user's name (e.g., JOHN). Note that the name is stored in the instance variable.
Also, call the method for the instance you created in Task 4.
"""

class User:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        return self.name.upper()

    def age(self, current_year):
        return current_year - self.birthyear

john = User("John", 1999)
print(john.age(2023))
print(john.get_name())