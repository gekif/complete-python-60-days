'''
In the coding area, we have defined a list of languages. Add some code that:
(1) iterates over the list using a for-loop,
(2) creates a new text file in each iteration using a with-context manager,
(3) each file should be named according to the current item (i.e., English.txt, German.txt, and Spanish.txt).
(4) the content of each file should be the item of the list (e.g., the content of the file English.txt should be English).
'''

languages = ["English", "German", "Spanish"]

for language in languages:
    with open(f"{language}.txt", "w") as file:
        file.write(language)