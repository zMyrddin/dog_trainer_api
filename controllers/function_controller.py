import functools
from init import db
from flask_jwt_extended import get_jwt_identity
from models.customer import Customer
from models.dog import Dog
from models.trainer import Trainer
from models.course import Course

def authorise_as_admin(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        customer_id = get_jwt_identity()
        stmt = db.select(Customer).filter_by(id=customer_id)
        customer = db.session.scalar(stmt)
        if customer.is_admin:
            return fn(*args, **kwargs)
        else:
            return {'error': 'Only admins are authorized to do this action'}, 403
    
    return wrapper


