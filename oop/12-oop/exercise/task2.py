"""
Task 2: Add an __init__ method to the User class. The method should have:
1. three parameters, self, name, and birthyear.
2. name and birthyear should also be instance variables.
Solution:  See the attached task2.py file in the Resources of the next lecture.
"""

class User:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        pass

    def age(self, current_year):
        pass