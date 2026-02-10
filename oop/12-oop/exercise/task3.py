"""
Implement/code the User.age method so the method returns the age of the user given the self.birthyear instance variable and the current_year parameters.
"""

class User:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        pass

    def age(self, current_year):
        return current_year - self.birthyear

