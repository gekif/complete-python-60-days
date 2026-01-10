"""
Define a function named get_age  which:
(1) has two parameters, year_of_birth and current_year
(2) the current_year  parameter should be a default parameter
(3) the default value of current_year should be the current year (e.g., the integer 2025)
(4) the function should calculate and return the age of the user given the year_of_birth and the current_year.
"""

def get_age(year_of_birth, current_year=2026):
    age = current_year - year_of_birth
    return age

# Example usage:
age = int(input("Enter your year of birth: "))
calculated_age = get_age(age)

# validate if result cannot be negative and if input not reasonable, continue until valid input is given
while calculated_age < 0 or age < 1900 or age > 2026:
    print("Invalid year of birth. Please enter a valid year.")
    age = int(input("Enter your year of birth: "))
    calculated_age = get_age(age)

print(f"You are {calculated_age} years old.")