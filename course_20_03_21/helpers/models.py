from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base

DB_NAME = 'resaturants.db'
engine = create_engine(f'sqlite:///{DB_NAME}', echo=True)

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'
    restaurant_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    image_url = Column(String)
    open_hours = Column(String)
    name_id = Column(String, unique=True)

metadata = Base.metadata

if __name__ == '__main__':
    metadata.create_all(engine)
