# Money Exchange System

## Project Overview
This project is a Money Exchange System developed of MSE800 course.
This system is designed for SQL practise.

## ER-diagram



## Techologies
- python
- SQLite

# Main features
- Mangage Customer/transcation/currency information for Money Exchange System

# Dataabases Design 
- Customer
- Currency
- Transaction
- Exchange rate 

## Entity 
CUSTOMER
PK  cust_id
    cust_name
    acc_num
    created_at

TRANSACTION
PK  tran_id
FK  cust_id
FK  cur_type_from
FK  cur_type_to
    txn_datetime
    amount_from
    amount_to
    ex_rate_used
    acc_id (nullable)
    remarks

CURRENCY
PK  cur_type
    cur_name
    active

EXCHANGE_RATE
PK  exr_id
FK  cur_type_from
FK  cur_type_to
    rate
    trans_type
    effective_from
    effective_to
    created_at

## relationship
CUSTOMER
   1
   │
   │ makes
   │
   N
TRANSACTION
   │
   ├── N : 1 ── CURRENCY (from)
   │
   └── N : 1 ── CURRENCY (to)


CURRENCY
   │
   ├── 1 : N ── EXCHANGE_RATE (from)
   │
   └── 1 : N ── EXCHANGE_RATE (to)

## Table Justification
1. Customer Table:
The Customer table include the customer information include ID, name and account number.It is necessary because one customer can do multiple exchange transactions. 

2. Currency Table:
This table store the currencies supported by the money exchange content, such as NZD, USD and CNY. It provides a consistent reference for currencies.

3. Exchange_rate Table:
This table stores exchange between two currencies. It is necessary because exchange rates change over time. Keeping exchange rates in a separate table allows the system to maintain rate history and identify the source currency, target currency, and applicable rate

4. Transaction Table:
This table records each currency exchange transaction. It connects the customer with the source and target currencies and stores the exchanged amount,exchange rate,and transaction time. It is necessary for tracking the complete history of the exchange business.


## How to run 
1. clone or download the project
2. open the project 
3. Active python environment
4. Run.

## Author
Leon Wu




