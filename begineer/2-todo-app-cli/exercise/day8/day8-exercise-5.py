'''
The code in the coding area successfully reads and prints out the number of characters in the bear.txt file. Similar to the previous task, your task is to rewrite the code by using a "with" context manager to achieve the same thing.
'''

with open("bear.txt", 'r') as file:
    content = file.read()
    print(len(content))