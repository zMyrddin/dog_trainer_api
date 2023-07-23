from init import db, ma


class Dog(db.Model):
    __tablename__ = 'dogs'

    id = db.Column(db.Integer, primary_key=True)
    dog_name = db.Column(db.String, nullable=False)
    size = db.Column(db.String)
    breed = db.Column(db.String)


class DogSchema(ma.Schema):
    class Meta:
        fields = ('id', 'dog_name', 'size', 'breed')


# dog_schema = DogSchema(exclude=['password'])
# dogs_schema = DogSchema(many=True, exclude=['password'])

