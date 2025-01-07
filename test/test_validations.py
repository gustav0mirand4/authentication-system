
# Adicionado a pasta principal ao path do python
from pathlib import Path
import sys
path_source = Path()
sys.path.append(f"{path_source.absolute()}")

# Importações
import unittest
from source.validations import LoginValidation


class TestValidationsMethods(unittest.TestCase):

    def test_validations_inputs(self):    
        user_test = LoginValidation()

        self.assertEqual(user_test.login_validation("test@test.com.br","1234"), None)

if __name__ == "__main__":
    unittest.main()
        

