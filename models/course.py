from init import db, ma
from marshmallow import fields
from models.trainer import Trainer, trainer_schema, trainers_schema
from models.dog import Dog, dog_schema, dogs_schema

class Course(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String, nullable=False)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'), nullable=True)
    dog_id = db.Column(db.Integer, db.ForeignKey('dog.id'), nullable=True)

    trainer = db.relationship('Trainer', back_populates='courses')
    dog = db.relationship('Dog', back_populates='course')


class CourseSchema(ma.Schema):
    trainer = fields.Nested('TrainerSchema', only=['id', 'trainer_name'], required = False)
    dog = fields.Nested('DogSchema', only=['id', 'dog_name'], required = False)

    class Meta:
        fields = ('id', 'course_name', 'trainer_id', 'dog_id', 'trainer', 'dog')
        ordered = True


course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)
