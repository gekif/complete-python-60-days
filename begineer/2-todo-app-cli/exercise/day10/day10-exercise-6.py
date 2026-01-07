'''
This exercise is similar to the previous one but with an added feature. In the coding area we have defined a list of filenames. Your task is to:
(1) loop over the list
(2) print out the filename of each item without the extension using slicing and with the first letter capitalized.

The output of your program would look like this:
Report
Downloads
Success
Folders
'''

filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]

for filename in filenames:
    print(filename[:-4].capitalize())