# Importações 

import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Gerador de código com 4 dígitos   
class CodeGenerator:
    def __init__(self):
        self.char_list = "ABCDEFGHIJKLMNOPQRSUVXWYZ0123456789"

    def code_generator(self):
        chars = random.choices(self.char_list, k=4)
        new_chars = "".join(chars)
        return new_chars
    
# SMTP Server
class SendEmail(CodeGenerator):
    def __init__(self, host, port):
        
        # Construindo o email tipo MIME
        self.server = smtplib.SMTP(host, port) # Configure o host a porta do seu servidor de email
        self.email_menssage = MIMEMultipart()


    def send_email(self, email_sender, email_recipient, password):

        # Código gerado 
        self.body = f"{CodeGenerator().code_generator()}"

        # Altere os campos para configurar o email 
        self.email_menssage["From"] = email_sender # Email remetente 
        self.email_menssage["To"] = email_recipient # Email destinatário 
        self.email_menssage["Subject"] = "Titulo do email"
        self.email_menssage.attach(MIMEText(self.body, "plain"))

        try:
            #Startando o servidor SMTP
            self.server.starttls()
            self.server.login(email_sender, password)


            #Enviar o email tipo MIME no servidor SMTP
            self.server.sendmail(self.email_menssage["From"], 
                                self.email_menssage["To"], 
                                self.email_menssage.as_string())        
       
        except Exception as error:
            print(f"Error {error}")
       
        else:
            print("Email enviado com sucesso!")
            self.server.quit()
