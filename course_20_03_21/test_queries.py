from course_20_03_21.helpers.models import Restaurant, DB_NAME
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(f'sqlite:///{DB_NAME}')
Session = sessionmaker(bind=engine)
session = Session()

restaurant = Restaurant(name="Rest", image_url="https://sd.ads", name_id="name1234")
session.add(restaurant)

session.commit()

print(session.query(Restaurant.name).all())


