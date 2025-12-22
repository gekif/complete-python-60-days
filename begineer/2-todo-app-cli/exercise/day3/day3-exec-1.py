'''
In the coding area, we have defined a country variable.  Below that line, write a match-case block that:
(1) checks the value of the country variable, and
(2) prints out Hello if the value of country is "USA"
(3) prints out Ciao if the value of country is "Italy",
(4) prints out Hallo if the value of country is "Germany".
'''

country = input("Enter the country: ")

match country:
    case "USA":
        print("Hello")
    case "Italy":
        print("Ciao")
    case "Germany":
        print("Hallo")
    case _:
        print("Please enter a valid country")