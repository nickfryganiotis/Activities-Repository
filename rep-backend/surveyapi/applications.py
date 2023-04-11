from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config.from_object('config.BaseConfig')
from models import db

from api import api
app.register_blueprint(api)


db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        # code that needs access to the application context goes here
        db.create_all()
    app.run(debug=True)