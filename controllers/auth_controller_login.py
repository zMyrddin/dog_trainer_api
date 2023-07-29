from flask import Blueprint, request
from init import db, bcrypt
from models.customer import Customer, customer_schema, customers_schema
from models.trainer import Trainer, trainer_schema, trainers_schema
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from datetime import timedelta


auth_login_bp = Blueprint('/auth/login', __name__, url_prefix='/auth/login')

@auth_login_bp.route('/customer', methods=['POST'])
def auth_logincustomer():
    body_data = request.get_json()
    stmt = db.select(Customer).filter_by(email=body_data.get('email'))
    customer = db.session.scalar(stmt)
    if customer and bcrypt.check_password_hash(customer.password, body_data.get('password')):
        token = create_access_token(identity=str(customer.id), expires_delta=timedelta(days=1))
        return { 'email': customer.email, 'token': token, 'is_admin': customer.is_admin }
    else:
        return { 'error': 'Invalid email or password' }, 401
    
@auth_login_bp.route('/trainer', methods=['POST'])
def auth_logintrainer():
    body_data = request.get_json()
    stmt = db.select(Trainer).filter_by(email=body_data.get('email'))
    trainer = db.session.scalar(stmt)
    if trainer and bcrypt.check_password_hash(trainer.password, body_data.get('password')):
        token = create_access_token(identity=str(trainer.id), expires_delta=timedelta(days=1))
        return { 'email': trainer.email, 'token': token}
    else:
        return { 'error': 'Invalid email or password' }, 401