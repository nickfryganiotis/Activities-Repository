from flask import request
from models import db, Special_need
from flask import Blueprint, jsonify
special_needs = Blueprint('special_needs', __name__)

@special_needs.route('/create_special_need/', methods=['POST'])
def create_special_need():
        
        if request.method=="POST":

            code = request.get_json()['code']
            new_special_need = Special_need(code=code)
            try:
                
                db.session.add(new_special_need)
                db.session.commit() 
                return jsonify(new_special_need.to_dict()), 201
            
            except:
            
                return "Error" 
        
        else:
            
            return "Error"