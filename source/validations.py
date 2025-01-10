# Importações 

from PySimpleGUI import PopupError
import re

# Classe para validação dos dados da aplicação 
class Regex:

    def __init__(self):
        self.name_regex = r"^[A-Za-záàâãéèêíïóôõöúçñ]+ [A-Za-záàâãéèêíïóôõöúçñ]+$"
        self.phone_regex = r'^\s*(?:\+?(\d{1,3}))?([-. (]*(\d{3})[-. )]*)?((\d{3})[-. ]*(\d{2,4})(?:[-.x ]*(\d+))?)\s*$'
        self.email_regex = r"^[\.A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+\.[a-z]{3}(\.[a-z]{2})?$"
        self.password_regex = r'^[0-9A-Za-záàâãéèêíïóôõöúçñ"@#$%¨&*()-+={}\[\]~^,.]{4,}$'
        self.code_regex = r"^[A-Z0-9]{4}$"

class LoginValidation:

    def __init__(self):
        self.regex = Regex()

    def login_validation(self, email, password):

        if re.search(self.regex.email_regex, email) == None or re.search(self.regex.password_regex, password) == None:
            PopupError("Dados Invalidos!")
        
        else:
            return True

class RegisterValidation:

    def __init__(self):
        self.regex = Regex()        

    def register_validation(self, name, phone, email, password):

        if re.search(self.regex.name_regex, name) == None or re.search(self.regex.phone_regex, phone) == None or re.search(self.regex.email_regex, email) == None or re.search(self.regex.password_regex, password) == None:
            PopupError("Dados Invalidos!")

        else:
            return True

class EmailRecoveryPasswordValidation:

    def __init__(self):
        self.email = Regex()

    def email_recovery_password_validation(self, email):
        if re.search(self.email.email_regex, email) == None:
            PopupError("Email Invalido!")
        else:
            return True

class CodeValidation:

    def __init__(self):
        self.code = Regex()

    def code_validation(self, code):

        if re.search(self.code.code_regex, code) == None:
            PopupError("Código Invalido!")

        else:
            return True

class ResetPasswordValidation:

    def __init__(self):
        self.password = Regex()

    def reset_password_validation(self, password_01, password_02):
        if re.search(self.password.password_regex, password_01) == None or re.search(self.password.password_regex, password_02) == None or password_01 != password_02:
            PopupError("Senha Invalida!")            

        else:
            return True


        
        


    
