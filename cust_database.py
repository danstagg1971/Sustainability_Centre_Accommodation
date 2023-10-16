import sqlite3

class CustomerDatabase:
    def __init__(self):
        self.con = sqlite3.connect("cust_database.db")
        self.cur = self.con.cursor()
        self.create_table()


    def create_table(self):
        # self.cur.execute("""DROP TABLE products""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS customers(
        date,
        firstname TEXT,
        surname TEXT,
        email TEXT,
        phone TEXT
        )""")

    def insert(self, item1):
        self.cur.execute("""INSERT OR IGNORE INTO customers VALUES(?,?,?,?,?)""", item1)
        self.con.commit()

    def read(self):
        self.cur.execute("""SELECT * FROM customers""")
        rows = self.cur.fetchall()
        return rows
