import MoneyExchange_db

class db_op:
    def __init__(self):
        self.db = MoneyExchange_db.MoneyExchangeDB("money_exchange.db")
        self.db.create_tables()
    def insert_customer(self, customer_name, acc_number):
        self.db.cursor.execute("INSERT INTO Customers (customer_name, acc_number) VALUES (?, ?)", (customer_name, acc_number))
        self.db.conn.commit()
    def insert_currency(self, cur_name, cur_type, active):

        # self.db.cursor.execute("PRAGMA database_list")
        # print(self.db.cursor.fetchall())

        # self.db.cursor.execute("PRAGMA table_info(Currency)")
        # print(self.db.cursor.fetchall())

        
        self.db.cursor.execute("INSERT INTO Currency (cur_name, cur_type, active) VALUES (?, ?, ?)", (cur_name, cur_type, active))
        self.db.conn.commit()
    def insert_exchange_rate(self, cur_id_from, cur_id_to, rate, trans_type, effective_time):
        self.db.cursor.execute("INSERT INTO ExchangeRate (cur_id_from, cur_id_to, rate, trans_type, effective_time) VALUES (?, ?, ?, ?, ?)", (cur_id_from, cur_id_to, rate, trans_type, effective_time))    
        self.db.conn.commit()
    def insert_transaction(self, cust_id, cur_id_from, cur_id_to, txn_datetime, amount_from, amount_to, ex_rate_used, acc_id, remark):
        self.db.cursor.execute("INSERT INTO CurTransaction (cust_id, cur_id_from, cur_id_to, txn_datetime, amount_from, amount_to, ex_rate_used, acc_id, remark) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (cust_id, cur_id_from, cur_id_to, txn_datetime, amount_from, amount_to, ex_rate_used, acc_id, remark))
        self.db.conn.commit()
    def customers_number(self):
        self.db.cursor.execute("SELECT COUNT(*) FROM Customers")
        number = self.db.cursor.fetchone()[0]
        print("Number of customers:", number)
        return number
    def transactions_number(self):
        self.db.cursor.execute("SELECT COUNT(*) FROM CurTransaction")
        number = self.db.cursor.fetchone()[0]
        print("Number of transactions:", number)
        return number
    def close_connection(self):
        self.db.conn.close()

