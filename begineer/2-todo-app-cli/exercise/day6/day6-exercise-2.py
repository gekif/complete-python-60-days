'''
In the coding area, there's an essay.txt file uploaded. Your task is to write a program that:
(1) opens the essay.txt file in read mode,
(2) reads its content,
(3) converts the first letter of each word into uppercase,
(4) prints out the updated content.
'''

file = open('essay.txt', 'r')
content = file.read()
file.close()

updated_content = content.title()
print(updated_content)