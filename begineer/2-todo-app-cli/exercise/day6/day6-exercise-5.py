'''
Create a program that:
(1) generates a new file with name file.txt, and
(2) writes the text snail in that file.
'''

file = open('file.txt', 'w')
file.write('snail')
file.close()