from flask import Flask
# importando la libreria flask restx
from flask_restx import Api, Resource

# Configuración Inicial Flask
app = Flask(__name__)

# importando los modelos
from models.userModel import *

# instancia de la clase Api
api = Api(
        app,
        title='Proyecto Final Backend',
        version='1.0',
        description='aplicacion CRUD',
    )

# endpoint de prueba
@api.route('/hello', endpoint='hola')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


if __name__ == "__main__":
	app.run(port=8080, debug=True)

