from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config.from_object('config.BaseConfig')

from blueprints.create_activities_api import create_activities_api
from blueprints.create_subarrays_api import create_subarrays_api
from blueprints.get_activities_api import get_activities_api
from blueprints.user_api import user_api
app.register_blueprint(create_activities_api)
app.register_blueprint(create_subarrays_api)
app.register_blueprint(get_activities_api)
app.register_blueprint(user_api)


from models import db
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        # code that needs access to the application context goes here
        db.create_all()
    app.run(debug=True)


# In this example, the db.create_all() method is called within the context of the Flask application, 
# which allows it to access the db object that was created using Flask-SQLAlchemy and 
# the configuration for the application.