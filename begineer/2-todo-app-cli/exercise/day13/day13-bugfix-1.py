"""
Given the above information, we have created a program that calculates the free-fall time given the free-fall distance h and the gravity g which will be a default parameter with a value of 9.80665:

def calculate_time(g=9.80665, h):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)
However, the script produces an error. Try running the script in your IDE and then fix the error so the program successfully calculates the free-fall time.
"""


def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t

time = calculate_time(100)
print(time)