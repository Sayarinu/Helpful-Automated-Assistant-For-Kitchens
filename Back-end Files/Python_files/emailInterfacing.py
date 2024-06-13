import smtplib
import ics
import os
import setup as s
import datetime
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

smtp_server = 'smtp-mail.outlook.com'
smtp_port = 587

body = """
Dear recipient,

Thank you so much for being a part of the launch of HAAK! We are so excited to have you on board and we hope you enjoy your experience with us. We are a small team of students who are passionate about food and we hope that our service will help you find the best restaurants in your area.

In celebration of our launch we are giving you recommendations for if you are ever in the area where our team is located in Downtown Brooklyn, New York. We hope you enjoy!

1. KUUN
2. The Alcove
3. The Long Island Bar
4. The River Cafe
5. The Osprey

Consider checking these out if you are ever in the area and we are extremely happy to have you on board!

Best regards,
HAAK Team
"""

with open("../text_files/email_login.txt", "r") as file:
    login = list(file.readline().split(" "))
    sender_email, sender_password = login[0], login[1]
    del login
file.close()

def convert_time(time: str =None) -> int:
    date_format = "%Y-%m-%d %H:%M"
    datetime_obj = datetime.datetime.strptime(time, date_format)
    utc_timestamp = int(datetime_obj.timestamp())
    return utc_timestamp

def generate_reservation(nameOfRestaurant: str =None, invitedName: str =None
                  , invitedEmail: str =None, location: str =None, utctimestamp: int =None):
    b = base64.b64encode((bytes(nameOfRestaurant + invitedName 
                                + invitedEmail + location + str(utctimestamp), 'utf-8')))
    
    event = ics.Event(
        name = nameOfRestaurant + " Reservation",
        begin = datetime.datetime.fromtimestamp(utctimestamp),
        duration = datetime.timedelta(minutes = 15),
        organizer = ics.Organizer("HAAK.Services@outlook.com" + nameOfRestaurant),
        attendees = [ics.Attendee(invitedEmail, invitedName)],
        location = location,
        uid = str(b).replace("b'", "").replace("'", "")
    )

    cal = ics.Calendar()
    cal.events.add(event)

    with open('event.ics', 'w') as f:
        f.writelines(cal.serialize_iter())
    f.close()

    return cal.serialize()

def send_calendar_email(subject: str =None, message: str =None, receiver_email: str =None, attachment_name: str =None):
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    if subject == None:
        subject = 'Your Dinner Reservation'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    if attachment_name is not None:
        filename = attachment_name
        attachment = open(filename, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)
        attachment.close()
        os.remove(attachment_name)


    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)

    server.quit()

def sendPromotionalEmail(receiver_email: str =None, subject: str=None, body: str =None):
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)

    server.quit()

#
#def main():
#    print(send_calendar_email("Testing", "This is a test email", "john@example.com", "event.ics"));

#if __name__ == "__main__":
#   main()
