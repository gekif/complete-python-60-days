'''
We have defined a numbers variable in the coding area. Add some code that:
(1) multiplies each number of the list by 2, and
(2) prints out the updated list.

Here is the expected output:
[20, 40, 60]
'''

numbers = [10, 20, 30]
numbers = [number * 2 for number in numbers]
print(numbers)