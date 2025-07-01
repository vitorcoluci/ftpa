## -*- coding: utf-8 -*-
# coding: utf8
import pandas as pd
import math
import numpy as np
import subprocess, os

import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

smtp_server = "smtp.unicamp.br"
smtp_port = 587
servidor = smtplib.SMTP(smtp_server, smtp_port)

email_usuario = "ftpa@unicamp.br"
senha = "Mcbfqtv25!"

servidor.starttls()
servidor.login(email_usuario, senha)

# carrega nomes
alunos = pd.read_csv("participantes-FTPA-2025.csv", encoding='utf-8') #encoding='latin-1')
num_alunos=alunos.shape[0]
print(num_alunos)
# gera certificado
for i in range(num_alunos):
    aluno = str(alunos.at[i,"Nome"])
    aluno_junto = "".join(aluno.split())
    # coleta primeira letra
    primeira_letra = aluno_junto[0].lower()
    ra = str(alunos.at[i,"RA"])
    texto=r"\documentclass[12pt,landscape]{{article}} \input{{sctruct.tex}} \begin{{document}} \pagestyle{{empty}} \para{{{0}}}{{{1}}} \end{{document}} ".format(aluno,ra)

    #print(texto)
    file = open("main.tex", "w") 
    file.write(texto)
    file.close()

    a = subprocess.run('pdflatex --enable-write18 --shell-escape main.tex > log.latex',shell=True)
    b = subprocess.run('mv main.pdf ' + str(aluno_junto) + '.pdf',shell=True)
    c = subprocess.run('rm main.* log.latex',shell=True)

    # Envia emails #
    attachments = [str(aluno_junto) + '.pdf']
    destinatario = primeira_letra + ra + '@dac.unicamp.br'
    
    assunto = "Certificado de participação da FT de Portas Abertas"

    corpo = """Prezado(a)  {}.
                
                Obrigado pela sua participação no FT de Portas Abertas.
                
                Segue em anexo o certificado de participação.

                Comissão organizadora.

                """.format(aluno)

  
    msg = MIMEMultipart()
    msg["From"] = email_usuario
    msg["To"] = destinatario
    msg["Subject"] = assunto
    msg.attach(MIMEText(corpo, "plain"))

    for filename in attachments:
            f = filename
            part = MIMEBase('application', "octet-stream")
            part.set_payload( open(f,"rb").read() )
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
            msg.attach(part)

    #servidor.sendmail(email_usuario, destinatario, msg.as_string())

    print(i,aluno,destinatario)
    print(corpo)
    print("E-mail enviado com sucesso para ",aluno," !")

servidor.quit()

# junta todos os certificados num unico arquivo para impressao
b = subprocess.run('qpdf --empty --pages ./*.pdf -- ./certificados-FTPA.pdf',shell=True)	