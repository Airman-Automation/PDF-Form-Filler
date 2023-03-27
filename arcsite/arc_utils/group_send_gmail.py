import smtplib
from email.message import EmailMessage


def sendGmail(EmailList, filepath="pdfs/envision_response.pdf"):
    print(EmailList)
    Sender_Email = "testdevelopment273689525@outlook.com"
    Password = ""

    for email in EmailList:
        Reciever_Email = email

        newMessage = EmailMessage()
        newMessage['Subject'] = "Check out PDF"
        newMessage['From'] = Sender_Email
        newMessage['To'] = Reciever_Email
        newMessage.set_content('test')

        files = [filepath]

        for file in files:
            with open(file, 'rb') as f:
                # print("check1")
                file_data = f.read()
                file_name = f.name
            newMessage.add_attachment(
                file_data, maintype='application', subtype='octet-stream', filename=file_name)

        # print("check2")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

            smtp.login(Sender_Email, Password)
            smtp.send_message(newMessage)

    print("Sent Email")
