import sqlite3



class Database:

    def __init__(self):
        print("Class method called")
        pass


    def create_table(self): 
        self.con = sqlite3.connect('bot_database.db')
        self.execute('CREATE TABLE db(item, trade, cancellations, price, discount, date, time)')



# db = Database()