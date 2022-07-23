from flask_restx import Api
from flask import Blueprint
from .routes_weather import api as weather_api

blueprint = Blueprint('swagger', 'swagger')
api = Api(
    blueprint,
    title='DEVGRID - API',
    version='1.0',
    description='API to track the progress of an asynchronous request.'
)

api.add_namespace(weather_api)