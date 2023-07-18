from email.message import EmailMessage
import ssl
import smtplib
import time
def send_mail():
    sender_email = 'rambudavincent0@gmail.com'
    email_password = '' #enter gmail security key 
    owner_email = 'onrambu022@student.wethinkcode.co.za'
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    subject = "MOVEMENT DETECTED!!!!!!"
    body = f'''There is unusual movement at your residence at {current_time}'''
    mailsen = EmailMessage()
    mailsen['From'] = sender_email
    mailsen['To'] = owner_email
    mailsen['Subject'] = subject
    mailsen.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(sender_email,email_password)
        smtp.sendmail(sender_email, owner_email,mailsen.as_string())
    print('email sent to owner')