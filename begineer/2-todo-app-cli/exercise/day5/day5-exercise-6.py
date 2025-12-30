'''
Similar to the previous exercise, we have a list of three strings defined in the code area. Your task is to:
(1) iterate over the filenames list,
(2) capitalize the first letter of each string,
(3) add a number and a dash in front of each string, and .txt at the end, and
(4) print each modified string as shown below.
0-Document.txt
1-Report.txt
2-Presentation.txt

Notice the first letter of each string is capitalized.
'''

filenames = ["document", "report", "presentation"]

for index, name in enumerate(filenames):
    print(f"{index}-{name.capitalize()}.txt")