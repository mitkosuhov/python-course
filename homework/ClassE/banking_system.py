# banking_system.py
import requests


class ExternalCreditService:
    def get_credit_score(self, customer_id):
        # Simulate HTTP request to external service
        response = requests.get(f"https://example.com/credit-score?customer_id={customer_id}")
        if response.status_code == 200:
            return response.json()['credit_score']
        else:
            return None


class Account:
    def __init__(self, account_id, initial_balance=0):
        self.account_id = account_id
        self.balance = initial_balance


    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")


class BankingSystem:
    def __init__(self):
        self.accounts = {}
        self.credit_service = ExternalCreditService()


    def create_account(self, account_id, initial_balance=0):
        if account_id not in self.accounts:
            self.accounts[account_id] = Account(account_id, initial_balance)
        else:
            raise ValueError("Account already exists")


    def close_account(self, account_id):
        if account_id in self.accounts:
            del self.accounts[account_id]
        else:
            raise ValueError("Account does not exist")


    def get_account_balance(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id].balance
        else:
            raise ValueError("Account does not exist")


    def get_customer_credit_score(self, customer_id):
        return self.credit_service.get_credit_score(customer_id)




  



    

 







   
        
    