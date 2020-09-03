from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

pet1 = Pet(name='Smokey', species='Dog', photo_url="https://media.tenor.com/images/b5db460f5847828b86fb39bfadfaedc9/tenor.png", age=3, notes='He is a good dog.')
pet2 = Pet(name='Rasta', species='Dog', photo_url='https://i.pinimg.com/originals/4d/c3/7c/4dc37c3fe56c15acc56013da0f423e16.jpg', age=12, notes='He is a calm dog')
pet3 = Pet(name='Guppie', species='Fish', photo_url='https://images-na.ssl-images-amazon.com/images/I/61yVvZLkTuL._CR204,0,1224,1224_UX256.jpg', age=8, notes='Blub blub')

db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)

db.session.commit()