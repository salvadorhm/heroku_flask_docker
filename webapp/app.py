import os

from flask import Flask # libreria flask
from flask import render_template # libreria para renderizar templates
from flask import request # libreria para obtener datos de la peticion
from flask import abort # libreria para abortar peticiones
from flask import redirect # libreria para redireccionar
from flask import url_for # libreria para generar url

app = Flask(__name__)

@app.route("/",methods=['GET']) # ruta para la pagina de index
def index(): # funcion para la pagina de index
    try:
        return render_template('index.html') # retorna la pagina de index
    except Exception as error: # si hay un error
        print("Error index(): ", error) # imprime el error en consola
        return render_template('index.html') # retorna la pagina de index

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    #app.run(debug=False, host="0.0.0.0")
