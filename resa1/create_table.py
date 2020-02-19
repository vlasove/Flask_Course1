import sqlite3 

conn = sqlite3.connect("data.db")
cur = conn.cursor()

query_items = "CREATE TABLE IF NOT EXISTS items (name TEXT PRIMARY KEY, price REAL)"
cur.execute(query_items)
query_users = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
cur.execute(query_users)


conn.commit()
conn.close()