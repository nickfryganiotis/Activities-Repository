from flask import request
from models import db, Activity, Activity_competence, Activity_translation, Competence
from flask import Blueprint

create_activities_api = Blueprint('create_activity', __name__)

@create_activities_api.route('/create_activity', methods=['POST'])
def create_activity():
    if request.method=='POST':
        data = request.get_json()
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
