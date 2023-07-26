from flask import Blueprint, request
from init import db
from models.dog import Dog, dog_schema, dogs_schema
from models.customer import Customer
# from datetime import date
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes


dog_bp = Blueprint('dog', __name__, url_prefix='/dog')

@dog_bp.route('/')
def get_all_dogs():
    stmt = db.select(Dog)
    dogs = db.session.scalars(stmt)
    return dogs_schema.dump(dogs)

@dog_bp.route('/<int:id>')
def get_one_dog(id):
    stmt = db.select(Dog).filter_by(id=id)
    dog = db.session.scalar(stmt)
    if dog:
        return dog_schema.dump(dog)
    else:
        return {'error': f'Dog not found with id {id}'}, 404
    


@dog_bp.route('/new', methods=['POST'])
@jwt_required()
def add_dog():
    try:
        body_data = request.get_json()
        
        dog = Dog() 
        dog.dog_name = body_data.get('dog_name')
        dog.size = body_data.get('size')
        dog.breed = body_data.get('breed')
        dog.customer_id=get_jwt_identity()
        
        db.session.add(dog)

        db.session.commit()

        return {'message': f'New dog {dog.dog_name} added successfully.'}, 201
    
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            custom_messages = {
            'dog_name': 'Dog Name is required',
            'customer_name': 'Owner Name is required',
            }
        column_name = err.orig.diag.column_name
        error_message = custom_messages.get(column_name)
        if not error_message:
            error_message = f'The {column_name} is required'
        return {'error': error_message}, 409