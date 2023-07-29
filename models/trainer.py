from init import db, ma
from marshmallow import fields


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
    password = fields.Str(required=False)

    class Meta:
        fields = ('id', 'trainer_name', 'email', 'password', 'skills', 'courses')

trainer_schema_for_update = TrainerSchema()
trainer_schema = TrainerSchema(exclude=['password'])
trainers_schema = TrainerSchema(many=True, exclude=['password'])

