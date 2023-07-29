from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp, OneOf
from marshmallow.exceptions import ValidationError


class Trainer(db.Model):
    __tablename__ = 'trainer'

    id = db.Column(db.Integer, primary_key=True)
    trainer_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    skills = db.Column(db.String, nullable=False)
    
    courses = db.relationship('Course', back_populates='trainer')

class TrainerSchema(ma.Schema):
    courses = fields.List(fields.Nested('CourseSchema'))
    trainer_name = fields.String(required=True, validate=And(
        Length(min=2, error='Name must be at least 2 characters long'),
        Regexp('^[a-zA-Z0-9 ]+$', error='Only letters, spaces and numbers are allowed')))
    password = fields.Str(required=False, load_only=True)

    class Meta:
        fields = ('id', 'trainer_name', 'email', 'password', 'skills', 'courses')


trainer_schema = TrainerSchema()
trainers_schema = TrainerSchema(many=True)

