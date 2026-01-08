'''
Your task for this exercise is to:
(1) define a function named format_filename
(2) define a variable named filename inside the function
(3) assign the string "report.txt" to filename
(4) remove the last four characters (.txt)
from the filename string and capitalize its first letter.
(5) return the altered string.
(6) call the function and print out its output.
'''

def format_filename():
    filename = "report.txt"
    modified_filename = filename[:-4].capitalize()
    return modified_filename

print(format_filename())