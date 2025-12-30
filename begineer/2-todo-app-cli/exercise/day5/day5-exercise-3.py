'''
(1) iterates over the list items,
(2) prints out the index of each item, a colon ":", and the item.

Here is how the output should look like:
0 : table
1 : chair
2 : door
'''

furniture = ["table", "chair", "door"]

for index, item in enumerate(furniture):
    print(f"{index} : {item}")