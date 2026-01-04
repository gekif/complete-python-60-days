'''
The coding area contains a list of numbers, each stored as a string. Your task is to add some code that:
(1) converts the numbers from strings to floats, and
(2) prints out the updated list.

The output of your code should be as below. Notice the numbers are floats without quotes.
[10.0, 19.1, 20.0]
'''

user_entries = ['10', '19.1', '20']
user_numbers = [float(entry) for entry in user_entries]
print(user_numbers)