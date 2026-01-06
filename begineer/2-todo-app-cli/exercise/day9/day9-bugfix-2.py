'''
This program also intends to find out how many items have an underscore in them. However, the program has a bug. It doesn't return an error message, but it returns:

1
1
2
Instead, the expected output is:

2

Try to fix the program so it returns the expected output. Here is the buggy program:

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