'''
Your task for this exercise is to:
(1) define a function named liters_to_m3
(2) the function should take a liters parameter
(3) in the function you should converts liters to cubic meters (1000 liters = 1 cubic meters)
(4) then, return the cubic meters.

Note: Defining the function is enough. You do not need to call or print out a function output,
but you should name the function exactly liters_to_m3.
'''

def liters_to_m3(liters):
    cubic_meters = liters / 1000
    return cubic_meters

# Example usage:
result = liters_to_m3(5000)
print(result)  # Output: 5.0