from flask import Flask
# importando la libreria flask restx
from flask_restx import Resource

from server import *
# importando los modelos
from models import *

from controllers.userController import UserController,UserPostController, UserOrderController, UserSearchController

user = api.namespace('api',description='User API')
user.add_resource(UserPostController,'/user')
user.add_resource(UserController,'/user/<int:id>')
user.add_resource(UserOrderController,'/user/order/<string:orden>')
user.add_resource(UserSearchController,'/user/search/<string:nombre>')


# endpoint de prueba
# @api.route('/buenas', endpoint='hola')
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}


if __name__ == "__main__":
	app.run(port=8000, debug=True)

