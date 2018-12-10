from database_setup import User, Base, Item, Category
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///itemcatalog.db',
                       connect_args={'check_same_thread': False})

# Bind the above engine to a session.
Session = sessionmaker(bind=engine)

# Create a Session object.
session = Session()

user1 = User(
    name='Chandrakant Bharti',
    email='chandrakant.bharti@gmail.com',
    picture=''
)

session.add(user1)
session.commit()

category1 = Category(
    name='Cricket',
    user=user1
)

session.add(category1)
session.commit()

item1 = Item(
    name='Bat',
    description='Use it to hit the ball and score runs.',
    category=category1,
    user=user1
)

session.add(item1)
session.commit()

category1 = Category(
    name='Soccer',
    user=user1
)

session.add(category1)
session.commit()

category1 = Category(
    name='Tennis',
    user=user1
)

session.add(category1)
session.commit()

category1 = Category(
    name='Badminton',
    user=user1
)

session.add(category1)
session.commit()

category1 = Category(
    name='Basketball',
    user=user1
)

session.add(category1)
session.commit()

category1 = Category(
    name='Baseball',
    user=user1
)

session.add(category1)
session.commit()

category1 = Category(
    name='Hockey',
    user=user1
)

session.add(category1)
session.commit()


print('Finished populating the database!')
