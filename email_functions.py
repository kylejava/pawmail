import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from functions import *
def sendMail(sender_name , recipient_email, image_url):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("pawmailexpress@gmail.com", "E7t<NEt]`jjn$KcQ")

    message = MIMEMultipart("alternative")
    message["Subject"] = (sender_name + " Has Sent You A Paw-Mail!")
    message["From"] = "pawmailexpress@gmail.com"
    message["To"] =  recipient_email
    # Create the plain-text and HTML version of your message

    html = """\
    <html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    </head>
      <body>
        <h2>
            Have A Pawsome Day!!!
        </h2>
        <img src='%s' class = 'img-thumbnail' style = 'max-width:150px; height:auto;'>
        <h2>Send your friends a random dog photo <a href = "google.com">here!</a></h2>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(html % (image_url), "html")

    # Define the image's ID as referenced above

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first

    message.attach(part1)
    server.sendmail(
      "pawmailexpress@gmail.com",
      recipient_email,
      message.as_string())

    server.quit()
