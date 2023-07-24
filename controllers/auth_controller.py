from flask import Blueprint, request
from init import db, bcrypt
from models.customer import Customer, customer_schema, customers_schema
from models.trainer import Trainer, trainer_schema, trainers_schema
from models.dog import Dog, dog_schema, dogs_schema
from flask_jwt_extended import create_access_token


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register/customer', methods=['POST'])
def auth_registercustomer():
    body_data = request.get_json()
    
    customer = Customer() 
    customer.customer_name = body_data.get('name')
    customer.email = body_data.get('email')
    customer.password = bcrypt.generate_password_hash(body_data.get('password')).decode('utf-8')

    db.session.add(customer)

    db.session.commit()

    return {'message': f'New Customer {customer.customer_name} profile created successfully.'}, 201

@auth_bp.route('/register/trainer', methods=['POST'])
def auth_registertrainer():
    body_data = request.get_json()
    
    trainer = Trainer() 
    trainer.trainer_name = body_data.get('name')
    trainer.email = body_data.get('email')
    trainer.password = bcrypt.generate_password_hash(body_data.get('password')).decode('utf-8')
    trainer.skills = body_data.get('skills')

    db.session.add(trainer)

    db.session.commit()

    return {'message': f'New Trainer {trainer.trainer_name} with {trainer.skills} skills added into the system successfully.'}, 201


@auth_bp.route('/register/dog', methods=['POST'])
def auth_registerdog():
    body_data = request.get_json()
    
    dog = Dog() 
    dog.dog_name = body_data.get('name')
    dog.size = body_data.get('size')
    dog.breed = body_data.get('breed')
    

    db.session.add(dog)

    db.session.commit()

    return {'message': f'New dog {dog.dog_name} added successfully.'}, 201