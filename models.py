from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Numeric


Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers" 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    phone = Column(String)
    personnummer = Column(String, unique=True)
    accounts = relationship('Account', back_populates='customer')
    
class Account(Base):
    __tablename__ = "accounts" 
    id = Column(Integer, primary_key=True)
    number = Column(String, nullable=False)
    balance = Column(Numeric, nullable=False)
    credit = Column(Numeric, default=0)
    interest = Column(Numeric, default=0)
    currency = Column(String(3), nullable=False)
    
    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="accounts")

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    timestamp = Column(String)
    amount = Column(Numeric)
    currency = Column(String)
    sender_account_id = Column(Integer, ForeignKey('accounts.id'))
    receiver_account_id = Column(Integer, ForeignKey('accounts.id'))
    sender_country = Column(String)
    sender_municipality = Column(String)
    receiver_country = Column(String)
    receiver_municipality = Column(String)
    transaction_type = Column(String)
    notes = Column(String)

    sender_account = relationship("Account", foreign_keys=[sender_account_id])
    receiver_account = relationship("Account", foreign_keys=[receiver_account_id])