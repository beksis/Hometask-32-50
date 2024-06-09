from sqlalchemy.orm import Session
from .models import Cars
from .models import CategoryCars


class CarService:

    def get_cars(self, db: Session):
        return db.query(Cars).all()

    def get_car_by_id(self, db: Session, car_id: int):
        return db.query(Cars).filter(Cars.id == car_id).first()

    def add_car(self, db: Session, name: str, description: str, price: int, category_id: int):
        new_car = Cars(name=name, description=description, price=price, category_id=category_id)
        db.add(new_car)
        db.commit()
        db.refresh(new_car)
        return new_car

    def update_car(self, db: Session, car_id: int, name: str, description: str, price: int, category_id: int):
        car = db.query(Cars).filter(Cars.id == car_id).first()
        if car:
            car.name = name
            car.description = description
            car.price = price
            car.category_id = category_id
            db.commit()
            db.refresh(car)
        return car

    def delete_car(self, db: Session, car_id: int):
        car = db.query(Cars).filter(Cars.id == car_id).first()
        if car:
            db.delete(car)
            db.commit()
        return car
