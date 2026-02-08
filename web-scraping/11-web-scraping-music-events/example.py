import sqlite3

# Establish a Connection and Cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query All Data Based on Condition
cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

# Query Certain Column Based on COndition
cursor.execute("SELECT band, date FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

# Insert New Rows
new_rows = [
    ('Cats', 'Cat City', '2088.10.17'),
    ('Hens', 'Hen City', '2088.10.17'),
]

cursor.executemany("INSERT INTO events VALUES (?,?,?)", new_rows)
connection.commit()

# Query All Data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)



