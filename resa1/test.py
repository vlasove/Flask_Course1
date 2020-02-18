import sqlite3

conn = sqlite3.connect("data.db")
cur = conn.cursor()

create_query = "CREATE TABLE IF NOT EXISTS books (id INT, name TEXT, author TEXT)"
cur.execute(create_query)

insert_query = "INSERT INTO books VALUES(?, ?, ?)"
for i in range(1, 4000):
    cur.execute(insert_query, (i, "petya", "dock"))
conn.commit()

select_query = "SELECT * FROM books"
for row in cur.execute(select_query):
    print(row)

update_query = "UPDATE books SET author= ? WHERE id = 3999"
cur.execute(update_query, ("bobby",))
select_query = "SELECT * FROM books"
for row in cur.execute(select_query):
    print(row)
conn.close()