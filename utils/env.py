import os

# VARIABLES DEL SERVICIO
os.environ["PORTA"]="80"
# en desarrollo
# os.environ["DEBUG"]="TRUE"
# en produccion
os.environ["DEBUG"]="FALSE"

# variables para la Base de Datos (por defecto sqlite)

os.environ["BD"]          = 'mysql'
os.environ["HOST"]        = 'database-project-pachaqtec.cyzimxz00kka.us-east-1.rds.amazonaws.com'
os.environ["DATABASE"]    = 'pachaqtecDB'
os.environ["PORTBD"]        = '3306'
os.environ["USER"]        = 'adminmaster'
os.environ["PASSWORD"]    = 'adminmaster2020'


#probando mysql en mi local
# os.environ["BD"]          = 'mysql'
# os.environ["HOST"]        = 'localhost'
# os.environ["DATABASE"]    = 'alchemy'
# os.environ["PORTBD"]        = '3306'
# os.environ["USER"]        = 'root'
# os.environ["PASSWORD"]    = 'root'







