'''
The code below tries to write the string "100.2" to the text file.
However, there is an error. Try to fix the error.

file = open("data.txt", 'r')
file.write("100.12")
file.close()
'''

file = open("data.txt", 'w')
file.write("100.12")
file.close()