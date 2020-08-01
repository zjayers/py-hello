# Multipurpose Internet Mail Extensions
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text())
body = template.substitute({"name": "John"})
body = template.substitute(name="John")
dict = {"name": "John"}
body = template.substitute(dict)

message = MIMEMultipart()
message["from"] = "Zach Ayers"
message["to"] = "testuser@gmail.com"
message["subject"] = "This is a test!"

message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path('test.png').read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo() # Start the smtp with hello
    smtp.starttls()
    smtp.login('testuser@gmail.com', 'password')
    smtp.send_message(message)
    print("Sent...")