# Instalamos las librerías:
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Motor de la base de datos (SQLite):
engine = create_engine('sqlite:///database/tareas.db', connect_args={'check_same_thread': False})

# Sesión (para haceer solicitudes a la base de datos):
Session = sessionmaker(bind=engine)
session = Session() # Creación de la sesión para interactuar con la base de datos
Base = declarative_base()