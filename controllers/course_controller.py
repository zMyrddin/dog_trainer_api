from flask import Blueprint, request
from init import db
from models.course import Course, course_schema, courses_schema
from models.trainer import Trainer
from models.dog import Dog
from flask_jwt_extended import jwt_required

course_bp = Blueprint('course', __name__, url_prefix='/course')

@course_bp.route('/', methods=['GET'])
def get_all_courses():
    stmt = db.select(Course)
    courses = db.session.scalars(stmt)
    return courses_schema.dump(courses)

@course_bp.route('/<int:id>')
def get_one_course(id):
    stmt = db.select(Course).filter_by(id=id)
    course = db.session.scalar(stmt)
    if course:
        return course_schema.dump(course)
    else:
        return {'error': f'Course not found with id {id}'}, 404

@course_bp.route('/create', methods=['POST'])
@jwt_required()
def add_course():
    body_data = request.get_json()
    course = Course()
    course.trainer_id = body_data.get('trainer_id')
    course.dog_id = body_data.get('dog_id')
    course_name = body_data.get('course_name')

    # # Check if the trainer with given ID exists
    trainer = Trainer.query.get(trainer_id)
    if not trainer:
        return {'error': f'Trainer not found with id {trainer_id}'}, 404

    # # Check if the dog with given ID exists
    dog = Dog.query.get(dog_id)
    if not dog:
        return {'error': f'Dog not found with id {dog_id}'}, 404

    db.session.add(course)
    db.session.commit()

    return {'message': f'Course {course_name} added successfully.'}, 201

@course_bp.route('/create/courseonly', methods=['POST'])
@jwt_required()
def add_courseonly():
    body_data = request.get_json()
    course = Course()
    course.course_name = body_data.get('course_name')

    db.session.add(course)
    db.session.commit()

    return {'message': f'Course {course.course_name} added successfully.'}, 201

@course_bp.route('/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_course(id):
    course = Course.query.get(id)
    if course:
        db.session.delete(course)
        db.session.commit()
        return {'message': f'Course {course.course_name} deleted successfully.'}, 200
    else:
        return {'error': f'Course not found with id {id}'}, 404
