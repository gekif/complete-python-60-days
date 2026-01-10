feet_inches = input("Enter feet and inches: ")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches

def convert_to_inches(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

f, i = parse(feet_inches)
result = convert_to_inches(f, i)

if result < 1:
    print("Kid to small")
else:
    print("kid can use slide")