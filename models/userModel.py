# importando el init
from . import db,ma
import datetime
from flask_bcrypt import generate_password_hash, check_password_hash

# la clase user creara la tabla users en la base de datos
class User(db.Model):
    __tablename__ ='users'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45),  nullable=False)
    apellido = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(115), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    movil       = db.Column(db.String(15), unique=True, nullable=False)
    fechaNacimiento = db.Column(db.Date, default=datetime.datetime.now())
    foto = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text(),nullable=False)
    estado_id = db.Column(db.Integer, db.ForeignKey('estados.id'))
    sede_id = db.Column(db.Integer, db.ForeignKey('sedes.id'))
    conexion = db.relationship('Conexion', backref='user', lazy=True)
    
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Estado(db.Model):
    __tablename__ ='estados'

    id = db.Column(db.Integer, primary_key=True)
    nombreEstado = db.Column(db.String(45), unique=True, nullable=False)
    users= db.relationship('User', backref='estado', lazy=True)

class Sede(db.Model):
    __tablename__ ='sedes'

    id = db.Column(db.Integer, primary_key=True)
    nombreSede = db.Column(db.String(100), unique=True, nullable=False)
    users= db.relationship('User', backref='sede', lazy=True)

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id","nombre","apellido","password","email","movil","fechaNacimiento","foto","description","estado_id","sede_id")

userSchema = UserSchema()
usersSchema = UserSchema(many=True)

class EstadoSchema(ma.Schema):
    class Meta:
        fields = ("id","nombreEstado")

estadoSchema = EstadoSchema()
estadosSchema = EstadoSchema(many=True)

# ************************************
class Conexion(db.Model):
    __tablename__ = 'detalle_conexion'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    create_At = db.Column(db.DateTime, default=datetime.datetime.now())