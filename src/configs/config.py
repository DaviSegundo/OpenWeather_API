import os
from dotenv import load_dotenv
from .cities_ids import CITIES_IDS

load_dotenv()

OPENW_KEY = os.getenv("OPENW_KEY")
CITIES_IDS = CITIES_IDS

SECRET_KEY = os.getenv("SECRET_KEY")
