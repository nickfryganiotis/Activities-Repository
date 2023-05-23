from flask import request

from models import db, User
from flask import Blueprint

users = Blueprint('users', __name__)

@users.route('/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
    try:
        # TODO: Hash the password...

        # Depending on the data given in the input field, the user is searched in the database
        if (data['username']):
            user = User.query.filter_by(username = data['username']).first()
        elif (data['email']):
            user = User.query.filter_by(email = data['email']).first()

        # If the user is found and the password is correct, the user is returned
        if user and user.password_hash == data['password_hash']:
            return user.to_dict()
        else:
            return "Error"
    except:
        return "Error"
    
@users.route('/signup', methods = ['POST'])
def signup():
    if request.method == 'POST':
        data = request.get_json()
        user = User(**data)
           
        db.session.add(user)
        db.session.commit()

        return {"user_id":user.id}
    