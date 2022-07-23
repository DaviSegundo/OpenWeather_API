import os
from dotenv import load_dotenv
from .cities_ids import CITIES_IDS

load_dotenv()

# OpenWeatherAPI
OPENW_KEY = os.getenv("OPENW_KEY")
CITIES_IDS = CITIES_IDS

# DevGrid API
SECRET_KEY = os.getenv("SECRET_KEY")

# Database Setup
DATABASE_NAME = os.getenv("DATABASE_NAME", "test")
DATABASE_URL_CONNECT = os.getenv("DATABASE_URL_CONNECT", f"mongodb://127.0.0.1:27017/{DATABASE_NAME}")
