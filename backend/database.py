import mysql.connector

# Connect to the MySQL server
connection = mysql.connector.connect(
    host="localhost",       # or your DB server address
    user="your_username",   # e.g., "root"
    password="your_password",
    database="your_database_name"
)

# Create a cursor to execute queries
cursor = connection.cursor()

# Example query
cursor.execute("SELECT * FROM users")

# Fetch and print results
results = cursor.fetchall()
for row in results:
    print(row)

# Clean up
cursor.close()
connection.close()