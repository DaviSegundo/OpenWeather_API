from broker.broker_commons import BrokerCommons
import json
from utils.weather_api import OpenWeatherAPI
from utils.data_formatter import DataFormatter
from utils.weather_collector import WeatherCollector
from configs.config import OPENW_KEY, CITIES_IDS, DATABASE_URL_CONNECT
from mongoengine import connect

if __name__ == '__main__':

    connect(host=DATABASE_URL_CONNECT)

    formatter = DataFormatter()
    api = OpenWeatherAPI(OPENW_KEY)
    collector = WeatherCollector(api, formatter, CITIES_IDS)

    def tec(ch, method, properties, body):
        decodec = json.loads(body)
        valid = decodec.get('valid')
        user_id = decodec.get('user_id')
        print(f"Collecting data to user: {user_id}")
        if valid:
            collector.collect_weather_data(user_id)
        print(f"Collection of data for user id: {user_id} has been completed.")

    print("Starting Consumer:")
    broker_consumer = BrokerCommons('localhost')
    broker_consumer.queue_declare('process')
    broker_consumer.set_callback_function(tec)
    print("Ready to consume...")
    broker_consumer.consume('process')