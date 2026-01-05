date = input("Enter today's date: ")
mood = input("How do you rate your mood today on a scale of 1-10? ")
thoughts = input("Let your thoughts: ")

# create program that input today mood and thoughts and write them to a file named with today's date save it on journal folder on the same place with context manager

with open(f"journal/{date}.txt", 'w') as file:
    file.write(f"Mood: {mood}\n")
    file.write("Thoughts:\n")
    file.write(thoughts)