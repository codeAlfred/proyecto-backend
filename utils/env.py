import os

# VARIABLES DEL SERVICIO
os.environ["PORTA"]="8080"
os.environ["DEBUG"]="TRUE"


# variables para la Base de Datos (por defecto sqlite)

#BD          = 'mysql'
#HOST        = 'database-project-pachaqtec.cyzimxz00kka.us-east-1.rds.amazonaws.com'
#DATABASE    = 'pachaqtecDB'
#PORT        = 3306
#USER        = 'adminmaster'
#PASSWORD    = 'adminmaster2020'


#probando mysql en mi local
os.environ["BD"]          = 'mysql'
os.environ["HOST"]        = 'localhost'
os.environ["DATABASE"]    = 'alchemy'
os.environ["PORTBD"]        = '3306'
os.environ["USER"]        = 'root'
os.environ["PASSWORD"]    = 'root'







