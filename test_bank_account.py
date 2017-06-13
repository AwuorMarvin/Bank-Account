import unittest
from bank_account import BankAccount, LeastBalance

class BankAccountClassTest(unittest.TestCase):
    """docstring for BankAccountClassTest"""

    def test_subclass_instance(self):
        account1 = BankAccount()
        self.assertIsInstance(account1, BankAccount, msg='The object should be an instance of the `BankAccount` class')

    def test_balance(self):
        account1 = BankAccount()
        self.assertEqual(account1.account_balance, 500)

    def test_deposit(self):
        account1 = BankAccount()
        account1.deposit(3400)
        self.assertEqual(account1.account_balance, 3900)

    def test_withdraw(self):
        account1 = BankAccount()
        account1.withdraw(100)
        self.assertEqual(account1.account_balance, 400)

    def test_invalid_transaction(self):
        account1 = BankAccount()
        self.assertEqual(account1.withdraw(1000), "Your account balance is insufficient")

    def test_sub_class(self):
        account1 = BankAccount()
        self.assertTrue(issubclass(LeastBalance, BankAccount))
