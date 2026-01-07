'''
Change the program, so it prints out "zen is not in the list" instead of returning an error when the user enters "zen" or any other name that is not in the list.
'''
try:
    waiting_list = ["john", "marry"]
    name = input("Enter name: ")

    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")

except ValueError:
    print(f"{name} is not on the waiting list.")