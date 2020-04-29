from flask import Flask
# importando la libreria flask restx
from flask_restx import Api

# Configuración Inicial Flask
app = Flask(__name__)

# instancia de la clase Api
api = Api(
        app,
        title='Proyecto Final Backend',
        version='1.0',
        description='aplicacion CRUD',
    )



if __name__ == "__main__":
	app.run(port=8080, debug=True)

