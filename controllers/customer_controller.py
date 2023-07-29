from flask import Blueprint, request
from init import db, bcrypt
from models.customer import Customer, customer_schema, customers_schema
from controllers.function_controller import authorise_as_admin
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


@customer_bp.route('/update/<int:id>', methods=['PUT','PATCH'])
@jwt_required()
@authorise_as_admin
def update_customer(id):
    body_data = customer_schema.load(request.get_json(), partial=True)
    stmt = db.select(Customer).filter_by(id=id)
    customer = db.session.scalar(stmt)
    if not customer:
        return {'error': f'Customer with ID: {id} does not exist or has already been deleted'}, 404

    if 'password' in body_data:
        customer.password = bcrypt.generate_password_hash(body_data['password'])

    customer.customer_name = body_data.get('customer_name', customer.customer_name)
    customer.email = body_data.get('email', customer.email)

    try:
        db.session.commit()
        return customer_schema.dump(customer), 200
    except Exception as e:
        db.session.rollback()
        return {'error': 'Failed to update customer.'}, 500



@customer_bp.route('/delete/<int:id>', methods=['DELETE'])
@jwt_required()
@authorise_as_admin
def delete_customer(id):
    customer = Customer.query.get(id)
    if customer:
        db.session.delete(customer)
        db.session.commit()
        return {'message': f'Customer {customer.customer_name} deleted successfully.'}, 200
    else:
        return {'error': f'Customer with ID: {id} does not exist or has already been deleted'}, 404    
