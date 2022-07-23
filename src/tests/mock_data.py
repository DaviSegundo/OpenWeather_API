from configs.config import OPENW_KEY, CITIES_IDS

MOCK_URL_API_SUCCESS = f"https://api.openweathermap.org/data/2.5/weather?id={CITIES_IDS[0]}&appid={OPENW_KEY}&units=metric"
MOCK_RETURN_API = {
    'coord': {
        'lon': -57.6333, 
        'lat': -32.6833
    }, 
    'weather': [{
        'id': 804, 
        'main': 'Clouds', 
        'description': 'overcast clouds', 
        'icon': '04n'
    }], 
    'base': 'stations', 
    'main': {
        'temp': 17.94, 
        'feels_like': 18.14, 
        'temp_min': 17.94, 
        'temp_max': 17.94, 
        'pressure': 1014, 
        'humidity': 90, 
        'sea_level': 1014, 
        'grnd_level': 1005
    }, 
    'visibility': 10000, 
    'wind': {
        'speed': 3.51, 
        'deg': 111, 
        'gust': 7.21
    }, 
    'clouds': {
        'all': 93
    }, 
    'dt': 1658531811, 
    'sys': {
        'country': 'UY', 
        'sunrise': 1658486836, 
        'sunset': 1658523981
    }, 
    'timezone': -10800, 
    'id': 3439525, 
    'name': 'Young', 
    'cod': 200
}