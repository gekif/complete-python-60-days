'''
We have defined a list of strings in the coding area. Your task is to add some code that:
(1) uses list comprehension to capitalize all the names and surnames of the list, and
(2) prints the updated list.

The output of your code should be as below:
['John Smith', 'Jay Santi', 'Eva Kuki']
'''

names = ['john smith', 'jay santi', 'eva kuki']
names = [name.title() for name in names]
print(names)