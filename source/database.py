# Importações 

import sqlite3 

# Classe para criar query SQL
class QueryDatabase():
    def __init__(self) -> None:
        self.db = ConnectDatabase()
   
    def query_handler(self, sql):
        self.db._connect(sql)

# Conector do banco de dados
class ConnectDatabase:
    def __init__(self):
        self.database_name = "data.db"


    def _connect(self, query):
        with sqlite3.connect(self.database_name) as con:
            try:
                self.cur = con.cursor()
                self.cur.execute(query)
            except (sqlite3.OperationalError, ValueError, KeyboardInterrupt):
                return "Fail"
            else:
                con.commit()
                print("successfull!")

# Inserindo dados na tabela users
class InsertTable:
    def __init__(self):
        self.query = QueryDatabase()
    
    def insert_table(self, sexo, name, phone, email, password):
        self.query.query_handler(f"""INSERT INTO users(sexo, name, phone, email, password) 
                                VALUES ('{sexo}','{name}','{phone}','{email}','{password}')""")

db = QueryDatabase()
db.query_handler("""
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sexo TEXT(10) NOT NULL,
            name TEXT NOT NULL,
            phone INT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password INT UNIQUE NOT NULL
            )
                """)

# db.query_handler("DROP TABLE users")

