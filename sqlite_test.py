import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id TEXT, name TEXT, wins INTEGER)")

conn.commit()
print("table created!")

cursor.execute("INSERT INTO users VALUES (?, ?, ?)", ("kuro123", "kuro", 0))
conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print(rows)