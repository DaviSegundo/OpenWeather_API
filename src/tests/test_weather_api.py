import unittest
from unittest import mock
from utils.weather_api import OpenWeatherAPI
from configs.config import OPENW_KEY, CITIES_IDS
from .mock_data import MOCK_RETURN_API
from .mock_functions import mocked_requests_get


class TestWeatherAPI(unittest.TestCase):
    """Class to test API functionality."""

    api = OpenWeatherAPI(OPENW_KEY)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_city_return_type(self, mock_get):
        """Tests if the return of the function has the correct type."""
        info = self.api.get_city_weather_information_by_id(CITIES_IDS[0])

        self.assertEqual(tuple, type(info))

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_city_return_success(self, mock_get):
        """Test with mock response to verify API request successfull."""
        info = self.api.get_city_weather_information_by_id(CITIES_IDS[0])
        status_code = info[0]
        json_body = info[1]

        self.assertEqual(status_code, 200)
        self.assertEqual(json_body, MOCK_RETURN_API)
    
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_city_return_fail(self, mock_get):
        """Test with mock response to verify API request fail."""
        info = self.api.get_city_weather_information_by_id(8888888)
        status_code = info[0]
        json_body = info[1]

        self.assertEqual(status_code, 404)
        self.assertEqual(json_body, {'cod': '404', 'message': 'city not found'})

