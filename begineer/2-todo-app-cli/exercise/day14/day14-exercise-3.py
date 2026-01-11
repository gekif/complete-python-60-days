"""
Define a function that:
(1) takes temperature as a parameter
(2) returns "Hot" if the temperature is greater than 25
(3) returns "Warm" if the temperature is between 15 and 25, including 15 and 25.
(4) returns "Cold" if the temperature is less than 15.

If I called your function with foo(10) it would return "Cold".

Calling it with foo(15), foo(16), or foo(25) would all return "Warm". Calling it with foo(26) would return "Hot".
"""

def temperature_feeling(temperature):
    if temperature > 25:
        return "Hot"
    elif 15 <= temperature <= 25:
        return "Warm"
    else:
        return "Cold"

# Example usage:
temp = input("Enter a temperature in degrees Celsius: ")
feeling = temperature_feeling(float(temp))
print(f"At {temp}°C, the feeling is '{feeling}'.")