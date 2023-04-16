import sqlite3

# Lost database class modules

class Database:

    def __init__(self):
        print("Class method called")
        pass


    def create_table(self): 
        self.con = sqlite3.connect('bot_database.db')
        self.execute('CREATE TABLE db(item, trade, cancellations, price, discount, date, time)')

    def add_item(self, item, trade, cancellations, price, discount, date, time):
        self.con = sqlite3.connect('bot_database.db')
        self.cur = self.con.cursor()
        self.cur.execute('INSERT INTO db VALUES (?,?,?,?,?,?,?)', (item, trade, cancellations, price, discount, date, time))


    def view_all(self):
        self.con = sqlite3.connect('bot_database.db')
        self.cur = self.con.cursor()
        self.cur.execute('SELECT * FROM db')
        rows = self.cur.fetchall()
        return rows
    
    def del_item(self, item):
        self.con = sqlite3.connect('bot_database.db')
        self.cur = self.con.cursor()
        self.cur.execute('DELETE FROM db WHERE item=?', (item,))
        self.con.commit()



