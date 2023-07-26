from flask import Blueprint, request
from init import db
from models.customer import Customer, customer_schema, customers_schema
# from datetime import date
from flask_jwt_extended import get_jwt_identity, jwt_required


customer_bp = Blueprint('customer', __name__, url_prefix='/customer')

@customer_bp.route('/')
def get_all_customers():
    stmt = db.select(Customer)
    customers = db.session.scalars(stmt)
    return customers_schema.dump(customers)

@customer_bp.route('/<int:id>')
def get_one_customer(id):
    stmt = db.select(Customer).filter_by(id=id)
    customer = db.session.scalar(stmt)
    if customer:
        return customer_schema.dump(customer)
    else:
        return {'error': f'Customer not found with id {id}'}, 404
    

