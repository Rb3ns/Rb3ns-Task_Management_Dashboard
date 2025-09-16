# Importamos las librerías:
from sqlalchemy import Column, Integer, String, Table, Boolean

# Importamos el fichero db.py al fichero models.py:
import db

'''
Creamos una clase llamada tarea (que va a ser nuestro modelo de datos de la tarea).
Esta clase va a almacenar toda la información referente a una tarea.
'''

# Todo lo que herede de base tiene la capacidad de convertirse en una tabla de la base de datos.

class Tarea(db.Base): # Clase Tarea (herada de Base):
    __tablename__ = "tarea"
    id = Column(Integer, primary_key=True) # Indentificador único de cada tarea.
    contenido =  Column(String(50), nullable=False) # Contenid de la tarea, un texto máximod e 200 caracteres.
    hecha = Column(Boolean) # Booleano que indica si una tarea ha sido hecha o no hecha.

    def __init__(self,contenido, hecha):
        self.contenido = contenido
        self.hecha = hecha

    def __repr__(self):
        return "Tarea {}: {} ({})".format(self.id, self.contenido, self.hecha)

    def __str__(self):
        return "Tarea {}: {} ({})".format(self.id, self.contenido, self.hecha)