'''
Extend the given code so it prints out the sum of the numbers.
Note that the numbers are currently string types.

The output of your code should be as below:
49.1
'''

# Define the initial list of user entries as strings
user_entries = ['10', '19.1', '20']

# Convert the string entries to floats using list comprehension
user_numbers = [float(entry) for entry in user_entries]

# Calculate the sum of the converted float numbers
total_sum = sum(user_numbers)

# Print the total sum
print(total_sum)