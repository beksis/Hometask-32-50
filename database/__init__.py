# Импортируем библиотеку для создания движка
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Указываем тип БД (Sqlite, Postgres...)
SQLALCHEMY_DATABASE_URI = 'sqlite:///car_shop.db'
# Создаем движок
engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread': False})
# Создаем сессию для хранения данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Создаем полноценную БД
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
