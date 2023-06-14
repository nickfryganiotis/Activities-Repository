from flask import Flask
from flask_cors import CORS
from flask_mail import Mail


app = Flask(__name__)
CORS(app)
app.config.from_object('config.BaseConfig')


# MAIL config GMAIL
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'emosociograms@gmail.com'
# app.config['MAIL_PASSWORD'] = '2TsfGHt3GTB8tREo'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'v3yeastproject@gmail.com'
app.config['MAIL_DEFAULT_SENDER'] = 'v3yeastproject <v3yeastproject@gmail.com>'
app.config['MAIL_PASSWORD'] = 'gfyxkzksvlotcsly'
# app.config['MAIL_PASSWORD'] = 'V3yeastproject!'
app.config['MAIL_USE_SSL'] = True

app.mail = Mail(app)

from blueprints.users import users
from blueprints.competencies import competencies
from blueprints.didactic_strategies import didactic_strategies
from blueprints.special_needs import special_needs
from blueprints.activities import activities

app.register_blueprint(users)
app.register_blueprint(competencies)
app.register_blueprint(didactic_strategies)
app.register_blueprint(special_needs)
app.register_blueprint(activities)


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