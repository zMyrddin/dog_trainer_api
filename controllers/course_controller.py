from flask import Blueprint, request
from init import db
from models.course import Course, course_schema, courses_schema
from models.trainer import Trainer, trainer_schema, trainers_schema
from models.dog import Dog, dog_schema, dogs_schema
from controllers.function_controller import authorise_as_admin
from flask_jwt_extended import get_jwt_identity, jwt_required

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
@authorise_as_admin
def add_course():
    body_data = request.get_json()
    course = Course()
    course.trainer_id = body_data.get('trainer_id')
    course.dog_id = body_data.get('dog_id')
    course.course_name = body_data.get('course_name')

    # Check if both the trainer and the dog with given IDs exist
    trainer = Trainer.query.get(course.trainer_id)
    dog = Dog.query.get(course.dog_id)

    errors = {}

    if course.trainer_id and not trainer:
        errors['trainer_error'] = f'Trainer not found with id {course.trainer_id}'

    if course.dog_id and not dog:
        errors['dog_error'] = f'Dog not found with id {course.dog_id}'

    # If both trainer and dog are not found, return the errors
    if errors:
        return {'errors': errors}, 404

    # Either trainer and dog or just one of them exist, add the course to the database. Also add if no trainer or dog are provided
    db.session.add(course)
    db.session.commit()

    return {'message': 'Course created successfully.', 'course_id': course.id}, 201



@course_bp.route('/create/courseonly', methods=['POST'])
@jwt_required()
@authorise_as_admin
def add_courseonly():
    body_data = request.get_json()
    course = Course()
    course.course_name = body_data.get('course_name')

    db.session.add(course)
    db.session.commit()

    return {'message': f'Course {course.course_name} added successfully.'}, 201


@course_bp.route('/update/<int:id>', methods=['PUT','PATCH'])
@jwt_required()
@authorise_as_admin
def update_course(id):
    body_data = course_schema.load(request.get_json(), partial=True)
    stmt = db.select(Course).filter_by(id=id)
    course = db.session.scalar(stmt)
    if course:
        course.course_name = body_data.get('course_name') or course.course_name
        course.trainer_id = body_data.get('trainer_id') or course.trainer_id
        course.dog_id = body_data.get('dog_id') or course.dog_id
        db.session.commit()
        return course_schema.dump(course), 200
    else:
        return {'error': f'Course with ID: {id} does not exist or has already been deleted'}, 404     


@course_bp.route('/delete/<int:id>', methods=['DELETE'])
@jwt_required()
@authorise_as_admin
def delete_course(id):
    course = Course.query.get(id)
    if course:
        db.session.delete(course)
        db.session.commit()
        return {'message': f'Course {course.course_name} deleted successfully.'}, 200
    else:
        return {'error': f'Course with ID: {id} does not exist or has already been deleted'}, 404    

