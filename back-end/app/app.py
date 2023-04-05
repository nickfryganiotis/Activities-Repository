# app.app_context() is a context manager provided by Flask that creates an application
# context for your Flask application. This context allows you to access the Flask application 
# and its configuration, as well as the objects and variables that are attached to it.
# When you use app.app_context(), you can run code within the context of your Flask application,
# even if it's outside of a request context. This is useful in cases where you need to perform 
# operations that are related to your application, such as creating database tables or initializing 
# an object with configuration from your application,
# but you don't have access to a request context.

from flask import Flask, request
from flask_cors import CORS
from models import db, Activity, Activity_competence, Activity_translation, Competence

app = Flask(__name__)
CORS(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/activities'
db.init_app(app)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/create_activity', methods=['POST'])
def create_activity():
    if request.method=='POST':
        data = request.json
        new_activity = Activity(data['activity'])   
        try:
            db.session.add(new_activity)
             #print(new_activity) 
            db.session.commit()
            #Activity.query.all()
            for activity_translation in data['activity_translations']:
                activity_translation['activity_id'] = new_activity.id
                new_activity_translation = Activity_translation(activity_translation)
                try:
                    db.session.add(new_activity_translation)
                    db.session.commit()
                except:
                    return "Error"
            for activity_competence_code in data['activity_competences']:
                competence_id = (Competence.query.filter_by(code=activity_competence_code)).first().id
                new_activity_competence = Activity_competence({"activity_id": new_activity.id, "competence_id": competence_id})
                try:
                    db.session.add(new_activity_competence)
                    db.session.commit()
                except:
                    return "Error"
            return new_activity.to_dict()
        except:
            return "Error"    
    else:
        return "Error"


@app.route('/create_competence', methods=['POST'])
def create_competence():
        if request.method=="POST":
            data = request.json
            new_competence = Competence(code=data['code'])
            try:
                db.session.add(new_competence)
                db.session.commit() 
                return {"code": new_competence.code}
            except:
                return "Error" 
        else:
            return "Error"

@app.route('/get_activities', methods=['GET'])
def get_activities():
    if request.method=="GET":
        try:
            activities = Activity.query.all() 
            activities_dict = []
            for activity in activities:
                act = activity.to_dict()
                act_competences=Activity_competence.query.filter(Activity_competence.activity_id==act["id"]).all()
                
                act_competences_codes = []
                for act_competence in act_competences:
                    act_competence_code = Competence.query.filter_by(id=act_competence.competence_id).first().code
                    act_competences_codes.append(act_competence_code)
                act_obj_transl = Activity_translation.query.filter(Activity_translation.activity_id==act["id"]).all()
                act_transl = [x.to_dict() for x in act_obj_transl]
                activities_dict.append({"activity": act, "activity_competences": act_competences_codes, "activity_translations": act_transl})
            return activities_dict
        except:
            return "Error"    
    else:
        return "Error"

@app.route('/get_activity', methods=['GET'])
def get_activity():
    if request.method=="GET":
        id = request.args.get('activity_id')
        act=(Activity.query.filter_by(id=id)).first().to_dict()
        act_competences=Activity_competence.query.filter(Activity_competence.activity_id==id).all()

        act_competences_codes = []
        for act_competence in act_competences:
            act_competence_code = Competence.query.filter_by(id=act_competence.competence_id).first().code
            act_competences_codes.append(act_competence_code)
        act_obj_transl = Activity_translation.query.filter(Activity_translation.activity_id==act["id"]).all()
        act_transl = [x.to_dict() for x in act_obj_transl]
        return {"activity": act, "activity_competences": act_competences_codes, "activity_translations": act_transl} 
    else:
        return "Error"

if __name__ == '__main__':
    with app.app_context():
        # code that needs access to the application context goes here
        db.create_all()
    app.run(debug=True)

# In this example, the db.create_all() method is called within the context of the Flask application, 
# which allows it to access the db object that was created using Flask-SQLAlchemy and 
# the configuration for the application.