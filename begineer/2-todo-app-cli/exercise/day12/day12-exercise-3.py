'''
Define a function that:
(1) takes a list as an argument
(2) returns the average value of the list items.

For example, if I called your function with foo([10, 20, 30, 40]) it should return 25 which is the average of the numbers of the list.
Note: You can name the function anyway you want. It's enough to define the function. There is no need to call it.
'''

def average(lst):
    if len(lst) == 0:
        return 0  # To avoid division by zero
    return sum(lst) / len(lst)

list_number = [10, 20, 30, 40]
print(average(list_number))  # Output: 25.0