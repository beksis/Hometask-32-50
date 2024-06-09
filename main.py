from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models import Base
from database.carservice import CarService

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

car_service = CarService()

@app.get("/cars/")
def read_cars(db: Session = Depends(get_db)):
    return car_service.get_cars(db)

@app.get("/cars/{car_id}")
def read_car(car_id: int, db: Session = Depends(get_db)):
    car = car_service.get_car_by_id(db, car_id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@app.post("/cars/")
def create_car(name: str, description: str, price: int, category_id: int, db: Session = Depends(get_db)):
    return car_service.add_car(db, name, description, price, category_id)

@app.put("/cars/{car_id}")
def update_car(car_id: int, name: str, description: str, price: int, category_id: int, db: Session = Depends(get_db)):
    car = car_service.update_car(db, car_id, name, description, price, category_id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@app.delete("/cars/{car_id}")
def delete_car(car_id: int, db: Session = Depends(get_db)):
    car = car_service.delete_car(db, car_id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return {"detail": "Car deleted"}
