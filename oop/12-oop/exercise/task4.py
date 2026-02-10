"""
Task 4: Let us suppose the current year is 2023.
1. Create a User instance for John, whose birth year is 1999.
2. Call the age method for that instance and print out the output.
You should get 24 as output.
"""

class User:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        pass

    def age(self, current_year):
        return current_year - self.birthyear

john = User("John", 1999)
print(john.age(2023))