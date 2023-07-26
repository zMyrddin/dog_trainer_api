from init import db, ma


class Trainer(db.Model):
    __tablename__ = 'trainer'

    id = db.Column(db.Integer, primary_key=True)
    trainer_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    skills = db.Column(db.String, nullable=False)
    

class TrainerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'trainer_name', 'email', 'password', 'skills')


trainer_schema = TrainerSchema(exclude=['password'])
trainers_schema = TrainerSchema(many=True, exclude=['password'])

