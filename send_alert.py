import smtplib
import string

email_from = ''
email_subject = 'Salt Level Alert!'

receivers = ['']

text = 'Salt Level is critical!'
body = string.join((
    'From: %s' % email_from,
    'Subject: %s' % email_subject,
    '',
    text,
    ), '\r\n')

try:
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login( 'USERNAME', 'APP_PASSWORD' )
    server.sendmail( email_from, receivers, body )
    server.quit()
except:
    print "Error: unable to send email"

