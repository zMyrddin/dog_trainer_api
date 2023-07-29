from flask import Blueprint, request
from init import db, bcrypt
from models.trainer import Trainer, trainer_schema, trainers_schema
from controllers.function_controller import authorise_as_admin
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
    

@trainer_bp.route('/update/<int:id>', methods=['PUT','PATCH'])
@jwt_required()
@authorise_as_admin
def update_trainer(id):
    body_data = trainer_schema.load(request.get_json(), partial=True)
    stmt = db.select(Trainer).filter_by(id=id)
    trainer = db.session.scalar(stmt)
    if trainer:
        trainer.trainer_name = body_data.get('trainer_name', trainer.trainer_name)
        trainer.email = body_data.get('email', trainer.email)

        # Update password conditionally
        new_password = body_data.get('password')
        if new_password:
            trainer.password = bcrypt.generate_password_hash(new_password)

        trainer.skills = body_data.get('skills', trainer.skills)

        db.session.commit()
        return trainer_schema.dump(trainer), 200
    else:
        return {'error': f'Trainer with ID: {id} does not exist or has already been deleted'}, 404    


@trainer_bp.route('/delete/<int:id>', methods=['DELETE'])
@jwt_required()
@authorise_as_admin
def delete_trainer(id):
    trainer = Trainer.query.get(id)
    if trainer:
        db.session.delete(trainer)
        db.session.commit()
        return {'message': f'Trainer {trainer.trainer_name} deleted successfully.'}, 200
    else:
        return {'error': f'Trainer with ID: {id} does not exist or has already been deleted'}, 404    