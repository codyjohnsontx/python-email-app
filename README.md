# python-email-app

<h1>Python Email Sender</h1>
This Python script sends an HTML formatted email using the SMTP protocol.

<h2>How It Works</h2>
This script reads an HTML file (index.html), substitutes a placeholder in the HTML with a specific name, and sends the resulting HTML content as the body of an email. The email is sent using the SMTP server of Gmail.

<h2>Requirements</h2>
Python 3
The smtplib and email.message standard libraries

<h2>How to Run</h2>
You can run this program directly without passing any arguments. 
Make sure to have your index.html in the same directory as your script.

Copy code
python3 script.py
Note: The email's sender, receiver, subject, SMTP host, and SMTP port are hard-coded into the script, as is the email password. Remember to keep your passwords secret and secure. Do not share the script with your password in it.



