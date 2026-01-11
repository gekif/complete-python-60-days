"""
In the previous exercise, we hardcoded the values 0 and 100. However, it is better to place those values in constants. Therefore, your task is to:
(1) create a FREEZING_POINT and a BOILING_POINT variable outside of the water_state function and store the values 0 and 100 in them respectively.
(2) modify the function of the previous exercise by using the variables given above instead of the hardcoded 0 and 100 values. The previous function is provided in the coding area.
"""

FREEZING_POINT = 0
BOILING_POINT = 100

def water_state(temperature):
    if temperature <= FREEZING_POINT:
        return "Solid"
    elif temperature < BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"

# Example usage:
temp = input("Enter a temperature in degrees Celsius: ")
state = water_state(float(temp))
print(f"At {temp}°C, water is in the '{state}' state.")