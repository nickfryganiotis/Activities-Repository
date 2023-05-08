from flask import request
from models import db, Competence
from flask import Blueprint
create_subarrays_api = Blueprint('create_subarrays', __name__)

@create_subarrays_api.route('/create_competence', methods=['POST'])
def create_competence():
        if request.method=="POST":
            data = request.get_json()
            new_competence = Competence(code=data['code'])
            try:
                db.session.add(new_competence)
                db.session.commit() 
                return {"code": new_competence.code}
            except:
                return "Error" 
        else:
            return "Error"
