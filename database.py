import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship, declarative_base, sessionmaker, Session
from datetime import datetime, timedelta

Base = declarative_base()

# Модель User
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    
    # Связь с результатами тестов
    results = relationship("Result", back_populates="user")
    
    # Связь с таблицей UsersTests (многие ко многим через промежуточную таблицу)
    tests = relationship("UsersTests", back_populates="user")

# Модель Tests
class Test(Base):
    __tablename__ = 'tests'
    
    id = Column(Integer, primary_key=True)
    content = Column(String)

    # Связь с результатами тестов
    results = relationship("Result", back_populates="test")
    
    # Связь с таблицей UsersTests (многие ко многим через промежуточную таблицу)
    users = relationship("UsersTests", back_populates="test")

# Модель связки Users и Tests
class UsersTests(Base):
    __tablename__ = 'users_tests'
    
    id_user = Column(Integer, ForeignKey('users.id'), primary_key=True)
    id_test = Column(Integer, ForeignKey('tests.id'), primary_key=True)

    # Связи с таблицами users и tests
    user = relationship("User", back_populates="tests")
    test = relationship("Test", back_populates="users")
    

# Модель Results
class Result(Base):
    __tablename__ = 'results'
    
    id_user = Column(Integer, ForeignKey('users.id'), primary_key=True)
    id_test = Column(Integer, ForeignKey('tests.id'), primary_key=True)
    date_passed = Column(DateTime, default=datetime.utcnow)
    score = Column(Float)

    # Связи с таблицами users и tests
    user = relationship("User", back_populates="results")
    test = relationship("Test", back_populates="results")


# Функция для создания/инициализации базы данных
def init_db():
    db_path = 'emotional_health.db'

    # Проверяем, существует ли база данных
    if not os.path.exists(db_path):
        engine = create_engine(f'sqlite:///{db_path}')
        Base.metadata.create_all(engine)  # Создаем таблицы, если базы нет
    else:
        engine = create_engine(f'sqlite:///{db_path}')

    # Настройка сессии
    Session = sessionmaker(bind=engine)
    return Session()

# Функция для создания нового пользователя
def create_user(session, id, name, age, gender):
    user = User(id=id, name=name, age=age, gender=gender)
    session.merge(user)
    session.commit()  # Подтверждаем изменения, чтобы сохранить запись
    print(f"Юзер {user.name} успешно добавлен!")

def get_user(session, id):
    return session.query(User).filter(id==id).first()

session: Session = init_db()