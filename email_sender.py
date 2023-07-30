import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Cody Johnson'
email['to'] = 'codyjohnsontx@gmail.com'
email['subject'] = 'Hi, how are you?'

# Set the email body content using the template and substitute method
email.set_content(html.substitute(name='John Smith'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('codyjohnsontx@gmail.com', 'qcqdbaundakyqstl')
    smtp.send_message(email)
    print('all good boss')
