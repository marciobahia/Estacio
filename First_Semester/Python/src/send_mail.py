# import dos pacotes necessários
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Criação de um objeto de mensagem
msg = MIMEMultipart()
texto = "Estou enviando um email com python"

# parâmetros
senha = "SUA SENHA"
msg['to'] = "SEU E-MAIL"
msg['Subject'] = "ASSUNTO"

# Criação do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

# Criação do Servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

# Login na conta para envio
server.login(msg['From'], senha)

# Envio da mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string())

# Encerramento do Servidor
server.quit()

print('Mensagem enviada com sucesso')
