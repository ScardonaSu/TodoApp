from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Parte	                    ¿Qué hace?

# SQLALCHEMY_DATABASE_URL =	Define dónde está y cómo conectarse a la base de datos.
# engine	              =  Crea el motor de conexión con SQLite.
# SessionLocal	          =  Crea instancias para trabajar con la base de datos.
# Base	                  =  Clase base para definir modelos/tablas con SQLAlchemy ORM.
#


SQLALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind= engine)

Base = declarative_base()


