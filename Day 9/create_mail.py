import smtplib # Simple Mail Transfer Protocol
from email.mime.multipart import MIMEMultipart # For sending email with attachments
from email.mime.text import MIMEText # For sending email with text



username = 'Your email'
password = 'Your email app password'

def myMail(body = 'Email Body', subject = 'Hello World', from_mail = 'Mahfuz Mia <{username}>', to_mails = None, html = None):
    assert isinstance(to_mails, list) # Check if to_mail is a list
    
    msg = MIMEMultipart('alternative') # Create a MIMEMultipart object
    msg['From'] = from_mail # Set the sender's email
    msg['To'] = ', '.join(to_mails) # Set the receiver's email
    msg['Subject'] = subject # Set the email subject
    text_part = MIMEText(body, 'plain') # Create a MIMEText object with plain text
    msg.attach(text_part) # Attach the plain text to the email

    if html != None:
        html_part = MIMEText(html, 'html') # Create a MIMEText object with html
        msg.attach(html_part) # Attach the html to the email

    msg = msg.as_string() # Convert the email to a string

    server = smtplib.SMTP(host='smtp.gmail.com', port=587) # Create an SMTP object
    server.ehlo() # Identify yourself to the server
    server.starttls() # Secure the connection
    server.login(username, password) # Login to your email
    server.sendmail(from_mail, to_mails, msg) # Send the email
    server.quit() # Close the connection
    