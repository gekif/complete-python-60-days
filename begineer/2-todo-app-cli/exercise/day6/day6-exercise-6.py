'''
In the coding area, we have defined two lists.
Each country in the first list should be written in a new file corresponding to the name in the filenames list.
 So, "Albania" should be written in a new a.txt file, "Belgium" in a new "b.txt" file and so on.
'''

countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']

for country, filename in zip(countries, filenames):
    file = open(filename, 'w')
    file.write(country)
    file.close()