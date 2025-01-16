# Importações

import PySimpleGUI as sg
from validations import (LoginValidation,
                        RegisterValidation,
                        EmailRecoveryPasswordValidation,
                        CodeValidation,
                        ResetPasswordValidation)

# Classe para a criação de layouts
class Ui:
    def __init__(self):
        # Carregando o layout principal
        self.window = self.email_recovery_password_layout()

        # Validação de dados
        self.login = LoginValidation()
        self.register = RegisterValidation()
        self.email_recovery_password = EmailRecoveryPasswordValidation()
        self.code = CodeValidation()
        self.reset_password = ResetPasswordValidation()

    # Funções que criam os layouts e carregam com um tamanho especifico para cada um deles
    def login_layout(self):

        # Layout de login
        layout = [
            [sg.Push(),sg.Text("Login",font=("Roboto Bold",20)),sg.Push()],
            [sg.Push(),sg.Image(filename=r"..\authentication-system\img\login-avatar-test.png"),sg.Push()],
            [sg.HSep(pad=20)],
            [sg.Text("Faça login na sua conta",font=("Roboto Bold",13))],
            [sg.Text("Email"),sg.Push()],
            [sg.Input(key="-EMAIL-LOGIN-"),sg.Push()],
            [sg.Text("Senha"),sg.Push()],
            [sg.Input(password_char="*", key="-PASSWORD-LOGIN-"),sg.Push()],
            [sg.Sizer(15,15)],
            [sg.Push(),sg.Button("Entrar",key="-ENTRAR-"),sg.Button("Cadastrar",key="-CADASTRAR"),sg.Button("Recuperar Senha",key="-RECUPERAR-SENHA-"),sg.Push()]
        ]

        return sg.Window("Login",size=(350,500),layout=layout)

    def register_layout(self):

        # Layout de cadastro de usuário
        layout = [
            [sg.Text("Cadastre sua conta",font=("Roboto Bold",13))],
            [sg.HSep()],
            [sg.Radio("Masculino", group_id=1, default=True, key="-SEXO-"),
             sg.Radio("Feminino", group_id=1)],
            [sg.Text("Nome:"),sg.Push(),sg.Input(key="-NOME-")],
            [sg.Text("Telefone"),sg.Input(key="-TELEFONE-",size=80)],
            [sg.Text("Email:"),sg.Push(),sg.Input(key="-EMAIL-")],
            [sg.Text("Senha:"),sg.Input(key="-SENHA-"),sg.Push()],
            [sg.Sizer(18,18)],
            [sg.Push(),sg.Button("Enviar",key="-CADASTRAR-"),sg.Button("Entrar",key="-TELA-DE-LOGIN-"),sg.Push()]
        ]

        return sg.Window("Cadastro",size=(400,240),layout=layout)

    def email_recovery_password_layout(self):

        # Layout para que o usuário forneça o email para recuperar sua conta
        layout = [
            [sg.Text("Recuperar Conta",font=("Roboto Bold",18))],
            [sg.HSep(pad=14)],
            [sg.Text("Digite o email para recuperar sua senha",font=("Roboto Bold",12))],
            [sg.Text("Email:"),sg.Input(key="-EMAIL-DE-RECUPERAÇAO-DE-SENHA-")],
            [sg.Sizer(18,18)],
            [sg.Push(),sg.Button("Enviar",key="-ENVIAR-EMAIL-DE-RECUPERAÇAO-DE-SENHA-"),sg.Button("Entrar",key="-TELA-DE-LOGIN-"),sg.Push()]
        ]

        return sg.Window("Email de Recuperação",size=(350,250),layout=layout)

    def send_code_layout(self):

        # Layout para enviar o código recebido no email do usuário
        layout = [
            [sg.Text("Enviamos o código para o email <email-do-usuário>",pad=15)],
            [sg.Push(),sg.Text("Código:"),sg.Input(size=(20,20),key="-CODE-"),sg.Push()],
            [sg.Sizer(18,18)],
            [sg.Push(),sg.Button("Alterar Senha",button_color="red",key="-ALTERAR-SENHA-"),sg.Button("Entrar",key="-TELA-DE-LOGIN-"),sg.Push()]
        ]

        return sg.Window("Alterar Senha",size=(350,250),layout=layout)

    def reset_password_layout(self):

        # Layout para alterar a senha da conta do usuário
        layout = [
            [sg.Text("Digite sua nova senha",font=("Roboto Bold",13), pad=14)],
            [sg.Push(),sg.Text("Senha:"),sg.Push(),sg.Input(size=(29,29), key="-PASSWORD-01-")],
            [sg.Text("Confirmar Senha:"),sg.Input(key="-PASSWORD-02-")],
            [sg.Sizer(18,18)],
            [sg.Push(),sg.Button("Enviar",button_color="red", key="-ENVIAR-NOVA-SENHA-"),sg.Button("Entrar",key="-TELA-DE-LOGIN-"),sg.Push()]
        ]

        return sg.Window("Cadastro",size=(350,210),layout=layout)


    # Função principal para carregas as janelas da aplicação
    def main(self):
        while True:
            event, value = self.window.read()
            match event:
                case "-CADASTRAR":
                    self.window.close()
                    self.window = self.register_layout()

                case "-TELA-DE-LOGIN-":
                    self.window.close()
                    self.window = self.login_layout()

                case "-ENTRAR-":
                    self.login.login_validation(value["-EMAIL-LOGIN-"],value['-PASSWORD-LOGIN-'])

                case "-CADASTRAR-":
                    self.register.register_validation(value["-SEXO-"],
                                                        value["-NOME-"],
                                                        value["-TELEFONE-"],
                                                        value["-EMAIL-"],
                                                        value["-SENHA-"])
                        

                case "-ENVIAR-EMAIL-DE-RECUPERAÇAO-DE-SENHA-":
                    match self.email_recovery_password.email_recovery_password_validation(value["-EMAIL-DE-RECUPERAÇAO-DE-SENHA-"]):
                        case True:
                            self.window.close()
                            self.window = self.send_code_layout()

                case "-RECUPERAR-SENHA-":
                    self.window.close()
                    self.window = self.email_recovery_password_layout()

                case "-ENVIAR-NOVA-SENHA-":
                    self.reset_password.reset_password_validation(value["-PASSWORD-01-"],value["-PASSWORD-02-"])

                case "-ALTERAR-SENHA-":
                    self.code.code_validation(value['-CODE-'])

                case sg.WIN_CLOSED:
                    break

        self.window.close()

# Criando um exemplo de instancia da classe principal
if __name__ == "__main__":
    ui = Ui()
    ui.main()