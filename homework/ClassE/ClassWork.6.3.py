
import unittest
from unittest.mock import patch, MagicMock
from banking_system import BankingSystem


class TestBankingSystem(unittest.TestCase):
    def setUp(self):
        self.banking_system = BankingSystem()


    def test_create_account(self):
        pass


    def test_close_account(self):
        pass
    def test_get_account_balance(self):
        pass


    # @patch('...')
    # def test_get_customer_credit_score(self, …):
    #     pass


if __name__ == '__main__':
    unittest.main()
