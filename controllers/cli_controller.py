from flask import Blueprint
from init import db, bcrypt
from models.customer import Customer
from models.trainer import Trainer
from models.dog import Dog
from models.course import Course

db_commands = Blueprint('db', __name__)
# Create all tables
@db_commands.cli.command('create')
def create_all():
    db.create_all()
    print('Tables Created')

# Drop all Tables
@db_commands.cli.command('drop')
def drop_all():
    db.drop_all()
    print('Tables Dropped')

# Seed all tables
@db_commands.cli.command('seed')
def seed_db():
    # Seed info for customers
    customers = [
        Customer(
            customer_name='dog_admin',
            email='admin@dogtrainer.com',
            password=bcrypt.generate_password_hash('dogmaster').decode('utf-8'),
            is_admin=True
        ),
        Customer(
            customer_name='Poh Tato',
            email='poh@tato.com',
            password=bcrypt.generate_password_hash('pohtato').decode('utf-8'),
        ),        
        Customer(
            customer_name='Pia Toes',
            email='pia@toes.com',
            password=bcrypt.generate_password_hash('piatoes').decode('utf-8'),
        ),
        Customer(
            customer_name='Sam Song',
            email='sam@song.com',
            password=bcrypt.generate_password_hash('samsong').decode('utf-8'),
        ),        
        Customer(
            customer_name='Otto Man',
            email='otto@man.com',
            password=bcrypt.generate_password_hash('ottoman').decode('utf-8'),
        )
    ]

    # Adds the customers to the session
    db.session.add_all(customers)

    # Seed info for trainers
    trainers = [
        Trainer(
            trainer_name='Sitmaster Alex',
            email='sitalex@dogtrainer.com',
            password=bcrypt.generate_password_hash('sitmaster').decode('utf-8'),
            skills='Sit'
        ),
        Trainer(
            trainer_name='Rollmaster Brad',
            email='rollbrad@dogtrainer.com',
            password=bcrypt.generate_password_hash('rollmaster').decode('utf-8'),
            skills='Roll'
        ),
        Trainer(
            trainer_name='Bangmaster Chad',
            email='bangchad@dogtrainer.com',
            password=bcrypt.generate_password_hash('bangmaster').decode('utf-8'),
            skills='Bang'
        ),
        Trainer(
            trainer_name='Standmaster Daniel',
            email='standdan@dogtrainer.com',
            password=bcrypt.generate_password_hash('standmaster').decode('utf-8'),
            skills='Stand'
        ),
        Trainer(
            trainer_name='Pawmaster Ella',
            email='pawella@dogtrainer.com',
            password=bcrypt.generate_password_hash('pawmaster').decode('utf-8'),
            skills='Paw'
        ),
        Trainer(
            trainer_name='Liemaster Farouq',
            email='liefarouq@dogtrainer.com',
            password=bcrypt.generate_password_hash('liemaster').decode('utf-8'),
            skills='Lie'
        ),   
        Trainer(
            trainer_name='Fetchmaster Gandalf',
            email='fetchgandalf@dogtrainer.com',
            password=bcrypt.generate_password_hash('fetchmaster').decode('utf-8'),
            skills='Fetch'
        ),
        Trainer(
            trainer_name='Hi5master Hillary',
            email='hi5hillary@dogtrainer.com',
            password=bcrypt.generate_password_hash('hi5master').decode('utf-8'),
            skills='Hi 5'
        ),
        Trainer(
            trainer_name='Staymaster Ignacio',
            email='stayignacio@dogtrainer.com',
            password=bcrypt.generate_password_hash('staymaster').decode('utf-8'),
            skills='Stay'
        ),
        Trainer(
            trainer_name='Playmaster Jack',
            email='playjack@dogtrainer.com',
            password=bcrypt.generate_password_hash('playmaster').decode('utf-8'),
            skills='Play'
        )        
    ]

    # Adds the trainers to the session
    db.session.add_all(trainers)
    
    # Seed info for dogs
    dogs = [
        Dog(
            dog_name='Fries',
            size='Large',
            breed='Doberman',
            customer=customers[1]  # Start indexing from 1 to skip the 'admin' customer
        ),
        Dog(
            dog_name='Chips',
            size='Medium',
            breed='Shiba Inu',
            customer=customers[2]
        ),
        Dog(
            dog_name='Galaxy',
            size='Small',
            breed='Shih Tzu',
            customer=customers[3]
        ),
        Dog(
            dog_name='Couch',
            size='Large',
            breed='Chow Chow',
            customer=customers[4]
        )
    ]

    # Adds the dogs to the session
    db.session.add_all(dogs)

    # Seed info for courses
    courses = [
        Course(
            course_name='Sit Course',
            trainer=trainers[0],  # Alex will be the teacher
            dog=dogs[3]  # Couch will be enrolled
        ),
        Course(
            course_name='Bang Course',
            trainer=trainers[2],  # Chad will be the teacher
            dog=dogs[0]  # Fries will be enrolled
        ),
        Course(
            course_name='Play course',
            trainer=trainers[9],  # Jack will be the teacher
            dog=dogs[1]  # Chips will be enrolled
        ),
        # Add more courses if needed
    ]

    # Adds the courses to the session
    db.session.add_all(courses)


    # Commits the seed info to the tables
    db.session.commit()

    print("Tables Seeded")
    