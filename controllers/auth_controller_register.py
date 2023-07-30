from flask import Blueprint, request
from init import db, bcrypt
from models.customer import Customer, customer_schema, customers_schema
from models.trainer import Trainer, trainer_schema, trainers_schema
from models.dog import Dog, dog_schema, dogs_schema
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from controllers.function_controller import authorise_as_admin
from flask_jwt_extended import jwt_required


auth_register_bp = Blueprint('/auth/register', __name__, url_prefix='/auth/register')

# registration route for new customers
@auth_register_bp.route('/customer', methods=['POST'])
def auth_registercustomer():
    try:

        body_data = customer_schema.load(request.get_json())
        
        customer = Customer() 
        customer.customer_name = body_data.get('customer_name')
        customer.email = body_data.get('email')
        customer.password = bcrypt.generate_password_hash(body_data.get('password')).decode('utf-8')

        db.session.add(customer)

        db.session.commit()

        return {'message': f'New Customer {customer.customer_name} profile created successfully.'}, 201

    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return { 'error': 'Email address already in use' }, 409
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            custom_messages = {
            'customer_name': 'Customer Name is required',
            'email': 'Email is required',
            'password': 'Password is required',
            }
        column_name = err.orig.diag.column_name
        error_message = custom_messages.get(column_name)
        if not error_message:
            error_message = f'The {column_name} is required'
        return {'error': error_message}, 409  


# Registration route for new trainers. This can only be done by admins as they will be interviewing trainers or be tasked to do this by the owners.
@auth_register_bp.route('/trainer', methods=['POST'])
@jwt_required()
@authorise_as_admin
def auth_registertrainer():
    try:
        body_data = request.get_json()
        
        trainer = Trainer() 
        trainer.trainer_name = body_data.get('trainer_name')
        trainer.email = body_data.get('email')
        trainer.password = bcrypt.generate_password_hash(body_data.get('password')).decode('utf-8')
        trainer.skills = body_data.get('skills')

        db.session.add(trainer)

        db.session.commit()

        return {'message': f'New Trainer {trainer.trainer_name} with {trainer.skills} skills added into the system successfully.'}, 201
    
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return { 'error': 'Email address already in use' }, 409
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            custom_messages = {
            'trainer_name': 'Trainer Name is required',
            'email': 'Email is required',
            'password': 'Password is required',
            'skills': 'Skills is required',
            }
        column_name = err.orig.diag.column_name
        error_message = custom_messages.get(column_name)
        if not error_message:
            error_message = f'The {column_name} is required'
        return {'error': error_message}, 409  
    
#  The dog registration route has been moved to the dog controller via a login done by a customer.
# @auth_register_bp.route('/dog', methods=['POST'])
# def auth_registerdog():
#     try:
#         body_data = request.get_json()
        
#         dog = Dog() 
#         dog.dog_name = body_data.get('dog_name')
#         dog.size = body_data.get('size')
#         dog.breed = body_data.get('breed')
        

#         db.session.add(dog)

#         db.session.commit()

#         return {'message': f'New dog {dog.dog_name} added successfully.'}, 201
#     except IntegrityError as err:
#         if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
#             custom_messages = {
#             'dog_name': 'Dog Name is required',
#             'customer_name': 'Owner Name is required',
#             }
#         column_name = err.orig.diag.column_name
#         error_message = custom_messages.get(column_name)
#         if not error_message:
#             error_message = f'The {column_name} is required'
#         return {'error': error_message}, 409