# Money Exchange System — UML Class Diagram

```mermaid
classDiagram

    class Person {
        <<abstract>>
        +String name
        +String email
        +String phoneNumber
    }

    class Customer {
        <<entity>>
        +String custId
        +DateTime createdAt
        +openAccount(currency) Account
        +requestExchange(sourceAccount, targetAccount, amount) ExchangeTransaction
        +viewTransactions() List~ExchangeTransaction~
    }

    class Administrator {
        <<entity>>
        +String adminId
        +updateCurrency(currency) void
        +updateExchangeRate(rate) void
        +viewUserActions() List~ExchangeTransaction~
    }

    class Account {
        <<entity>>
        +int accId
        +String accNum
        +Decimal balance
        +boolean active
        +DateTime createdAt
        +deposit(amount) void
        +withdraw(amount) boolean
        +getBalance() Decimal
    }

    class Currency {
        <<entity>>
        +String curType
        +String curName
        +boolean active
        +activate() void
        +deactivate() void
    }

    class ExchangeTransaction {
        <<entity>>
        +int tranId
        +DateTime txnDateTime
        +Decimal amountFrom
        +Decimal amountTo
        +Decimal exRateUsed
        +String remarks
        +calculateAmount(rate) Decimal
        +complete() void
        +addRemark(text) void
    }

    class ExchangeRate {
        <<entity>>
        +int exrId
        +String curTypeFrom
        +String curTypeTo
        +Decimal rate
        +String transType
        +DateTime effectiveTime
        +DateTime createdAt
        +isEffective(at) boolean
        +convert(amount) Decimal
        +updateRate(newRate, effectiveTime) void
        +deferUpdate(newEffectiveTime) void
    }

    Customer --|> Person : inherits
    Administrator --|> Person : inherits

    Customer "1" --> "0..*" Account : owns
    Account "0..*" --> "1" Currency : denominated in

    Customer "1" --> "0..*" ExchangeTransaction : makes
    ExchangeTransaction "0..*" --> "1" Account : source account
    ExchangeTransaction "0..*" --> "1" Account : target account
    ExchangeTransaction ..> ExchangeRate : calculates with

    ExchangeRate "0..*" --> "1" Currency : source currency
    ExchangeRate "0..*" --> "1" Currency : target currency

    Administrator ..> Currency : manages
    Administrator ..> ExchangeRate : manages
    Administrator ..> ExchangeTransaction : monitors

    note for Person "Shared personal information is inherited by Customer and Administrator."
    note for Customer "custId is a customer-specific identifier."
    note for Administrator "adminId is an administrator-specific identifier."
    note for Account "Each account is denominated in exactly one currency; balance uses that currency."
    note for ExchangeTransaction "exRateUsed preserves the exchange-rate snapshot applied to the transaction."
```

## Class

- **Person:** An abstract superclass that stores personal information shared by customers and administrators, including name, email address, and phone number.
- **Customer:** Represents a customer who can open accounts, request currency exchanges, and view transaction history. `custId` is the customer-specific identifier.
- **Administrator:** Represents an administrator who maintains currencies and exchange rates and monitors customer transactions. `adminId` is the administrator-specific identifier.
- **Account:** Represents a customer's currency account. It stores the account number, balance, status, creation time, and provides deposit, withdrawal, and balance-checking operations.
- **Currency:** Represents a currency supported by the system, such as NZD, USD, or CNY. It stores the currency code, currency name, and active status.
- **ExchangeTransaction:** Represents a completed or in-progress currency exchange between a source account and a target account. It records the exchanged amounts, applied exchange-rate snapshot, transaction time, and remarks.
- **ExchangeRate:** Represents the exchange rate from one currency to another. It records the rate, transaction type, effective time, and creation time and provides operations for conversion and rate updates.

## Class-relationship

- **Inheritance:** `Customer` and `Administrator` inherit the shared personal attributes from the abstract `Person` class.
- **Customer–Account association:** One `Customer` can own zero or more `Account` objects, while each `Account` belongs to exactly one customer.
- **Account–Currency association:** Each `Account` is denominated in exactly one `Currency`, while one currency can be used by zero or more accounts. The account balance is expressed in that currency.
- **Customer–ExchangeTransaction association:** One `Customer` can make zero or more `ExchangeTransaction` objects, while each transaction is associated with exactly one customer.
- **ExchangeTransaction–Account associations:** Each `ExchangeTransaction` has exactly one source account and one target account. An account can participate in zero or more transactions.
- **ExchangeTransaction–ExchangeRate dependency:** An `ExchangeTransaction` uses an `ExchangeRate` to calculate the target amount. The transaction retains `exRateUsed` as a historical snapshot.
- **ExchangeRate–Currency associations:** Each `ExchangeRate` has one source currency and one target currency. A currency can participate in multiple exchange-rate records.
- **Administrator dependencies:** An `Administrator` manages `Currency` and `ExchangeRate` objects and monitors `ExchangeTransaction` records.
