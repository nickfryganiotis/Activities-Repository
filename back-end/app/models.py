from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    min_age = db.Column(db.Integer)
    max_age = db.Column(db.Integer)
    periodicity = db.Column(db.String(255))
    duration = db.Column(db.Integer)
    presence = db.Column(db.String(255))
    sub_grouping = db.Column(db.Integer)
    teacher_role = db.Column(db.String(255))
    source = db.Column(db.String(255))
    source_type = db.Column(db.String(255))
    apriory = db.Column(db.Integer, db.ForeignKey('activity.id'))
    posteriory = db.Column(db.Integer, db.ForeignKey('activity.id'))
    #__table_args__ = (db.ForeignKeyConstraint([apriory], ['activity.id']),
    #                  db.ForeignKeyConstraint([posteriory], ['activity.id']))
    activity_apriory = db.relationship('Activity', foreign_keys = [apriory], remote_side = [id], backref='apriori_activity')
    activity_posteriory = db.relationship('Activity', foreign_keys = [posteriory], remote_side = [id], backref= 'posteriory_activity')
    activity_translation = db.relationship('Activity_translation', backref='translation_activity')
    activity_didactic_strategy = db.relationship('Activity_didactic_strategy', backref='didactic_activity')

    def __init__(self, data):
        if 'min_age' in data:
            self.min_age = data['min_age']
        if 'max_age' in data:
            self.max_age = data['max_age']
        if 'periodicity' in data:
            self.periodicity = data['periodicity']
        if 'duration' in data:
            self.duration = data['duration']
        if 'presence' in data:
            self.presence = data['presence']
        if 'sub_grouping' in data:
            self.sub_grouping = data['sub_grouping']
        if 'teacher_role' in data:
            self.teacher_role = data['teacher_role']
        if 'source' in data:
            self.source = data['source']
        if 'source_type' in data:
            self.source_type = data['source_type']
        if 'apriory' in data:
            self.apriory = data['apriori']
        if 'posteriory' in data:
            self.posteriory = data['posteriory']

    def to_dict(self):
        activity = {}
        activity['id'] = self.id
        activity['created_at'] = self.created_at
        activity['min_age'] = self.min_age 
        activity['max_age'] = self.max_age
        activity['periodicity'] = self.periodicity 
        activity['duration'] = self.duration
        activity['presence'] = self.presence
        activity['sub_grouping'] = self.sub_grouping
        activity['teacher_role'] = self.teacher_role
        activity['source'] = self.source
        activity['source_type'] = self.source_type
        activity['apriory'] = self.apriory
        activity['posteriory'] = self.posteriory

        return activity

class Activity_translation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))
    language_code = db.Column(db.String(255))
    title = db.Column(db.String(255))
    learning_objectives = db.Column(db.String(255))
    description = db.Column(db.String(255))
    evaluation = db.Column(db.String(255))
    material = db.Column(db.String(255))

    def __init__(self, data):
        if 'activity_id' in data:
            self.activity_id = data['activity_id']
        if 'language_code' in data:
            self.language_code = data['language_code']
        if 'title' in data:
            self.title = data['title']
        if 'learning_objectives' in data:
            self.learning_objectives = data['learning_objectives']
        if 'description' in data:
            self.description = data['description']
        if 'evaluation' in data:
            self.evaluation = data['evaluation']
        if 'material' in data:
            self.material = data['material']
    
    def to_dict(self):
        activity_translation = {}
        activity_translation['id'] = self.id
        activity_translation['activity_id'] = self.activity_id
        activity_translation['language_code'] = self.language_code
        activity_translation['title'] = self.title
        activity_translation['learning_objectives'] = self.learning_objectives
        activity_translation['description'] = self.description
        activity_translation['evaluation'] = self.evaluation
        activity_translation['material'] = self.material
        return activity_translation  

class Activity_didactic_strategy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))
    strategy_id = db.Column(db.Integer, db.ForeignKey('didactic_strategy.id'))

class Didactic_strategy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(255), nullable=False)
    activity_didactic_strategy = db.relationship('Activity_didactic_strategy', backref='activity_didactic')

class Activity_competence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))
    competence_id = db.Column(db.Integer, db.ForeignKey('competence.id'))
    
    def __init__(self, data):
        if 'activity_id' in data:
            self.activity_id = data['activity_id']
        if 'competence_id' in data:
            self.competence_id = data['competence_id']
    
    def to_dict(self):
        activity_competence = {}
        activity_competence['id'] = self.id
        activity_competence['activity_id'] = self.activity_id
        activity_competence['competence_id'] = self.competence_id

        return activity_competence    

class Competence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(255), nullable=False)
    activity_competence = db.relationship('Activity_competence', backref='act_competence')

class Activity_special_need(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))
    special_need_id = db.Column(db.Integer, db.ForeignKey('special_need.id'))

class Special_need(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(255), nullable=False)
    activity_special_need = db.relationship('Activity_special_need', backref='activity_special_need')

  