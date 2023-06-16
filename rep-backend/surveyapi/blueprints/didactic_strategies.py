from flask import request
from models import db, Didactic_strategy
from flask import Blueprint, jsonify
didactic_strategies = Blueprint('didactic_strategies', __name__)

@didactic_strategies.route('/create_didactic_strategy/', methods=['POST'])
def create_didactic_strategy():
        
        if request.method=="POST":

            code = request.get_json()['code']
            new_didactic_strategy = Didactic_strategy(code=code)
            try:
                
                db.session.add(new_didactic_strategy)
                db.session.commit() 
                return jsonify(new_didactic_strategy.to_dict()), 201
            
            except:
            
                return "Error" 
        
        else:
        
            return "Error"