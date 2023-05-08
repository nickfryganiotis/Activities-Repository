# app.app_context() is a context manager provided by Flask that creates an application
# context for your Flask application. This context allows you to access the Flask application 
# and its configuration, as well as the objects and variables that are attached to it.
# When you use app.app_context(), you can run code within the context of your Flask application,
# even if it's outside of a request context. This is useful in cases where you need to perform 
# operations that are related to your application, such as creating database tables or initializing 
# an object with configuration from your application,
# but you don't have access to a request context.

from flask import request
from models import Activity, Activity_competence, Activity_translation, Competence
from flask import Blueprint
from sqlalchemy import or_, and_
from helpers import duration_to_num, sub_grouping_to_num
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

get_activities_api = Blueprint('get_activities', __name__)

@get_activities_api.route('/get_activities', methods=['GET'])
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
                activities_dict.append({"activity": act, "activity_competences": act_competences_codes, 
                                        "activity_translations": act_transl})
            return activities_dict
        except:
            return "Error"    
    else:
        return "Error"
    

@get_activities_api.route('/get_activity', methods=['GET'])
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
    
@get_activities_api.route('/get_activities_per_page', methods=['GET'])
def get_activities_per_page():
    if request.method=="GET":
        try:
            cursor = int(request.args.get('cursor'))
            activities = Activity.query.offset((cursor - 1) * 4).limit(5).all()
            next_cursor = -1
            if len(activities) > 4:
                activities.pop()
                next_cursor = cursor + 1
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
                activities_dict.append({"activity": act, "activity_competences": act_competences_codes, 
                                        "activity_translations": act_transl})
            if next_cursor == - 1:
                return {"activities": activities_dict}
            return {"activities": activities_dict, "nextCursor": cursor + 1}
        except:
            return "Error"
    else:
        return "Error"
    
@get_activities_api.route('/filter_activities', methods=['POST'])
def filter_activities():
    if request.method=="POST":
        data = request.get_json()
        query_parameters = []   # Set a tuple variable for the query conjuction parameters 

        # Activity attributes
        query_parameters.append(or_(*[Activity.periodicity == periodicity for periodicity in data['periodicity']]))     
        query_parameters.append(or_(*[and_(Activity.min_age == min_age, Activity.max_age == max_age)
                                       for (min_age, max_age) in [tuple([int(x) for x in age_target_group_case])
                                                        for age_target_group_case in [age_target_group.split('-')
                                                                for age_target_group in data['age_target_group']]]]))
        query_parameters.append(or_(*[Activity.duration == duration_to_num(duration.split(' ')[0]) for duration in data['duration']]))
        query_parameters.append(or_(*[Activity.sub_grouping == sub_grouping_to_num(sub_grouping.split(' ')[0]) 
                                   for sub_grouping in data['sub_grouping']]))
        if not data['teacher_role'] == "":
            query_parameters.append(Activity.teacher_role == data['teacher_role']) 

        print(*query_parameters)

        # Filtering query execution 
        query = and_(*query_parameters)
        try:
             activities = Activity.query.filter(query).all()
             return [x.to_dict() for x in activities]
        except:
            return "Error"
    else:
        return "Error"