'''
Complete the function given in the coding area. The function should:
(1) calculate the maximum value of the grades list,
(2) return the calculated value.

After completing the function definition you should call the function and print out its output.
The output of your code would be:
9.7
'''

def get_max():
    grades = [9.6, 9.2, 9.7]
    max_grade = max(grades)
    return max_grade

print(get_max())
