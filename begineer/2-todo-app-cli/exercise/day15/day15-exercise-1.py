"""
Your task is to create a program that generates a random whole number. Here is how the program should behave:

As you can see, the program first asks the user to enter a whole number. Then, once the user enters a number, the program asks the user again to enter another number.

Then, the program returns a random number that falls between the two whole numbers. Here is another example:
"""

import random

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

random_number = random.randint(lower_bound, upper_bound)
print(f"A random number between {lower_bound} and {upper_bound} is {random_number}.")
