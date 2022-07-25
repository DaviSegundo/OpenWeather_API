from dataclasses import dataclass
import time
from .weather_api import OpenWeatherAPI
from .data_formatter import DataFormatter
from models.process import Process, CityInfo


@dataclass
class WeatherCollector:
    """Class to manage the execution of data collection."""

    api: OpenWeatherAPI
    formatter: DataFormatter
    cities_list: list

    def collect_weather_data(self, user_id: int):
        """Controls the data collection flow from the api and stores it in the database.

        Args:
            user_id (int): user identifier 
        """
        data = Process.objects(user_id=user_id).first()
        data_list = data.data
        
        for city_id in self.cities_list: # Remove limitation
            status_code, json_body = self.api.get_city_weather_information_by_id(city_id)
            while status_code != 200:
                status_code, json_body = self.api.get_city_weather_information_by_id(city_id)
                if status_code != 200:
                    time.sleep(30)
            essencial_info = self.formatter.retrive_essencial_city_information(json_body)
            city_info = CityInfo(**essencial_info)
            data_list.append(city_info)
            data.save()
