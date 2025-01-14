# Importações 

import sqlite3 

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

# Classe para selecionar o campo de email e senha e retornar dos dados para validação de login
class SelectTable:

    def __init__(self):
        self.login_data = ConnectDatabase()

    def select_table(self, email):
        self.login_data._connect(f"SELECT email, password FROM users WHERE email='{email}'")
        return self.login_data.cur.fetchall()

# Inserindo dados na tabela users
class InsertTable:
    def __init__(self):
        self.query = ConnectDatabase()
    
    def insert_table(self, sexo, name, phone, email, password):
        self.query._connect(f"""INSERT INTO users(sexo, name, phone, email, password) 
                                VALUES ('{sexo}','{name}','{phone}','{email}','{password}')""")

db = ConnectDatabase()
db._connect("""
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sexo TEXT(10) NOT NULL,
            name TEXT NOT NULL,
            phone INT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password INT UNIQUE NOT NULL
            )
                """)




