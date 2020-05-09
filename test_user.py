import unittest
from copy import deepcopy
from application import app, db

from connection import *
from utils import *
import json

BASE_URL = "http://localhost:80/api/user"
GOOD_URL = f"{BASE_URL}/1"
BAD_URL = f"{BASE_URL}/18"


import mysql.connector

class TestConnection(unittest.TestCase):
    connection = None
    #Metodo para configurar nuestro ambiente de pruebas (en MYSQL) antes de ejecutar las mismas
    #devuelve status 401 por temas de autenticacion del JWT
    def setUp(self):
        app.config['TESTING']=True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['URI'] ='mysql+mysqlconnector://adminmaster:adminmaster2020@database-project-pachaqtec.cyzimxz00kka.us-east-1.rds.amazonaws.com:3306/pachaqtecDB'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        pass
      
    #Prueba de listar todos los usuarios 
    #devuelve status 401 por temas de autenticacion del JWT
    def test_getALL(self):
        response = self.app.get(BASE_URL)
        self.assertEqual(401, response.status_code)
    
    #Prueba para crear un usuario segun tipo de datos de BD MYSQL 
    #devuelve status 401 por temas de autenticacion del JWT
    def test_create(self):
        payload =  json.dumps({
        "apellido": "gonzales",
        "fechaNacimiento": "1990-01-02",
        "last_connection": "2020-05-08T11:54:25",
        "nombre": "ricardo",
        "id": 1,
        "password": "ricardo2020",
        "movil": "+51987456321",
        "description": "Front-End",
        "especialidad_id": 2,
        "foto": "https://fotosbackend.s3.amazonaws.com/person1.jpeg",
        "email": "ricardo@correo.com",
        "sede_id": 1,
        "estado_id": 1
        })
        response = self.app.post(BASE_URL,headers={"Content-Type":"application/json"}, data=payload)
        self.assertEqual(401,response.status_code)
        
    #Prueba para actualizar un usuario segun tipo de datos de BD MYSQL 
    #devuelve status 401 por temas de autenticacion del JWT    
    def test_put(self):
        response = self.app.put(GOOD_URL)
        self.assertEqual(401, response.status_code)
        
    #Prueba para eliminar un usuario segun tipo de datos de BD MYSQL 
    #devuelve status 401 por temas de autenticacion del JWT
    def test_delete(self):
        response = self.app.delete(GOOD_URL)
        self.assertEqual(401, response.status_code)
        
if __name__ == '__main__':
    unittest.main()
