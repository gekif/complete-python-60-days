'''
The code in the coding area successfully reads and prints out the content of the bear.txt file.
Your task is to rewrite the code by using a "with" context manager to achieve the same thing.
'''

with open("bear.txt", 'r') as file:
    content = file.read()
    print(content)

