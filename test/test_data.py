import unittest
from unittest.mock import patch
from src.data.preprocessing.data_cleaning import clean_data

class TestDataCleaning(unittest.TestCase):
    @patch('src.data.preprocessing.data_cleaning.is_valid_email')
    def test_clean_data(self, mock_is_valid_email):
        mock_is_valid_email.return_value = True
        dirty_data = [
            {'name': 'John Doe', 'email': 'john.doe@example.com'},
            {'name': 'Jane Doe', 'email': 'jane.doe@example'},
            {'name': '', 'email': ''}
        ]
        expected_data = [
            {'name': 'John Doe', 'email': 'john.doe@example.com'},
            {'name': 'Jane Doe', 'email': 'jane.doe@example.com'},
            {'name': None, 'email': None}
        ]
        self.assertEqual(clean_data(dirty_data), expected_data)
