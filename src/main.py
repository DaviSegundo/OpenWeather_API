from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from configs.config import SECRET_KEY, DATABASE_URL_CONNECT
from api.routes import blueprint

# App initial configuration setup
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

# Database configuration with MongoEngine
app.config['MONGODB_SETTINGS'] = {
    'host': DATABASE_URL_CONNECT
}
db = MongoEngine(app)

# CORS setup
CORS(app)

app.register_blueprint(blueprint, url_prefix='/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)