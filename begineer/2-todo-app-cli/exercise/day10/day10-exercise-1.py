'''
Take a look at the code in the coding area. You should expand that code. Your task is to:
(1) calculate the percentage using the  value/total * 100 formula
(2) print out the message "That is 40.0%" (or whatever the calculated percentage value is)
'''

try:
    total_value = int(input("Enter the total value: "))
    value = int(input("Enter the value: "))

    percentage = (value / total_value) * 100
    print(f"That is {percentage}%")

except ValueError:
    print("You need to enter a number. Run the program again.")