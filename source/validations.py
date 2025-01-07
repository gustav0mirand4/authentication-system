# Importações 

from PySimpleGUI import PopupError
import re

# Classe para validação dos dados da aplicação 
class LoginValidation:

    def __init__(self):
        
        # Expressão regular para validar campos 
        self.email_regex = r"^[\.A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+\.[a-z]{3}(\.[a-z]{2})?$"
        self.password_regex = r'^[0-9A-Za-záàâãéèêíïóôõöúçñ"@#$%¨&*()-+={}\[\]~^,.]{4,}$'

    def login_validation(self, email, password):

        if re.search(self.email_regex, email) == None or re.search(self.password_regex, password) == None:
            PopupError("Dados Invalidos!")
        
        else:
            True

        


    
