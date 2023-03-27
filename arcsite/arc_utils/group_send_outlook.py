import smtplib
import email.mime.multipart
import email.mime.text
import email.mime.base
import os
from smtplib import SMTPException


def sendOutlook(email_addr, filepath="pdfs/envision_response.pdf"):

    sender = "automated-arc-sender@outlook.com"
    # "testdevelopment273689525@outlook.com"
    password = ""

    receivers = [email_addr]

    file_name = filepath

    server_host = 'smtp.office365.com'
    server_port = 587

    main_msg = email.mime.multipart.MIMEMultipart()

    text_msg = email.mime.text.MIMEText("this is a email text content")

    main_msg.attach(text_msg)

    contype = 'application/octet-stream'
    maintype, subtype = contype.split('/', 1)

    print(file_name)

    data = open(file_name, 'rb')
    file_msg = email.mime.base.MIMEBase(maintype, subtype)
    file_msg.set_payload(data.read())
    data.close()

    email.encoders.encode_base64(file_msg)

    basename = os.path.basename(file_name)
    file_msg.add_header('Content-Disposition',
                        'attachment', filename=basename)

    main_msg.attach(file_msg)

    main_msg['From'] = sender
    main_msg['To'] = ", ".join(receivers)
    main_msg['Subject'] = "This attachment sent from outlook"
    main_msg['Date'] = email.utils.formatdate()

    fullText = main_msg.as_string()

    server = smtplib.SMTP(server_host, server_port)
    try:
        print(receivers)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender, password)

        server.sendmail(sender, receivers, fullText)
        print ("Successfully sent email")
    except SMTPException as e:
        print (f"Error: unable to send email: {e}")
    finally:
        server.quit()
