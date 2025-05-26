import pytest
from account import Account
from bank import Bank
from customer import Customer
from db import Db
from db import init_db, SessionLocal 
from models import Customer, Account
    
def test_customer_and_account():
    init_db()
    db = SessionLocal()
    
    customer = Customer(name= "Maggie", ssn="9002012288")
    db.add(customer)
    db.commit()
    
    account = Account(number="12345678", balance=200, currency='SEK', customer_id=customer.id)
    db.add(account)
    db.commit() 
    
    print(f"{customer.name} har saldo {account.balance}")
    db.close()
    
if __name__ == "__main__":
    test_customer_and_account()
    
def test_deposit_and_withdraw():
    init_db()
    db = SessionLocal()
    
    Bank = bank
    