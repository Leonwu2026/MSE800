# Week 3 - Activity 5: Money Exchange Project with Database - due date 22.8.26 at 8:00 AM
# Design ER diagram and develop a database for the money exchange project (with at least three entities and OOP style). In a README file, clearly describe how many tables you have created and justify why each table is necessary. Once completed, share the link to your GitHub repository. 
# Project scope: The Money Exchange System should allow a exchange business to manage customers, currencies, exchange rates, and currency exchange transactions

import db_op
import MoneyExchange_db

def main(): 
    db_operations = db_op.db_op()
    print("Database operations initialized.")

    db_operations.insert_customer("Tom", "100")
    db_operations.insert_customer("Jack", "200")
    db_operations.insert_customer("Jerry", "300")
    db_operations.insert_customer("Alice", "400")
    print("Customers inserted successfully.")
    db_operations.insert_currency("USD", "Dollar", 1)
    db_operations.insert_currency("EUR", "Euro", 1)
    db_operations.insert_currency("JPY", "Yen", 1)
    print("Currencies inserted successfully.")
    db_operations.insert_exchange_rate(1, 2, 1.2, 'buy', '2024-01-01 00:00:00')
    db_operations.insert_exchange_rate(2, 1, 0.8, 'sell', '2024-02-01 00:00:00')
    db_operations.insert_exchange_rate(1, 3, 110.0, 'buy', '2024-03-01 00:00:00')
    print("Exchange rates inserted successfully.")
    db_operations.insert_transaction(1, 1, 2, '2024-01-01 10:00:00', 100.0, 120.0, 1.2, 'ACC001', 'First transaction')
    db_operations.insert_transaction(2, 2, 1, '2024-02-01 11:00:00', 200.0, 160.0, 0.8, 'ACC002', 'Second transaction')
    db_operations.insert_transaction(3, 1, 3, '2024-03-01 12:00:00', 300.0, 33000.0, 110.0,'ACC003', 'Third transaction')
    db_operations.insert_transaction(4, 3, 1, '2024-04-01 13:00:00', 400.0, 3.636, 0.0091, 'ACC004', 'Fourth transaction')
    print("Transactions inserted successfully.")
    db_operations.customers_number()
    db_operations.transactions_number()
    db_operations.close_connection()

    db_operations.close_connection()    

if __name__ == "__main__":
    main()
    
