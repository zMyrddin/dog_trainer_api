from init import db, ma
from marshmallow import fields, validates
from marshmallow.validate import Length, And, Regexp, OneOf
from marshmallow.exceptions import ValidationError

# This will be the reference point on Valid breeds only. 
VALID_BREEDS = (
    'Affenpinscher',
    'Afghan Hound',
    'Airedale Terrier',
    'Akita',
    'Alaskan Malamute',
    'American Bulldog',
    'American Cocker Spaniel',
    'American Eskimo Dog',
    'American Foxhound',
    'American Pit Bull Terrier',
    'American Staffordshire Terrier',
    'American Water Spaniel',
    'Anatolian Shepherd Dog',
    'Australian Cattle Dog',
    'Australian Shepherd',
    'Australian Terrier',
    'Basenji',
    'Basset Hound',
    'Beagle',
    'Bearded Collie',
    'Beauceron',
    'Bedlington Terrier',
    'Belgian Malinois',
    'Belgian Sheepdog',
    'Belgian Tervuren',
    'Bernese Mountain Dog',
    'Bichon Frise',
    'Black and Tan Coonhound',
    'Black Russian Terrier',
    'Bloodhound',
    'Border Collie',
    'Border Terrier',
    'Borzoi',
    'Boston Terrier',
    'Bouvier des Flandres',
    'Boxer',
    'Briard',
    'Brittany',
    'Brussels Griffon',
    'Bull Terrier',
    'Bulldog',
    'Bullmastiff',
    'Cairn Terrier',
    'Canaan Dog',
    'Cane Corso',
    'Cardigan Welsh Corgi',
    'Cavalier King Charles Spaniel',
    'Chesapeake Bay Retriever',
    'Chihuahua',
    'Chinese Crested',
    'Chinese Shar-Pei',
    'Chow Chow',
    'Clumber Spaniel',
    'Cocker Spaniel',
    'Collie',
    'Coonhound',
    'Corgi',
    'Coton de Tulear',
    'Curly-Coated Retriever',
    'Dachshund',
    'Dalmatian',
    'Dandie Dinmont Terrier',
    'Doberman Pinscher',
    'Dogue de Bordeaux',
    'Dalmatian',
    'English Bulldog',
    'English Cocker Spaniel',
    'English Foxhound',
    'English Setter',
    'English Springer Spaniel',
    'English Toy Spaniel',
    'Entlebucher Mountain Dog',
    'Eskimo Dog',
    'Field Spaniel',
    'Finnish Lapphund',
    'Finnish Spitz',
    'Flat-Coated Retriever',
    'French Bulldog',
    'German Pinscher',
    'German Shepherd',
    'German Shorthaired Pointer',
    'German Wirehaired Pointer',
    'Giant Schnauzer',
    'Glen of Imaal Terrier',
    'Golden Retriever',
    'Goldendoodle',
    'Gordon Setter',
    'Great Dane',
    'Great Pyrenees',
    'Greater Swiss Mountain Dog',
    'Greyhound',
    'Harrier',
    'Havanese',
    'Irish Setter',
    'Irish Terrier',
    'Irish Water Spaniel',
    'Irish Wolfhound',
    'Italian Greyhound',
    'Jack Russell Terrier',
    'Japanese Chin',
    'Keeshond',
    'Kerry Blue Terrier',
    'King Charles Spaniel',
    'Komondor',
    'Kuvasz',
    'Labradoodle',
    'Labrador Retriever',
    'Lakeland Terrier',
    'Lhasa Apso',
    'Löwchen',
    'Maltese',
    'Manchester Terrier',
    'Mastiff',
    'Miniature Bull Terrier',
    'Miniature Pinscher',
    'Miniature Schnauzer',
    'Neapolitan Mastiff',
    'Newfoundland',
    'Norfolk Terrier',
    'Norwegian Buhund',
    'Norwegian Elkhound',
    'Norwegian Lundehund',
    'Norwich Terrier',
    'Nova Scotia Duck Tolling Retriever',
    'Old English Sheepdog',
    'Otterhound',
    'Papillon',
    'Pekingese',
    'Pembroke Welsh Corgi',
    'Petit Basset Griffon Vendéen',
    'Pharaoh Hound',
    'Plott',
    'Pointer',
    'Polish Lowland Sheepdog',
    'Pomeranian',
    'Poodle',
    'Portuguese Water Dog',
    'Presbyterian Terrier',
    'Pug',
    'Puli',
    'Pumi',
    'Pyrenean Shepherd',
    'Rat Terrier',
    'Redbone Coonhound',
    'Rhodesian Ridgeback',
    'Rottweiler',
    'Saint Bernard',
    'Saluki',
    'Samoyed',
    'Schipperke',
    'Scottish Deerhound',
    'Scottish Terrier',
    'Sealyham Terrier',
    'Shetland Sheepdog',
    'Shiba Inu',
    'Shih Tzu',
    'Siberian Husky',
    'Silky Terrier',
    'Skye Terrier',
    'Sloughi',
    'Small Munsterlander Pointer',
    'Soft-Coated Wheaten Terrier',
    'Spanish Water Dog',
    'Spinone Italiano',
    'Staffordshire Bull Terrier',
    'Standard Schnauzer',
    'Sussex Spaniel',
    'Swedish Vallhund',
    'Tibetan Mastiff',
    'Tibetan Spaniel',
    'Tibetan Terrier',
    'Toy Fox Terrier',
    'Treeing Walker Coonhound',
    'Vizsla',
    'Weimaraner',
    'Welsh Springer Spaniel',
    'Welsh Terrier',
    'West Highland White Terrier',
    'Whippet',
    'Wire Fox Terrier',
    'Wirehaired Pointing Griffon',
    'Xoloitzcuintli',
    'Yorkshire Terrier'
)

# This will be the reference point on Valid sizes only. 
VALID_SIZES = (
    'Small',
    'Medium',
    'Large',
    'Giant'
)

class Dog(db.Model):
    __tablename__ = 'dog'

    id = db.Column(db.Integer, primary_key=True)
    dog_name = db.Column(db.String, nullable=False,)
    size = db.Column(db.String)
    breed = db.Column(db.String)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable = False)

    customer = db.relationship('Customer', back_populates='dogs')
    
    course = db.relationship('Course', back_populates='dog')
    

class DogSchema(ma.Schema):
    customer = fields.Nested('CustomerSchema', only=['customer_name', 'email'])
    courses = fields.List(fields.Nested('CourseSchema'))
    
    # This function will validate the info provided when creating/updating a dog's info with regards to it's breed. This will only accept information if it is in the list above.
    @validates('breed')
    def validate_breed(self, value):
        if value not in VALID_BREEDS:
            raise ValidationError(f'Invalid breed. Must be one of: {", ".join(VALID_BREEDS)} or talk to an admin to add the breed if it is valid')
    
     # This function will validate the info provided when creating/updating a dog's info with regards to it's size. This will only accept information if it is in the list above.
    @validates('size')
    def validate_size(self, value):
        if value not in VALID_SIZES:
            raise ValidationError(f'Invalid size. Must be one of: {", ".join(VALID_SIZES)}')
        

    class Meta:
        fields = ('id', 'dog_name', 'size', 'breed', 'customer', 'courses')
        ordered = True


dog_schema = DogSchema()
dogs_schema = DogSchema(many=True)

