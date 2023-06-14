from flask import request
from models import db, Didactic_strategy
from flask import Blueprint
didactic_strategies = Blueprint('didactic_strategies', __name__)

@didactic_strategies.route('/create_didactic_strategy/', methods=['POST'])
def create_didactic_strategy():
        if request.method=="POST":
            data = request.get_json()
            new_didactic_strategy = Didactic_strategy(code=data['code'])
            try:
                db.session.add(new_didactic_strategy)
                db.session.commit() 
                return {"code": new_didactic_strategy.code}
            except:
                return "Error" 
        else:
            return "Error"