from init import db, ma
from marshmallow import fields


class Trainer(db.Model):
    __tablename__ = 'trainers'

    id = db.Column(db.Integer, primary_key=True)
    trainer_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    skills = db.Column(db.String, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id')
                        #   , nullable=False
                          )
    
    courses = db.relationship('Course', back_populates='trainer', foreign_keys='Course.trainer_id', cascade='all, delete-orphan', single_parent=True)


class TrainerSchema(ma.Schema):
    courses = fields.Nested('CourseSchema', exclude=['trainer'])

    class Meta:
        fields = ('id', 'trainer_name', 'email', 'password', 'skills', 'course')


trainer_schema = TrainerSchema(exclude=['password'])
trainers_schema = TrainerSchema(many=True, exclude=['password'])

