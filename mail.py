import serial
import csv
import datetime
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_email():
    gmail_user = 'galuafre@gmail.com'  
    gmail_password = 'random97key'
    subject = "Dados do dia - Coleta solar"

    sent_from = gmail_user  
    to = ['hugonvsc@gmail.com', 'gabrieluis10@outlook.com', 'victormacedo10@yahoo.com.br']

    msg = MIMEMultipart()
    msg['Subject'] = subject 
    msg['From'] = gmail_user
    msg['To'] = "hugonvsc@gmail.com"

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("solar_data.csv", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="solar_data.csv"')
    msg.attach(part)

    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to, msg.as_string())
        server.close()

    except:  
        print ('Something went wrong...')

email_sent = False
send_mail_date = datetime.datetime(2016, 1, 1, 19, 0)
morning_date = datetime.datetime(2016, 1, 1, 6, 0)

while(True):
    date = datetime.datetime.now()
    if date.time().hour == send_mail_date.time().hour and email_sent is not True:
        email_sent = True

    elif date.time().hour == morning.time().minute and email_sent is True:
        email_sent = False