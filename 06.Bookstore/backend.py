import sqlite3

db_path = "06.Bookstore/app/db/books.db"

def connect():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER, ISBN INTEGER)")
    conn.commit()
    conn.close()
connect()

def view_all():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows

def search_entry(title="",author="",year="",ISBN=""):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author = ? OR year = ? OR ISBN = ?",(title,author,year,ISBN))
    conn.close()

def add_entry(title,author,year,ISBN):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title,author,year,ISBN))
    conn.commit()
    conn.close()

def update(id,title,author,year,ISBN):
    conn = sqlite.connect(db_path)
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=?,author=?,year=?,ISBN=? WHERE id=?",(title,author,year,ISBN,id))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def close():
    print("Close")