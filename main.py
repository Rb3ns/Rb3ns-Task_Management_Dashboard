# Importamos las librerías:
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import redirect

# Importamos el resto de ficheros:
import db
from models import Tarea

# Flask nos pide que todos los ficheros html tienen que estar en una carpeta separada (index.html).
# En la carpeta templates vamos a meter los ficheros HTML y contenido web.
# En la carpeta static vamos a guardar el contenido estatico (ficheros css, video, audio,...)

app = Flask(__name__)

@app.route("/") # Definimos una ruta.
def home(): # Aquí cargaremos los ficheros html que serán la portada de mi web.
    todas_las_tareas = db.session.query(Tarea).all()
    print(todas_las_tareas)
    return  render_template("index.html", lista_de_tareas=todas_las_tareas) # El return es lo que nos hace volver a la web.

@app.route("/crear-tarea", methods=["POST"]) # Deifnimos una ruta.
def crear():
    contenido = request.form["contenido-tarea"]
    print(contenido)
    tarea=Tarea(contenido=contenido, hecha=False)
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for("home")) # Esto nos redirecciona a la función home().

@app.route("/eliminar-tarea/<id>")
def eliminar(id):
    db.session.query(Tarea).filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/tarea-hecha/<id>")
def hecha(id):
    tarea= db.session.query(Tarea).filter_by(id=int(id)).first()
    tarea.hecha = not(tarea.hecha)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == '__main__':
    db.Base.metadata.create_all(bind=db.engine) # Creamos el modelo de datos
    app.run(debug=True)