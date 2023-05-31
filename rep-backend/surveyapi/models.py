from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from helpers import duration_to_num, sub_grouping_to_num, num_to_duration, num_to_sub_grouping

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    surname = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    role = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    confirmed = db.Column(db.Integer,  unique=False, nullable=True)
    confirmationHash = db.Column(db.String(255),  unique=False, nullable=True)
    confirmationDate = db.Column(db.DateTime, nullable=True)
    recoverHash = db.Column(db.String(255),  unique=False, nullable=True)
    recoverDate = db.Column(db.DateTime, nullable=True)
    activities = db.relationship('Activity', backref='activity_creator')
    activity_translations = db.relationship('Activity_translation', backref='activity_translation_creator')
    stars = db.relationship('Stars', backref='evaluator')
    comments = db.relationship('Comments', backref='commenter')

    def __init__(self, name, surname, sex, email, password, role):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = 40
        #self.abbreviation = name[0:1]+surname[0:1]
        self.email = email
        self.role = role
        self.password = generate_password_hash(password, method='sha256')


class Activity(db.Model):
    __tablename__ = 'activity'

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
    creator = db.Column(db.Integer, db.ForeignKey('users.id'))
    has_apriory = db.relationship('Activity', foreign_keys = [apriory], remote_side = [id], backref='apriori_activity')
    has_posteriory = db.relationship('Activity', foreign_keys = [posteriory], remote_side = [id], backref= 'posteriory_activity')
    activity_translations = db.relationship('Activity_translation', backref='activity')
    activity_competences = db.relationship('Activity_competence', backref='activity')
    activity_didactic_strategies = db.relationship('Activity_didactic_strategy', backref='activity')
    activity_special_needs = db.relationship('Activity_special_need', backref='activity')
    stars = db.relationship('Stars', backref='activity')
    comments = db.relationship('Comments', backref='activity')

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if key == 'duration':
                setattr(self, key, duration_to_num(value))
            elif key == 'sub_grouping':
                setattr(self, key, sub_grouping_to_num(value))
            else:
                setattr(self, key, value)  

    def to_dict(self):
        return dict(id=self.id,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    min_age=self.min_age,
                    max_age=self.max_age,
                    periodicity=self.periodicity, 
                    duration=num_to_duration(self.duration),
                    presence=self.presence,
                    sub_grouping=num_to_sub_grouping(self.sub_grouping),
                    teacher_role=self.teacher_role,
                    source=self.source,
                    source_type=self.source_type,
                    apriory=self.apriory,
                    posteriory=self.posteriory,
                    creator=self.creator,
                    comptences=[competence.to_dict()['code'] for competence in self.activity_competences],
                    didactic_strategies=[didactic_strategy.to_dict()['code'] for didactic_strategy in self.activity_didactic_strategies],
                    special_needs=[special_need.to_dict()['code'] for special_need in self.activity_special_needs],
                    activity_translations=[activity_translation.to_dict() for activity_translation in self.activity_translations]
                )
    
    def preview_to_dict(self):
        return dict(id=self.id,
                    min_age=self.min_age,
                    max_age=self.max_age,
                    teacher_role=self.teacher_role,
                    comptences=[competence.to_dict()['code'] for competence in self.activity_competences],
                    activity_translations=[activity_translation.preview_to_dict() for activity_translation in self.activity_translations]
                    ) 
    
class Stars(db.Model):
    __tablename__ = 'stars'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(500))
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

class Activity_translation(db.Model):
    __tablename__ = 'activity_translation'

    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))
    creator = db.Column(db.Integer, db.ForeignKey('users.id'))
    language_code = db.Column(db.String(255))
    title = db.Column(db.String(255))
    learning_objectives = db.Column(db.String(255))
    description = db.Column(db.String(255))
    evaluation = db.Column(db.String(255))
    material = db.Column(db.String(255))

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def to_dict(self):
        return dict(id=self.id,
                    activity_id=self.activity_id,
                    language_code=self.language_code,
                    title=self.title,
                    learning_objectives=self.learning_objectives,
                    description=self.description,
                    evaluation=self.evaluation,
                    material=self.material,
                    short_description=self.short_description
                )
    
    def preview_to_dict(self):
        return dict(id=self.id,
                    activity_id=self.activity_id,
                    language_code=self.language_code,
                    title=self.title,
                    short_description=f"{self.description[:100]}..."
                    )    
       
class Activity_didactic_strategy(db.Model):
    __tablename__ = 'activity_didactic_strategy'

    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))
    strategy_id = db.Column(db.Integer, db.ForeignKey('didactic_strategy.id'))

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def to_dict(self):
        return dict(id=self.id,
                    activity_id=self.activity_id,
                    strategy_id=self.strategy_id,
                    code=self.didactic_strategy.code
                   )


class Didactic_strategy(db.Model):
    __tablename__ = 'didactic_strategy'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(255), nullable=False)
    activities = db.relationship('Activity_didactic_strategy', backref='didactic_strategy')

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def to_dict(self):
        return dict(id=self.id,
                    code=self.code
                )    

class Activity_competence(db.Model):
    __tablename__ = 'activity_competence'

    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))
    competence_id = db.Column(db.Integer, db.ForeignKey('competence.id'))
    
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def to_dict(self):
        return dict(id=self.id,
                    activity_id=self.activity_id,
                    competence_id=self.competence_id,
                    code=self.competence.code
                   )

class Competence(db.Model):
    __tablename__ = 'competence'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(255), nullable=False)
    activities = db.relationship('Activity_competence', backref='competence')

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def to_dict(self):
        return dict(id=self.id,
                    code=self.code
                )    
    
class Activity_special_need(db.Model):
    __tablename__ = 'activity_special_need'

    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))
    special_need_id = db.Column(db.Integer, db.ForeignKey('special_need.id'))

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def to_dict(self):
        return dict(id=self.id,
                    activity_id=self.activity_id,
                    special_need_id=self.special_need_id,
                    code=self.special_need.code
                   )

class Special_need(db.Model):
    __tablename__ = 'special_need'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(255), nullable=False)
    activities = db.relationship('Activity_special_need', backref='special_need')

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return dict(id=self.id,
                    code=self.code
                )    
 