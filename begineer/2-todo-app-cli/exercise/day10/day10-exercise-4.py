'''
Your task for this exercise is to:
(1) loop over the passwords list and
(2) print out only those passwords that are less than 8 characters.
'''

passwords = ["acasd9983k", "34aiufaac99", "98jjanf", "afjj879"]

for password in passwords:
    if len(password) < 8:
        print(password)