from flask import Flask
from configs.config import SECRET_KEY
from api.routes import blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.register_blueprint(blueprint, url_prefix='/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)