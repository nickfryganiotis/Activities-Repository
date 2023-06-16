from models import db, User
from flask import Blueprint, jsonify, request, current_app
from flask_mail import Message
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
from functools import wraps
import jwt
import time
import os
import hashlib
import re


users = Blueprint('users', __name__)
FRONT_END_URI = os.getenv('FRONT_END_URI', 'localhost:9000')

# Function that creates a new user and send the mail to confirm the mail.
@users.route('/register/', methods=('POST',))
def register():
    dataAll = request.get_json()
    data = dataAll.get("args")
    bdData = {
        "name": data.get("name", "test"),
        "surname": data.get("surname", "test2"),
        "sex": data.get("sex", "Female"),
        "age": data.get("age", 5),
        "email": data.get("email"),
        "password": data.get("password"),
        "role": "tutor"
    }
    locale = dataAll.get("locale", "en") # TODO: Check that only can be 3 values en, es, gr

    user = User(**bdData)
    isUser = User.query.filter_by(email=user.email)
    if isUser.count()>0 :
        return jsonify({ 'message': 'user already exists', 'code': 'failedRegistrationRegister' }), 409
    db.session.add(user)
    db.session.commit()

    # Generate the hash
    userDb = User.query.filter_by(email=user.email).first()
    strHash = f"{str(userDb.id)}{userDb.email}{userDb.role}"
    mailHash = hashlib.sha224(strHash.encode('utf-8')).hexdigest()
    userDb.confirmationHash = mailHash
    db.session.commit()


    # Read the template mail content
    with open(f"../static/register_{locale}.html", 'r') as file :
        filedata = file.read()

    # Find title in the confirmation file
    pattern = re.split("title", filedata)
    pattern = pattern[1][1:-2]

    # Replace the target string
    msg = Message(pattern, recipients = [user.email])
    msg.html = str(filedata.replace('TAGTOCHANGE', f"http://{FRONT_END_URI}/confirmation/?mail={userDb.email}&key={mailHash}"))
    current_app.mail.send(msg)
    return jsonify({"email": user.email}), 200

# Function to confirm the mail in registration process
@users.route('/confirm/', methods=('POST',))
def confirm():
    data = request.get_json()
    # Maybe it is empty data. We have to check it.
    hash = data.get('key', "empty")
    mail = data.get('mail', "none")

    # If user does not exist, return Error
    isUser = User.query.filter_by(email=mail)
    if isUser.count()==0:
        return jsonify({ 'message': 'User does not exist', 'code': 'failedConfirmationConfirm' }), 409

    user = isUser.first()
    # if user is confirmed yet
    if user.confirmed == 1:
        return jsonify({ 'message': 'User yet confirmed', 'code': 'yetConfirmatedConfirm' }), 409

    # If hashs match and it is not confirmed yet, ok. Else, Error.
    if user.confirmationHash == hash and not user.confirmed :
        user.confirmed = 1
        db.session.commit()
        return jsonify({"email": mail}), 201
    else :
        return jsonify({ 'message': 'Hashes does not match', 'code': 'failedConfirmationConfirm' }), 409
    
# Function that sends the email to recover the password.
@users.route('/recover/', methods=('POST',))
def recover():
    data = request.get_json()
    mail = data.get('email', "none")
    locale = data.get("locale", "en") # TODO: Check that only can be 3 values en, es, gr

    # If user does not exist, return error
    isUser = User.query.filter_by(email=mail)
    if isUser.count()==0:
        return jsonify({ 'message': 'User does not exist', 'code': 'failedRecover' }), 409

    recoverDate = datetime.now()
    userDb = isUser.first()
    strHash = f"{str(userDb.id)}{userDb.email}{str(recoverDate)}"
    mailHash = hashlib.sha224(strHash.encode('utf-8')).hexdigest()
    userDb.recoverHash = mailHash
    userDb.recoverDate = recoverDate
    db.session.commit()

    # Read the template mail content
    with open(f"../static/recover_mail_{locale}.html", 'r') as file :
      filedata = file.read()

    # Find title in the confirmation file
    pattern = re.split("title", filedata)
    pattern = pattern[1][1:-2]

    # Replace the target string
    msg = Message(pattern, recipients = [mail])
    msg.html = str(filedata.replace('TAGTOCHANGE', f"http://{FRONT_END_URI}/introPassword/?mail={userDb.email}&key={mailHash}"))
    current_app.mail.send(msg)
    return jsonify({"email": mail}), 200

# Function that change the password of one user. The data are the email, password and the token
@users.route('/changePassword/', methods=('POST',))
def changePassword():
    data = request.get_json()
    mail = data.get('email', "none")
    password = data['password']
    hash = data.get('key','1')

    # If user does not exist, return error
    isUser = User.query.filter_by(email=mail)
    if isUser.count()==0:
        return jsonify({ 'message': 'User does not exist', 'code': 'failedIntroduce' }), 409


    userDb = isUser.first()
    # la recoveryDate es menor de un día. Puede ser que recoverData sea nulo?????????
    yesterday = datetime.now() - timedelta(days=1)
    if userDb.recoverDate < yesterday :
        return jsonify({ 'message': 'Too much time to change the password', 'code': 'toomuchTimeIntroduce' }), 409

    # If hashs match change password. Else, Error.
    if userDb.recoverHash == hash :
        userDb.password = generate_password_hash(password, method='sha256')
        userDb.recoverDate = None
        db.session.commit()
        return jsonify({"email": mail}), 201
    else :
        return jsonify({ 'message': 'Hashes does not match', 'code': 'failedIntroduce' }), 409
"""
LOGIN
- Function that manage login
if user email does not exists, login error.
if user password does not exists, login error.

"""

@users.route('/login/', methods=('POST',))
def login():
    data = request.get_json()
    user = User.authenticate(**data)
    if not user:
        return jsonify({ 'message': 'Invalid credentials', 'code': 'authenticationFailedLogin' }), 400

    if not user.confirmed:
        return jsonify({ 'message': 'Not confirmed yet', 'code': 'notYetConfirmatedLogin' }), 409

    token = jwt.encode(payload={"sub": user.email,
        "iat":int(time.time()),
        "exp":int(time.time() + timedelta(minutes = 180).total_seconds())},
    key=current_app.config['SECRET_KEY'],
    algorithm="HS256")

    return jsonify({ 'token': token, 'role': user.role })


"""
token_required
- Function that manage the token received by the call.
"""
def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401
        try:
            token = auth_headers[1]
            # data = jwt.decode(token, current_app.config['SECRET_KEY'])
            data = jwt.decode(jwt=token,
            key=current_app.config['SECRET_KEY'],
            algorithms=["HS256"])
            user = User.query.filter_by(email=data['sub']).first()
            #print(user)
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args,**kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401 # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify




