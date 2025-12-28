'''
(1) iterates over the list of usernames,
(2) replaces the white space " " of each username with an underscore "_",
(3) prints out the updated username in each iteration.
'''

usernames = ['the blueman', 'sorted hedgehog', 'infinite lagoon']

for username in usernames:
    username = username.replace(" ", "_")
    print(username)