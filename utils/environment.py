import os
from dotenv import load_dotenv

load_dotenv()

class Environment:

    def settingsBD(self):
        return{
            'BD': os.getenv("BD", 'sqlLite'),
            'HOST': os.getenv("HOST", '127.0.0.1'),
            'DATABASE': os.getenv("DATABASE", 'dbTest'),
            'PORT': os.getenv("PORT", 3306),
            'USER': os.getenv("USER", 'root'),
            'PASS': os.getenv("PASSWORD", 'root'),
        }
