from init import db, ma


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)


class CustomerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'customer_name', 'email', 'password', 'is_admin')


customer_schema = CustomerSchema(exclude=['password'])
customers_schema = CustomerSchema(many=True, exclude=['password'])

