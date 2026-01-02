'''
1. reads each text file and
2. prints out the content of each file in the command line.
The expected output would be like the following:
'''
filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(f"exercise10files\\{filename}", 'r')
    content = file.read()
    print(content)