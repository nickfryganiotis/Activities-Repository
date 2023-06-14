from flask import request
from models import db, Competency
from flask import Blueprint
competencies = Blueprint('competencies', __name__)

@competencies.route('/create_competency/', methods=['POST'])
def create_competency():
        if request.method=="POST":
            data = request.get_json()
            new_competency = Competency(code=data['code'])
            try:
                db.session.add(new_competency)
                db.session.commit() 
                return {"code": new_competency.code}
            except:
                return "Error" 
        else:
            return "Error"