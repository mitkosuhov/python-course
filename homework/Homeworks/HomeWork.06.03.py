import unittest
from unittest.mock import patch
import re
from datetime import datetime
# Задача 1
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(5, 10), -5)


#Задача 2 


def is_valid_email(email):
    # Проверяваме дали е-мейлът е валиден чрез регулярен израз
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

class TestEmailValidation(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(is_valid_email('user@abv.com'))
        self.assertTrue(is_valid_email('user123@gmail.co.bg'))
        self.assertTrue(is_valid_email('hello_world123@example.org'))

    def test_invalid_emails(self):
        self.assertFalse(is_valid_email('invalid_email.com'))
        self.assertFalse(is_valid_email('name@abv'))
        self.assertFalse(is_valid_email('@example.com'))
        self.assertFalse(is_valid_email('user@.com'))


#Задача 3 
    
def is_weekend():
    today = datetime.now()
    return today.weekday() in [5, 6]  # Събота и неделя имат индекси 5 и 6

class TestWeekendDetection(unittest.TestCase):  
    @patch('datetime.datetime')
    def test_weekend_detection(self, mock_datetime):
        # Симулиране на ден със събота
        mock_datetime.now.return_value = datetime(2024, 3, 16)  # Събота
        self.assertTrue(is_weekend())

        # Симулиране на ден с неделя
        mock_datetime.now.return_value = datetime(2024, 3, 17)  # Неделя
        self.assertTrue(is_weekend())

        # Симулиране на ден с понеделник
        mock_datetime.now.return_value = datetime(2024, 3, 18)  # Понеделник
        self.assertFalse(is_weekend())

if __name__ == '__main__':
    unittest.main()