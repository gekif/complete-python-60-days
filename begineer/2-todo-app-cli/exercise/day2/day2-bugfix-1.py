'''
Create a program that:
(1) prompts the user to input their name,
(2) prints out the name with the first letter capitalized,
(3) keeps prompting the user to input another name
(4)  prints out the name with the first letter capitalized,
(5) The process is repeated infinitely.
'''

while True:
    name = input("What is your name? ")
    print(name.capitalize())
