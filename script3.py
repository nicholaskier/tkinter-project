# DATABASES
# sqlite is an embedded databse
# sqlite3
# sqlite wrapper for python
import sqlite3
def create_table():
# connect to DB
    conn=sqlite3.connect("lite.db")
# create cursor object
    cur=conn.cursor()
# apply sql query
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
# commit changes to db
    conn.commit()
# close connection
    conn.close()

def insert(item, quantity, price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, price))
    conn.commit()
    conn.close()

insert("butt", 8, 5)

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    # don't need to commit because you're not adding data
    conn.close()
    return rows

def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()
    
def update(quantity,price,item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()


update(11,6,"water glass")
# delete("Wine Glass")
print(view())