# Importações 

import sqlite3 

# Classe para conectar no banco de dados
class DatabaseConnection:
    def __init__(self, db_file):
        self.db_file = db_file
       
    def connect(self):
        with sqlite3.connect(self.db_file) as db:
            try:
                cursor = db.cursor()
                return cursor
            except sqlite3.OperationalError:
                return 'Fail'


class QueryHandler:
    def __init__(self, cursor):
        self.cursor = cursor
       
    def create_table(self, sql):
        return self.cursor.execute(sql)
   
db_connection = DatabaseConnection('dados.db').connect()


query_handler = QueryHandler(db_connection).create_table("""
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sexo TEXT(2) NOT NULL,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password UNIQUE NOT NULL
            )
            """)


