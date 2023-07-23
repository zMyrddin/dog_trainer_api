from flask import Blueprint
from init import db, bcrypt
from models.customer import Customer
from models.trainer import Trainer
from models.dog import Dog

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_all():
    db.create_all()
    print('Tables Created')

@db_commands.cli.command('drop')
def drop_all():
    db.drop_all()
    print('Tables Dropped')


@db_commands.cli.command('seed')
def seed_db():
    customers = [
        Customer(
            name='Dog Admin',
            email='admin@dogtrainer.com',
            password=bcrypt.generate_password_hash('dogmaster').decode('utf-8'),
            is_admin=True
        ),
        Customer(
            name='Poh Tato',
            email='poh@tato.com',
            password=bcrypt.generate_password_hash('pohtato').decode('utf-8'),
        ),        
        Customer(
            name='Pia Toes',
            email='pia@toes.com',
            password=bcrypt.generate_password_hash('piatoes').decode('utf-8'),
        ),
        Customer(
            name='Sam Song',
            email='sam@song.com',
            password=bcrypt.generate_password_hash('samsong').decode('utf-8'),
        ),        
        Customer(
            name='Otto Man',
            email='otto@man.com',
            password=bcrypt.generate_password_hash('ottoman').decode('utf-8'),
        ),
    ]
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
        ),        
    ]
    dogs = [
        Dog(
            dog_name='Rambo',

        )
    ]

    db.session.add_all(customers)
    db.session.add_all(trainers)
    db.session.add_all(dogs)
    db.session.commit()

    print("Tables Seeded")

 

    