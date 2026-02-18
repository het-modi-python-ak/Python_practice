import os
import smtplib
import ssl # Import the ssl module
from dotenv import load_dotenv, dotenv_values
from email.message import EmailMessage

load_dotenv()

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASS = os.environ.get('EMAIL_PASS')
print(EMAIL_ADDRESS, " and ", EMAIL_PASS)

msg = EmailMessage()
msg['Subject'] = 'hello'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'het.modi@armakuni.com'
msg.set_content('this file contains pdf ?')


context = ssl.create_default_context()

files = ['email_python/sample.pdf']

for  file in files:
    with open(file,'rb') as f:
        file_data = f.read()
        file_name = f.name

        msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)


with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
    smtp.send_message(msg)
    print("Email sent successfully!")
