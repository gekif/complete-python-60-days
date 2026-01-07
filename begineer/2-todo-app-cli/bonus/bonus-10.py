try:
    width = float(input("Enter the width of the rectangle: "))
    length = float(input("Enter the length of the rectangle: "))

    if width == length:
        print("That looks like square.")
    else:
        area = length * width
        print("Area of the rectangle: ", area)

except ValueError:
    print("Invalid input. Please enter the number for width and length.")