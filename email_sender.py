import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# Reading HTML from a file and preparing a template
html = Template(Path('index.html').read_text())

# Creating a new email message
email = EmailMessage()

# Setting the sender, receiver, and subject of the email
email['from'] = 'Cody Johnson'
email['to'] = 'codyjohnsontx@gmail.com'
email['subject'] = 'Hi, how are you?'

# Setting the HTML content of the email, replacing a placeholder in the template with a specific name
email.set_content(html.substitute(name='John Smith'), 'html')

# Sending the email using Gmail's SMTP server
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # Saying hello to the server
    smtp.ehlo()

    # Starting TLS encryption
    smtp.starttls()

    # Logging in to the SMTP server
    smtp.login('codyjohnsontx@gmail.com', 'qcqdbaundakyqstl')

    # Sending the email
    smtp.send_message(email)

    # Printing a success message
    print('all good boss')
