import unittest
from utils.data_formatter import DataFormatter
from .mock_data import MOCK_RETURN_API


class TestDataFormatter(unittest.TestCase):
    """Class to test DataFormatter functionality."""
    
    def test_retrive_information_type(self):
        """Tests if the return of the function has the correct type."""
        formatter = DataFormatter()
        data = formatter.retrive_essencial_city_information(MOCK_RETURN_API)

        self.assertEqual(dict, type(data))

    def test_mock_return(self):
        """Test to verify if the return is correct with the mocked data."""
        formatter = DataFormatter()
        data = formatter.retrive_essencial_city_information(MOCK_RETURN_API)
        correct_return = {
            'city_id': 3439525, 
            'temperature': 17.94, 
            'humidity': 90
        }

        self.assertEqual(data, correct_return)
