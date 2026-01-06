'''
The program below intends to find out how many items have at least
one underscore ("_") character in them.
However, there is an error with the code. Try to find and fix it.

ids = ["XF345_89", "XER76849", "XA454_55"]

x = 0

for id in ids:
if '_' in id:
    x = x + 1
print(x)
'''

ids = ["XF345_89", "XER76849", "XA454_55"]

x = 0

for id in ids:
    if '_' in id:
        x = x + 1

print(x)