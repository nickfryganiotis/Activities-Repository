from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config.from_object('config.BaseConfig')

from blueprints.activities import activities
from blueprints.competences import competences
from blueprints.users import users
app.register_blueprint(activities)
app.register_blueprint(competences)
app.register_blueprint(users)


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