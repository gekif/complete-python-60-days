feet_inches = input("Enter feet and inches: ")

def convert_to_inches(feet_inches):
    try:
        feet, inches = feet_inches.split()
        feet = float(feet)

        inches = float(inches)
        meters = feet * 0.3048 + inches * 0.0254
        return meters
    except ValueError:
        return "Invalid input. Please enter feet and inches separated by a space."

result = convert_to_inches(feet_inches)
# print(result)

if result < 1:
    print("Kid to small")
else:
    print("kid can use slide")