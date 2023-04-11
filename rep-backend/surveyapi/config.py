"""
config.py
- settings for the flask application object
"""
import os

class BaseConfig(object):
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///survey.db'
    #SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///survey.db')
    # SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'mysql://root:!EduC@rdi@2022!@localhost:3306/survey')
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(
        os.getenv('DB_USER', 'root'),
        os.getenv('DB_PASSWORD', 'root'),
        os.getenv('DB_HOST', 'localhost'),
        os.getenv('DB_NAME', 'activities')
    )
