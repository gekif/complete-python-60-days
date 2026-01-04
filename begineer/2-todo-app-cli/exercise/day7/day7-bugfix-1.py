'''
The code below tries to write the items of temperatures each in one line in the file.txt list.
However, the code has an error. Try to fix the error.

temperatures = [10, 12, 14]
file = open("file.txt", 'w')
file.writelines(temperatures)
'''

temperatures = [10, 12, 14]
file = open("file.txt", 'w')
temperatures = [str(temp) + '\n' for temp in temperatures]
file.writelines(temperatures)
file.close()