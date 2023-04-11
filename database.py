import sqlite3

# Lost database class modules

class Database:

    def __init__(self):
        print("Class method called")
        pass


    def create_table(self): 
        self.con = sqlite3.connect('bot_database.db')
        self.execute('CREATE TABLE db(item, trade, cancellations, price, discount, date, time)')

    # Untested, not sure if working. Ive written this part but the rebase erased it.
    #    I must re-write this part.

    # def store_api_key(self, api_key):
    #     self.con = sqlite3.connect('bot_database.db')
    #     self.execute('INSERT INTO db VALUES(api_key)')

    # def select_api_key(self):
    #     self.con = sqlite3.connect('bot_database.db')
    #     self.execute('SELECT * FROM db')

    



