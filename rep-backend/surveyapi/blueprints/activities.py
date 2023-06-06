# app.app_context() is a context manager provided by Flask that creates an application
# context for your Flask application. This context allows you to access the Flask application 
# and its configuration, as well as the objects and variables that are attached to it.
# When you use app.app_context(), you can run code within the context of your Flask application,
# even if it's outside of a request context. This is useful in cases where you need to perform 
# operations that are related to your application, such as creating database tables or initializing 
# an object with configuration from your application,
# but you don't have access to a request context.


from flask import request
from models import db, Activity, Activity_competence, Activity_translation, Competence, Didactic_strategy, Activity_didactic_strategy, Special_need, Activity_special_need, User
from flask import Blueprint
from sqlalchemy import or_, and_
from helpers import duration_to_num, sub_grouping_to_num
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

activities = Blueprint('activities', __name__)

@activities.route('/create_activity/', methods=('POST',))
def create_activity():
    if request.method=='POST':
        data = request.get_json()

        ## add activity attributes

        new_activity = Activity(**data['activity'])        

        db.session.add(new_activity)
        db.session.commit()

        ## add initial translation
        
        new_activity_translation = Activity_translation(**data['activity_translation'], activity_id = new_activity.id)  
            
        db.session.add(new_activity_translation)
        db.session.commit()

        ## add activity competences
                        
        competences_ids = Competence.query.with_entities(Competence.id).\
                                filter(Competence.code.in_(data['activity_competences'])).\
                                    all()
        competences_ids = [competence_id for (competence_id,) in competences_ids] 
        new_activity_competences = [
                  Activity_competence(activity_id=new_activity.id, competence_id=comp_id) for comp_id in competences_ids
        ]
            
        db.session.add_all(new_activity_competences)
        db.session.commit()

        ## add activity didactic strategies

        strategies_ids = Didactic_strategy.query.with_entities(Didactic_strategy.id).\
                                filter(Didactic_strategy.code.in_(data['activity_didactic_strategies'])).\
                                    all()
        strategies_ids = [strategy_id for (strategy_id,) in strategies_ids] 
        new_activity_strategies = [
                  Activity_didactic_strategy(activity_id=new_activity.id, strategy_id=str_id) for str_id in strategies_ids
        ]
            
        db.session.add_all(new_activity_strategies)
        db.session.commit()

        ## add activity special needs

        special_needs_ids = Special_need.query.with_entities(Special_need.id).\
                                filter(Special_need.code.in_(data['activity_special_needs'])).\
                                    all()
        special_needs_ids = [special_need_id for (special_need_id,) in special_needs_ids] 
        new_activity_special_needs = [
                  Activity_special_need(activity_id=new_activity.id, special_need_id=sp_need_id) for sp_need_id in special_needs_ids
        ]
            
        db.session.add_all(new_activity_special_needs)
        db.session.commit()
                       
        return new_activity.to_dict()    
           
    else:
        return "Error"

    

@activities.route('/get_activity/<int:id>/<string:language_code>/', methods=('GET',))
def get_activity(id, language_code):
    if request.method=='GET':

        activity = Activity.query.\
                        filter_by(id=id).\
                            join(Activity_translation).\
                                filter_by(language_code='en').\
                                    first()
        activity.to_dict()
        return activity.to_dict()

    else: 
        return "Error"
    
@activities.route('/get_activities_per_page/<int:cursor>/<string:language_code>/', methods=('GET',))
def get_activities_per_page(cursor, language_code):
    if request.method=='GET':
        
        ## get activities
        
        activities = Activity.query.join(Activity_translation).\
                                            filter_by(language_code=language_code).\
                                                    offset((cursor - 1) * 10).\
                                                        limit(11).\
                                                            all()
        
        ## set next cursor

        next_cursor = -1
        if len(activities) > 10:
            activities.pop()
            next_cursor = cursor + 1
        
        activities = [
            activity.preview_to_dict() for activity in activities
        ]

        if next_cursor == -1:
            return {'activities': activities}
        else:
            return {'activities': activities, 'nextCursor': cursor + 1} 
        
    else:
        return "Error"
    
@activities.route('/test/', methods=('POST', 'GET',))
def test():
    if request.method=="POST":
        data = request.get_json()
        competences_query = db.session.query(Competence.id).join(
            Activity_competence, Competence.id == Activity_competence.competence_id).filter(
            Competence.code.in_(data['competences'])
            ).order_by(Competence.id)
        #competences_query = competences_query.options(joinedload(Competence.activity_competence))
        #competences_results = [(competence.code, activity_competence.activity_id) for competence, 
        #                        activity_competence in competences_query.all()]
        print(competences_query)
        return "Hi"
    elif request.method=='GET':
        activity = Activity.query.\
                        filter_by(id=1).\
                            join(Activity_translation).\
                                filter_by(language_code='en').\
                                    first()
        print(activity.activity_translations[0].to_dict())
        return "hi"

# @activities.route('/test2/<int:cursor>/<string:language_code>/', methods=('POST',))
# def test2(cursor, language_code):
#     if request.method=='POST':
        
#         data = request.get_json()

#         ## Set a list variable for the query conjuction parameters concerining of activity and activity_translation

#         query_parameters = []   

#         ## Activity attributes
        
#         query_parameters.append(or_(*[Activity.periodicity == periodicity for periodicity in data['periodicity']]))     
#         query_parameters.append(or_(*[and_(Activity.min_age == min_age, Activity.max_age == max_age)
#                                        for (min_age, max_age) in [tuple([int(x) for x in age_target_group_case])
#                                                         for age_target_group_case in [age_target_group.split('-')
#                                                                 for age_target_group in data['age_target_group']]]]))
#         query_parameters.append(or_(*[Activity.duration == duration_to_num(duration) for duration in data['duration']]))
#         query_parameters.append(or_(*[Activity.sub_grouping == sub_grouping_to_num(sub_grouping) 
#                                    for sub_grouping in data['sub_grouping']]))
#         if not data['teacher_role'] == "":
#             query_parameters.append(Activity.teacher_role == data['teacher_role'])
        
#         ## Activity_translation attributes

#         if not data['title'] == "":
#             query_parameters.append(Activity_translation.title == data['title'])
#         query_parameters.append(Activity_translation.language_code == language_code)
                       
#         activities = Activity.\
#                         query.\
#                             join(Activity_translation).\
#                                 filter(and_(*query_parameters))
                                    
#         ## Competences, Didactic strategies, Special needs
        
#         competences = data['competences']
#         didactic_strategies = data['didactic_strategies']
#         special_needs = data['special_needs']

#         activity_competences = db.session.\
#                                 query(Activity_competence.activity_id).\
#                                     join(Competence).\
#                                         filter(Competence.code.in_(competences)).\
#                                             group_by(Activity_competence.activity_id).\
#                                                 subquery()
                
#         activity_didactic_strategies = db.session.\
#                                         query(Activity_didactic_strategy.activity_id).\
#                                             join(Didactic_strategy).\
#                                                 filter(Didactic_strategy.code.in_(didactic_strategies)).\
#                                                     group_by(Activity_didactic_strategy.activity_id).\
#                                                         subquery()
        
#         activity_special_needs = db.session.\
#                                     query(Activity_special_need.activity_id).\
#                                         join(Special_need).\
#                                             filter(Special_need.code.in_(special_needs)).\
#                                                 group_by(Activity_special_need.activity_id).\
#                                                     subquery()
        
#         if competences:
#             activities = activities.join(activity_competences)
        
#         if didactic_strategies:
#             activities = activities.join(activity_didactic_strategies)
        
#         if special_needs:
#             activities = activities.join(activity_special_needs)

#         ## uncomment to print query
#         # print(activities)    
        
#         activities = activities.\
#                         offset((cursor - 1) * 10).\
#                             limit(11).\
#                                 all()

#         ## set next cursor

#         next_cursor = -1
#         if len(activities) > 10:
#             activities.pop()
#             next_cursor = cursor + 1
        
#         activities = [
#             activity.preview_to_dict() for activity in activities
#         ]

#         if next_cursor == -1:
#             return {'activities': activities}
#         else:
#             return {'activities': activities, 'nextCursor': cursor + 1} 
        
#     else:
#         return "Error"     

@activities.route('/filter_activities/<int:cursor>/<string:language_code>/', methods=('POST',))
def filter_activities(cursor, language_code):
    if request.method=="POST":
        
        data = request.get_json()

        ## Set a list variable for the query conjuction parameters concerining of activity and activity_translation

        query_parameters = []   

        ## Activity attributes
        
        query_parameters.append(or_(*[Activity.periodicity == periodicity for periodicity in data['periodicity']]))     
        query_parameters.append(or_(*[and_(Activity.min_age == min_age, Activity.max_age == max_age)
                                       for (min_age, max_age) in [tuple([int(x) for x in age_target_group_case])
                                                        for age_target_group_case in [age_target_group.split('-')
                                                                for age_target_group in data['age_target_group']]]]))
        query_parameters.append(or_(*[Activity.duration == duration_to_num(duration) for duration in data['duration']]))
        query_parameters.append(or_(*[Activity.sub_grouping == sub_grouping_to_num(sub_grouping) 
                                   for sub_grouping in data['sub_grouping']]))
        query_parameters.append(or_(*[Activity.teacher_role == teacher_role for teacher_role in data['teacher_role']]))
        
        ## Activity_translation attributes

        if not data['title'] == "":
            query_parameters.append(Activity_translation.title == data['title'])
        query_parameters.append(Activity_translation.language_code == language_code)
                       
        activities = Activity.\
                        query.\
                            join(Activity_translation).\
                                filter(and_(*query_parameters))
                                    
        ## Competences, Didactic strategies, Special needs
        
        competences = data['competences']
        didactic_strategies = data['didactic_strategies']
        special_needs = data['special_needs']

        activity_competences = db.session.\
                                query(Activity_competence.activity_id).\
                                    join(Competence).\
                                        filter(Competence.code.in_(competences)).\
                                            group_by(Activity_competence.activity_id).\
                                                subquery()
                
        activity_didactic_strategies = db.session.\
                                        query(Activity_didactic_strategy.activity_id).\
                                            join(Didactic_strategy).\
                                                filter(Didactic_strategy.code.in_(didactic_strategies)).\
                                                    group_by(Activity_didactic_strategy.activity_id).\
                                                        subquery()
        
        activity_special_needs = db.session.\
                                    query(Activity_special_need.activity_id).\
                                        join(Special_need).\
                                            filter(Special_need.code.in_(special_needs)).\
                                                group_by(Activity_special_need.activity_id).\
                                                    subquery()
        
        if competences:
            activities = activities.join(activity_competences)
        
        if didactic_strategies:
            activities = activities.join(activity_didactic_strategies)
        
        if special_needs:
            activities = activities.join(activity_special_needs)

        ## uncomment to print query
        # print(activities)    
        
        activities = activities.\
                        offset((cursor - 1) * 10).\
                            limit(11).\
                                all()

        ## set next cursor

        next_cursor = -1
        if len(activities) > 10:
            activities.pop()
            next_cursor = cursor + 1
        
        activities = [
            activity.preview_to_dict() for activity in activities
        ]

        if next_cursor == -1:
            return {'activities': activities}
        else:
            return {'activities': activities, 'nextCursor': cursor + 1} 
        
    else:
        return "Error"     