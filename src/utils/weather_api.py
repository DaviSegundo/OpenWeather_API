import requests
from dataclasses import dataclass

@dataclass
class OpenWeatherAPI:
    """Class representing API consumption."""

    api_key: str
    unit: str = 'metric'
    base_url: str = "https://api.openweathermap.org/data/2.5/weather"

    def get_city_weather_information_by_id(self, city_id: int):
        """Get specific information about a city given its id.

        Args:
            city_id (int): city id 

        Returns:
            tuple[Response, dict]: a tuple with the http response and json body
        """
        url = f"{self.base_url}?id={city_id}&appid={self.api_key}&units={self.unit}"
        response = requests.get(url)
        status = response.status_code
        json_body: dict = response.json()
        
        return status, json_body
