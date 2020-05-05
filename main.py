from flask import Flask
# importando la libreria flask restx
from flask_restx import Resource

from server import *
# importando los modelos
from models import *

from controllers.userController import UserController,UserPostController, UserOrderController, UserSearchController, UserStateController, UserLastConnectionController
from controllers.userController import UserController,UserPostController
from controllers.loginController import LoginController

user = api.namespace('api',description='User API')
user.add_resource(UserPostController,'/user')
user.add_resource(UserController,'/user/<int:id>')
user.add_resource(UserOrderController,'/user/order/<string:orden>')
user.add_resource(UserSearchController,'/user/search/<string:nombre>')
user.add_resource(UserStateController,'/user/state')

user.add_resource(UserLastConnectionController,'/user/active/connection')


login = api.namespace('api', description='Login API')
login.add_resource(LoginController, '/login')


if __name__ == "__main__":
	app.run(port=8000, debug=True)

