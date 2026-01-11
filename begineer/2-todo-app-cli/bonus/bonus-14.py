from converter14 import convert_to_inches
from parser14 import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)
result = convert_to_inches(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result} meters")

if result < 1:
    print("Kid to small")
else:
    print("kid can use slide")