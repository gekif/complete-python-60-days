'''
In the coding area, there's a bear.txt file uploaded. Your task is to write a program that:
(1) opens the bear.txt file in read mode,
(2) reads its content, and
(3) prints out its content.
'''

file = open('bear.txt', 'r')
content = file.read()
file.close()

print(content)
