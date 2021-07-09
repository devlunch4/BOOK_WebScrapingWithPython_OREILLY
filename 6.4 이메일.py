import smtplib
from email.mime.text import MIMEText

msg = MIMEText('The body of the email is here')

msg['Subject'] = 'An Email Alert'
msg['From'] = 'ryan@python.com'
msg['To'] = 'webmaster@python.com'

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()

