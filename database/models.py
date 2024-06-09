from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from database import Base


class CategoryCars(Base):
    __tablename__ = 'category_cars'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True)
    datetime = Column(DateTime)

    cars = relationship("Cars", back_populates="category")


class Cars(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Integer)
    category_id = Column(Integer, ForeignKey('category_cars.id'))

    category = relationship("CategoryCars", back_populates="cars")
