'''
In the coding area there is a story.txt file tab that contains some text. Your task is to make a copy of the story.txt file. Here are the exact steps:
(1) Read the story.txt file using a with-context manager and store its text in a string variable.
(2) Create a new story_copy.txt file using a second with-context and write the string variable in the file.
'''

with open("story.txt", "r") as original_file:
    story_text = original_file.read()

with open("story_copy.txt", "w") as copy_file:
    copy_file.write(story_text)