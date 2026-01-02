'''
In the coding area, there is an essay.txt file uploaded. Your task is to write a program that:
(1) opens the essay.txt file in read mode,
(2) reads its content,
(3) finds out the number of characters in the content,
(4) prints out the number of characters.

Here is the expected output:
144
'''

file = open('essay.txt', 'r')
content = file.read()
file.close()

length_content = len(content)
print(length_content)