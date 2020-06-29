import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)
import base64

def sender(frame):
    message = Mail(
        from_email='pointersd3@gmail.com',
        to_emails='mohit.mk1541@gmail.com',
        subject='PFA the detections made',
        html_content='Person without msk detected!')

    with open('defaulter.png', 'rb') as f:#sending attachment
        data = f.read()
        f.close()
    encoded_file = base64.b64encode(data).decode()

    attachedFile = Attachment(
        FileContent(encoded_file),
        FileName('defaulter.png'),
        FileType('image/png'),
        Disposition('attachment')
    )
    message.attachment = attachedFile
    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)