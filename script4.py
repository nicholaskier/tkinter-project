import psycopg2

def create_table():
# connect to DB
    conn=psycopg2.connect("dbname='Database1' user='postgres' password='postgres123' host='localhost' port='5432'")
# create cursor object
    cur=conn.cursor()
# apply sql query
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
# commit changes to db
    conn.commit()
# close connection
    conn.close()

def insert(item, quantity, price):
    conn=psycopg2.connect("dbname='Database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES ('%s','?%s,'%s')" % (item, quantity, price))
    # or
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item,quantity,price))
    conn.commit()
    conn.close()

# insert("butt", 8, 5)

def view():
    conn=psycopg2.connect("dbname='Database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    # don't need to commit because you're not adding data
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='Database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()
    
def update(quantity,price,item):
    conn=psycopg2.connect("dbname='Database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()

create_table()
insert("Apple",10,5)
# update(11,6,"water glass")
# delete("Wine Glass")
# print(view())