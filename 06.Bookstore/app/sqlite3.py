import sqlite3

def create_table():
    conn = sqlite3.connect("06.Bookstore/app/db/test.db") #1 Connect to database
    cur = conn.cursor() #2 Create a cursor object
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") #3 Write SQL query
    conn.commit() #4 Commit changes to db
    conn.close() #5 Close connection


def insert(item,quantity,price):
    conn = sqlite3.connect("06.Bookstore/app/db/test.db") #1 Connect to database
    cur = conn.cursor() #2 Create a cursor object
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price)) #3 Write SQL query
    conn.commit() #4 Commit changes to db
    conn.close() #5 Close connection

def view():
    conn = sqlite3.connect("06.Bookstore/app/db/test.db") #1 Connect to database
    cur = conn.cursor() #2 Create a cursor object
    cur.execute("SELECT * FROM store") #3 Write SQL query
    rows = cur.fetchall()
    conn.close() #5 Close connection
    return rows

print(view())

def delete(item):
    conn = sqlite3.connect("06.Bookstore/app/db/test.db") #1 Connect to database
    cur = conn.cursor() #2 Create a cursor object
    cur.execute("DELETE FROM store WHERE item=?",(item,)) #3 Write SQL query
    conn.commit() #4 Commit changes to db
    conn.close() #5 Close connection

def update(item,quantity, price) :
    conn = sqlite3.connect("06.Bookstore/app/db/test.db") #1 Connect to database
    cur = conn.cursor() #2 Create a cursor object
    cur.execute("UPDATE store SET quantity=?, price=?, WHERE item=?",(quantity,price,item)) 
    cur.commit()
    conn.close() #5 Close connection

#create_table()
#insert('Phone',50,150)
#insert('Book',2,10.5)
#delete('Phone')