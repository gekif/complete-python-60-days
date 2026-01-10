"""
Define a function that:
(1) takes the side length of a square as a parameter
(2) calculates and returns the area of a square.

For example, if I was to call your function with foo(7)it would return 49.  You can name the function anyway you want.
"""

def calculate_square_area(side_length):
    area = side_length ** 2
    return area

# Example usage:
side = float(input("Enter the side length of the square: "))
area = calculate_square_area(side)
print(f"The area of the square is {int(area)}.")