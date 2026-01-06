'''
Fix the program below so it prints out "OK"
when the perimeter is less than 14 and the area is less than 8.

length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = (length + width) * 2
area = length * width

print("Perimeter is", perimeter)
print("Area is", area)

if perimeter < 14 and area > 10:
    print("OK")
else:
    print("NOT OK")
'''


length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = (length + width) * 2
area = length * width

print("Perimeter is", perimeter)
print("Area is", area)

if perimeter < 14 and area > 8:
    print("OK")
else:
    print("NOT OK")