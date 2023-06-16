from flask import request
from models import db, Competency
from flask import Blueprint, jsonify
competencies = Blueprint('competencies', __name__)

@competencies.route('/create_competency/', methods=['POST'])
def create_competency():
        
        if request.method=="POST":

            code = request.get_json()['code']
            new_competency = Competency(code=code)
            try:

                db.session.add(new_competency)
                db.session.commit() 
                return jsonify(new_competency.to_dict()), 201
            
            except:

                return "Error"
             
        else:

            return "Error"