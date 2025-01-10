
# Adicionado a pasta principal ao path do python
from pathlib import Path
import sys
path_source = Path()
sys.path.append(f"{path_source.absolute()}")

# Importações
import unittest
from source.validations import (LoginValidation,
                                RegisterValidation,
                                EmailRecoveryPasswordValidation,
                                CodeValidation,
                                ResetPasswordValidation)
                                
class TestValidationsMethods(unittest.TestCase):

    def test_login(self):    
        login_validation_test = LoginValidation()  
        self.assertEqual(login_validation_test.login_validation("teste@email_teste.com.br","134656"), True)


    def test_register(self):
        register_validation_test = RegisterValidation()

        self.assertAlmostEqual(register_validation_test.register_validation(
            "Nome Sobrenome",
            "99984656521", # Telefone Fictício
            "email@teste.com.br",
            "1326465"
        ), True)

    def test_email_recovery_password(self):
        email_recovery_password_test = EmailRecoveryPasswordValidation()
        self.assertAlmostEqual(email_recovery_password_test.email_recovery_password_validation("email@test.com.br"), True)

    def test_code(self):
        code_test = CodeValidation()
        self.assertAlmostEqual(code_test.code_validation("A5F9"), True)

    def test_password_reset(self):
        password_reset_test = ResetPasswordValidation()
        self.assertAlmostEqual(password_reset_test.reset_password_validation("12345","12345"), True)

if __name__ == "__main__":
    unittest.main()
        

