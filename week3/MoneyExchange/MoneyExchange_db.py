import os
import sqlite3

class MoneyExchangeDB:
    def __init__(self, db_name):
      print("Database path:",os.path.abspath(db_name))
      self.conn = sqlite3.connect(db_name)
      self.cursor = self.conn.cursor()
    # self.cursor.execute("PRAGMA table_info('currency')")
      print(self.cursor.fetchall())
    
   
# Create tables into the database 
    def create_tables(self):
        print("Creating tables...") 
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        Create table if not exists Customers(
        cust_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        acc_number TEXT NOT NULL,
        create_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
            """)
        print("Customers table created successfully.")
        self.cursor.execute("""
        Create table if not exists Currency(
        cur_id INTEGER PRIMARY KEY AUTOINCREMENT,
        cur_name TEXT NOT NULL,
        cur_type TEXT NOT NULL,
        active BOOLEAN NOT NULL
         )
            """)
        print("Currency table created successfully.")

        self.cursor.execute("""
        Create table if not exists ExchangeRate(
        exr_id INTEGER PRIMARY KEY AUTOINCREMENT,
        cur_id_from INTEGER NOT NULL,
        cur_id_to INTEGER NOT NULL,
        rate REAL NOT NULL,
        trans_type TEXT NOT NULL,
        effective_time DATETIME NOT NULL,
        create_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (cur_id_from) REFERENCES Currency(cur_id),
        FOREIGN KEY (cur_id_to) REFERENCES Currency(cur_id)
        )
        """)
        print("ExchangeRate table created successfully.")   

        self.cursor.execute("""
        Create table if not exists CurTransaction(
        tran_id INTEGER PRIMARY KEY AUTOINCREMENT,
        cust_id INTEGER NOT NULL,
        cur_id_from INTEGER NOT NULL,
        cur_id_to INTEGER NOT NULL,
        txn_datetime DATETIME NOT NULL,
        amount_from REAL NOT NULL,
        amount_to REAL NOT NULL,
        ex_rate_used REAL NOT NULL,
        acc_id TEXT NOT NULL,
        remark TEXT,
        FOREIGN KEY (cust_id) REFERENCES Customers(cust_id),
        FOREIGN KEY (cur_id_from) REFERENCES Currency(cur_id),
        FOREIGN KEY (cur_id_to) REFERENCES Currency(cur_id)
        )
        """)
        
        print("Transaction table created successfully.")
        self.conn.commit()
        print("All tables created successfully.")
