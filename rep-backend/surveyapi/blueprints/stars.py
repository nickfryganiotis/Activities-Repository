from flask import request
from models import db, Stars
from flask import Blueprint, jsonify
from blueprints.users import token_required
stars = Blueprint('stars', __name__)

@stars.route('/add_rating/<int:activity_id>/', methods=['POST'])
@token_required
def create_competency(current_user, activity_id):
        
        if request.method=="POST":
            
            value = request.get_json()['value']
            stars = Stars.query.filter_by(user_id=current_user.id).first()
            if stars == None:  ## 1st rating case
                 
                 new_rating = Stars(value=value, activity_id=activity_id, user_id=current_user.id)
                 try:
                      
                      db.session.add(new_rating)
                      db.session.commit() 
                      return jsonify(new_rating.to_dict()), 201
                 
                 except:
                      
                      return "Error"
            
            else:
                 
                 stars.update(value)
                 db.session.commit()
                 
                 return jsonify(stars.to_dict()), 201
        else:

            return "Error"