from email.mime.multipart import MIMEMultipart
import smtplib
from email.utils import formataddr
from email.header import Header
from string import Template
from pathlib import Path
from email.mime.text import MIMEText
from config.config import email_password

def send_email_to_registered_users(message_to,username,password):
    template = Template(
        Path("rst\\templates\\rst\\email.html").read_text())
    message = MIMEMultipart()
    message["from"] = formataddr(
        (str(Header('Result Checker', 'utf-8')), 'peterkingdbx@gmail.com'))
    message["to"] = message_to
    message["subject"] = "Result checker registration for your ward"
    body = template.substitute(
        {"username": username, "password": password})
    message.attach(MIMEText(body, "html"))

    print("about to open SMTP server")
    
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        print("just opned smtp server")
        smtp.ehlo()
        smtp.starttls()
        print("About to login")
        smtp.login("peterkingdbx@gmail.com", email_password)
        print("logged in")
        smtp.send_message(message)
        print("message sent")

def send_email_for_newly_published_result(message_to,student_name,course,grade):
    template = Template(
        Path("rst\\templates\\rst\\new_result.html").read_text())
    message = MIMEMultipart()
    message["from"] = formataddr(
        (str(Header('New Published result', 'utf-8')), 'peterkingdbx@gmail.com'))
    message["to"] = message_to
    message["subject"] = "New results have been uploaded for your ward"
    body = template.substitute(
        {"student_name": student_name, "course": course, "grade":grade})
    message.attach(MIMEText(body, "html"))

    print("about to open SMTP server")
    
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        print("just opned smtp server")
        smtp.ehlo()
        smtp.starttls()
        print("About to login")
        smtp.login("peterkingdbx@gmail.com", email_password)
        print("logged in")
        smtp.send_message(message)
        print("message sent")