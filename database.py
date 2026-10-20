
import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")

# Create a cursor
cursor = conn.cursor()

# Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

# Save changes
conn.commit()

# Close connection
conn.close()

print("Database created successfully!")
