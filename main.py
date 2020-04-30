from flask import Flask
# importando la libreria flask restx
from flask_restx import Resource

from server import *

# importando los modelos
from models import *


# endpoint de prueba
@api.route('/buenas', endpoint='hola')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


if __name__ == "__main__":
	app.run(port=8000, debug=True)

