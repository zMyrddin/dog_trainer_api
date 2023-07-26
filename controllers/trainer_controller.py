from flask import Blueprint, request
from init import db
from models.trainer import Trainer, trainer_schema, trainers_schema
# from datetime import date
from flask_jwt_extended import get_jwt_identity, jwt_required


trainer_bp = Blueprint('trainer', __name__, url_prefix='/trainer')

@trainer_bp.route('/')
def get_all_trainers():
    stmt = db.select(Trainer)
    trainers = db.session.scalars(stmt)
    return trainers_schema.dump(trainers)

@trainer_bp.route('/<int:id>')
def get_one_trainer(id):
    stmt = db.select(Trainer).filter_by(id=id)
    trainer = db.session.scalar(stmt)
    if trainer:
        return trainer_schema.dump(trainer)
    else:
        return {'error': f'Trainer not found with id {id}'}, 404