import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Cody Johnson'
email['to'] = 'codyjohnsontx@gmail.com'
email['subject'] = 'Hi, how are you?'

email.set_content('I\'m a python developer')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('codyjohnsontx@gmail.com', 'qcqdbaundakyqstl')
	smtp.send_message(email)	
	print('all good boss')