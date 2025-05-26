# import pytest

# from ..account import Account

# acc = Account()

# @pytest.fixture
# def account_created():
#     account = Account("1", "Benjamin", "Berglund", "7008109-2456")
#     return account

# def test_create_account(account_created):
#     assert len(account_created.ssn) == 11 or len(account_created.ssn) == 13
#     assert account_created.account_number is not None
#     assert account_created.account_number != ""

# def test_account_deposit(account_created):
#     # testdata
#     amount_to_deposit = 1000
#     # setup
#     account_created.deposit(amount_to_deposit)
#     assert account_created.balance >=  amount_to_deposit

# def test_account_withdraw(account_created):
#     # testdata
#     account_created.deposit(1000)
#     amount_to_withdraw = 100
#     # setup
#     account_created.withdraw(amount_to_withdraw)
#     print(account_created.balance)
#     assert account_created.balance >= 0

