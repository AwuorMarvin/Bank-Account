import unittest
from bank_account import BankAccount

class BankAccountClassTest(unittest.TestCase):
    """docstring for BankAccountClassTest"""

    def test_subclass_instance(self):
        account1 = BankAccount()
        self.assertIsInstance(account1, BankAccount, msg='The object should be an instance of the `BankAccount` class')