from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp, OneOf
from marshmallow.exceptions import ValidationError


class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    dogs = db.relationship('Dog', back_populates='customer', cascade='all, delete-orphan')


class CustomerSchema(ma.Schema):
    password = fields.String(required=True, load_only=True)  
    customer_name = fields.String(required=True, validate=And(
        Length(min=2, error='Name must be at least 2 characters long'),
        Regexp('^[a-zA-Z0-9 ]+$', error='Only letters, spaces and numbers are allowed')))
    dogs = fields.List(fields.Nested('DogSchema', exclude=['customer']))

    class Meta:
        fields = ('id', 'customer_name', 'email', 'password', 'is_admin', 'dogs')



customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

