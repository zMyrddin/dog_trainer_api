from init import db, ma
from marshmallow import fields


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
    
    dogs = fields.List(fields.Nested('DogSchema', exclude=['customer']))

    class Meta:
        fields = ('id', 'customer_name', 'email', 'password', 'is_admin', 'dogs')


customer_schema = CustomerSchema(exclude=['password'])
customers_schema = CustomerSchema(many=True, exclude=['password'])

