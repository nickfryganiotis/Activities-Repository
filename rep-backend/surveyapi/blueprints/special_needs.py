from flask import request
from models import db, Special_need
from flask import Blueprint
special_needs = Blueprint('special_needs', __name__)

@special_needs.route('/create_special_need/', methods=['POST'])
def create_special_need():
        if request.method=="POST":
            data = request.get_json()
            new_special_need = Special_need(code=data['code'])
            try:
                db.session.add(new_special_need)
                db.session.commit() 
                return {"code": new_special_need.code}
            except:
                return "Error" 
        else:
            return "Error"