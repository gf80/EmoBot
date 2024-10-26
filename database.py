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
    

# Модель Tests
class Test(Base):
    __tablename__ = 'tests'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    content = Column(String)

    # Связь с результатами тестов
    results = relationship("Result", back_populates="test")
    

# Модель Results
class Result(Base):
    __tablename__ = 'results'
    
    id_user = Column(Integer, ForeignKey('users.id'))
    id_test = Column(Integer, ForeignKey('tests.id'))
    date_passed = Column(DateTime, default=datetime.utcnow, primary_key=True)
    score = Column(Integer)

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

# Функция для создания результата по прохождению теста
def create_result_test(session, id_user, id_test, score):
    result = Result(id_user=id_user, id_test=id_test, score=score)
    session.merge(result)
    session.commit()
    print(f"Тест {id_test} - {score}")


def create_test(session, id, name, content):
    test = Test(id=id, name=name, content=content)
    session.merge(test)
    session.commit()
    print(f"Тест {name} добавлен!")


def get_tests(session, id_user):
    result = (
        session.query(Test.id, Test.name)
        .join(Result, Result.id_test == Test.id)
        .filter(Result.id_user == id_user)
        .distinct()
        .all()
    )
    return [{"id": row.id, "name": row.name} for row in result]

def get_results_last_month(session, id_user, id_test):
    now = datetime.utcnow()
    month_ago = now - timedelta(days=30)

    results = session.query(Result).filter(
        Result.id_user == id_user,
        Result.id_test == id_test,
        Result.date_passed >= month_ago
    ).all()

    return results

session: Session = init_db()