from flask import request
from models import db, Comments
from flask import Blueprint, jsonify
from blueprints.users import token_required
comments = Blueprint('comments', __name__)

@comments.route('/add_comment/<int:activity_id>/', methods=['POST'])
@token_required
def create_competency(current_user, activity_id):
        
        if request.method=="POST":
            
            value = request.get_json()['value']
            new_comment = Comments(value=value, activity_id=activity_id, user_id=current_user.id)
            try:

                db.session.add(new_comment)
                db.session.commit() 
                return jsonify(new_comment.to_dict()), 201
             
            except:

                return "Error" 
        else:

            return "Error"