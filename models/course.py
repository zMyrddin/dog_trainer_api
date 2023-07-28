from init import db, ma
from marshmallow import fields


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String, nullable=False)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.id')
                           , nullable = False
                           )
    dog_id = db.Column(db.Integer, db.ForeignKey('dogs.id')
                       , nullable = False
                       )

    dogs = db.relationship('Dog', back_populates='course', foreign_keys='Dog.course_id', cascade='all, delete-orphan', single_parent=True)
    trainer = db.relationship('Trainer', back_populates='courses', foreign_keys='Course.trainer_id')




class CourseSchema(ma.Schema):
    dogs = fields.List(fields.Nested('DogSchema', only=['dog_name', 'customer']))
    trainer = fields.Nested('TrainerSchema', only=['trainer_name'])

    class Meta:
        fields = ('id', 'course_name', 'dogs', 'trainer')
        ordered = True


course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

