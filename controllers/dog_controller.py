from flask import Blueprint, request
from init import db
from models.dog import Dog, dog_schema, dogs_schema
from models.customer import Customer
from controllers.function_controller import authorise_as_admin
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
        dog.customer_id = get_jwt_identity()
        
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
    

@dog_bp.route('/update/<int:id>', methods=['PUT','PATCH'])
@jwt_required()
@authorise_as_admin
def update_dog(id):
    body_data = dog_schema.load(request.get_json(), partial=True)
    stmt = db.select(Dog).filter_by(id=id)
    dog = db.session.scalar(stmt)
    if dog:
        dog.dog_name = body_data.get('dog_name') or dog.dog_name
        dog.breed = body_data.get('breed') or dog.breed
        dog.size = body_data.get('size') or dog.size
        db.session.commit()
        return dog_schema.dump(dog), 200
    else:
        return {'error': f'Dog with ID: {id} does not exist or has already been deleted'}, 404     


# @dog_bp.route('/update/<int:id>', methods=['PUT','PATCH'])
# @jwt_required()
# def update_dog(id):
#     body_data = dog_schema.load(request.get_json(), partial=True)
#     stmt = db.select(Dog).filter_by(id=id)
#     dog = db.session.scalar(stmt)
    
#     if dog:
#         current_customer_id = get_jwt_identity()
#         if dog.customer_id != current_customer_id:
#             return {'error': 'You are not allowed to update details for this dog.'}, 403
        
#         dog.dog_name = body_data.get('dog_name', dog.dog_name)
#         dog.breed = body_data.get('breed', dog.breed)
#         dog.size = body_data.get('size', dog.size)
#         db.session.commit()
#         return dog_schema.dump(dog), 200
#     else:
#         return {'error': f'Dog with ID: {id} does not exist or has already been deleted'}, 404


@dog_bp.route('/delete/<int:id>', methods=['DELETE'])
@jwt_required()
@authorise_as_admin
def delete_dog(id):
    dog = Dog.query.get(id)
    if dog:
        db.session.delete(dog)
        db.session.commit()
        return {'message': f'Dog {dog.dog_name} deleted successfully.'}, 200
    else:
        return {'error': f'Dog with ID: {id} does not exist or has already been deleted'}, 404    
    