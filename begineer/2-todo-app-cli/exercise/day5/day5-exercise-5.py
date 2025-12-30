'''
In the code area we have a list of strings. Your task is to write some code that:
(1) iterates over the filenames list,
(2) adds a number and a dash in front of each string, and .txt at the end using f-strings, and
(3) prints each modified string as shown below.
0-document.txt
1-report.txt
2-presentation.txt
'''

filenames = ["document", "report", "presentation"]

for index, name in enumerate(filenames):
    print(f"{index}-{name}.txt")