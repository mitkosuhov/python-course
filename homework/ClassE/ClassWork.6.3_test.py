
import unittest
from unittest.mock import patch, MagicMock
from homework.ClassE.banking_system import BankingSystem


class TestBankingSystem(unittest.TestCase):
    def setUp(self):
        self.banking_system = BankingSystem()


    def test_create_account(self):
        self.banking_system.create_account('12345', initial_balance=100)
        self.assertIn('12345', self.banking_system.accounts)
        self.assertEqual(self.banking_system.accounts['12345'].balance, 100)

        pass


    def test_close_account(self):
        self.banking_system.create_account('12345', initial_balance=100)
        self.banking_system.close_account('12345')
        self.assertNotIn('12345', self.banking_system.accounts)

        pass

    def test_get_account_balance(self):
        self.banking_system.create_account('12345', initial_balance=500)
        balance = self.banking_system.get_account_balance('12345')
        self.assertEqual(balance ,500)

        pass


    @patch('requests.get')
    def test_get_customer_credit_score(self,mock_request_get):

        mock_request_get.return_value.status_code = 200
        mock_request_get.return_value.json.return_value = {'credit_score': 1}

        credit_score = self.banking_system.get_customer_credit_score('123')
        self.assertEqual(1, credit_score)
        

    @patch('requests.get')
    def test_get_customer_credit_score_when_not_200(self,mock_request_get):

        mock_request_get.return_value.status_code = 201

        credit_score = self.banking_system.get_customer_credit_score('123')
        self.assertIsNone(credit_score)

    @patch('requests.get')
    def test_get_customer_credit_score_when_not(self,mock_request_get):
        mock_request_get.return_value.status_code = 200
        mock_request_get.return_value.json.return_value = {'credit_score': 1}

        # self.banking_system.get_customer_credit_score(1)

        self.assertEqual(1, self.banking_system.get_customer_credit_score(1))


if __name__ == '__main__':
    unittest.main()
