'''
The code below tries to convert all the numbers to integers.
However, the code has an error. Try to fix the error.

numbers = [10.1, 12.3, 14.7]
numbers = [int(number) for item in numbers]
print(numbers)
'''

numbers = [10.1, 12.3, 14.7]
numbers = [float(number) for number in numbers]
print(numbers)