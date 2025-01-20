# Importações 

from PySimpleGUI import PopupError, Popup
from hashlib import sha256
from database import InsertTable, SelectTable, QueryCodeTable
from smtp_server import CodeGenerator
import re
import time

# Classe para validação dos dados da aplicação 
class Regex:
    def __init__(self):
        
        # Expressões regulares
        self.name_regex = r"^[A-Za-záàâãéèêíïóôõöúçñ]+ [A-Za-záàâãéèêíïóôõöúçñ]+$" # Reescrever o regex do campo nome!
        self.phone_regex = r'^\s*(?:\+?(\d{1,3}))?([-. (]*(\d{3})[-. )]*)?((\d{3})[-. ]*(\d{2,4})(?:[-.x ]*(\d+))?)\s*$'
        self.email_regex = r"^[\.A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+\.[a-z]{3}(\.[a-z]{2})?$"
        self.password_regex = r'^[0-9A-Za-záàâãéèêíïóôõöúçñ"@#$%¨&*()-+={}\[\]~^,.]{4,}$'
        self.code_regex = r"^[A-Z0-9]{4}$"

# Classe para criptografar a senha do usuário com sha256
class PasswordHash:
    def __init__(self, password):
        self.password = str(password).encode()

    def encrypt(self):
        hash_password = sha256(self.password).hexdigest()
        return hash_password

# Classe para validação de login
class LoginValidation(SelectTable, PasswordHash):
    def __init__(self):
        self.regex = Regex()

    def login_validation(self, email, password):

        if re.search(self.regex.email_regex, email) == None or re.search(self.regex.password_regex, password) == None:
            PopupError("Dados Invalidos!")
            
        else:
            data_user = SelectTable().select_table(email)
            if data_user[0][0] != email or data_user[0][1] != PasswordHash(password).encrypt():
                PopupError("Senha ou Email Incorreto!")
            else:
                True

# Classe para validação de registro do usuário 
class RegisterValidation(InsertTable, PasswordHash):
    def __init__(self):
        self.regex = Regex()        

    def register_validation(self, sexo, name, phone, email, password):

        if re.search(self.regex.name_regex, name) == None or re.search(self.regex.phone_regex, phone) == None or re.search(self.regex.email_regex, email) == None or re.search(self.regex.password_regex, password) == None:
            PopupError("Dados Invalidos!")

        else:
            match sexo:
                case True:
                    sexo = "M"
                case False:
                    sexo = "F"
            InsertTable().insert_table(sexo, name, phone, email, PasswordHash(password).encrypt())
            Popup("Conta cadastrada com sucesso!")

# Classe para validação do email para recuperação de senha 
class EmailRecoveryPasswordValidation(CodeGenerator, QueryCodeTable):
    def __init__(self):
        self.email = Regex()

    def email_recovery_password_validation(self, email):
        if re.search(self.email.email_regex, email) == None:
            PopupError("Email Invalido!")
        else:
            QueryCodeTable().insert_code(CodeGenerator().code_generator())
            return True
                

# Classe para validar o código enviado para o email dos usuário 
class CodeValidation:
    def __init__(self):
        self.code = Regex()

    def stopwatch(self):
        self.sec = int()
        for self.sec in range(0, 900):
            time.sleep(1)

    def code_validation(self, code):
        if re.search(self.code.code_regex, code) == None or len(code) < 4:
            PopupError("Código Invalido!")

        else:
            ...

class ResetPasswordValidation:
    def __init__(self):
        self.password = Regex()

    def reset_password_validation(self, password_01, password_02):
        if re.search(self.password.password_regex, password_01) == None or re.search(self.password.password_regex, password_02) == None or password_01 != password_02:
            PopupError("Senha Invalida!")            
        else:
            return True
        


    
