import csv

# Example of reading a CSV file and printing all temperatures with their stations

# with open('weather.csv', 'r') as csvfile:
#     csvreader = csv.reader(csvfile)
#     header = next(csvreader)  # Skip the header row
#     for row in csvreader:
#         station, temperature = row
#         print(f"Temperature: {temperature}, Station: {station}")


# Example of searching for a specific city's temperature
city = input("Enter city name: ")

with open('weather.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row
    found = False
    for row in csvreader:
        station, temperature = row
        if station.lower() == city.lower():
            print(f"The temperature in {station} is {temperature}")
            found = True
            break
    if not found:
        print(f"City {city} not found in the data.")