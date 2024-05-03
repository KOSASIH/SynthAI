import unittest
from src.utils.data_io import load_data

class TestDataIO(unittest.TestCase):
    def test_load_data(self):
        data = load_data('tests/test_data.csv')
        # Add assertions here to test the loaded data
        pass
