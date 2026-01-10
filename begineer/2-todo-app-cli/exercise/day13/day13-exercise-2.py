"""
Write a get_nr_items function that:
(1) gets as a parameter one string with commas (e.g., "john,lisa, teresa")
(2) the function calculates the number of words (i.e., three words in the above example)
(3) returns the number of words.

For example, if I called your function with get_nr_items("john,lisa, teresa") it would return 3.
"""

def get_nr_items(items_string):
    # Split the string by commas and strip any extra whitespace
    items_list = [item.strip() for item in items_string.split(',')]
    # Return the number of items
    return len(items_list)

# Example usage:
input_string = input("Enter items separated by commas: ")
number_of_items = get_nr_items(input_string)
print(f"You have {number_of_items} items.")