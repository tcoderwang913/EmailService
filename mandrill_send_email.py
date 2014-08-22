import os
import smtplib

from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders


class sendEmail_Mandrill():
    def send(self,subject, dest,message,fileList):
        self.msg = MIMEMultipart()
        self.msg['Subject'] = subject;
        self.msg['From'] = "example@gmail.com"
        self.msg['To'] = dest

        self.textMessagePart = MIMEText(message)
        self.msg.attach(self.textMessagePart)
        
        for inputFileName in fileList:
            self.attachmentPart = MIMEBase('application', "octet-stream")
            self.attachmentPart.set_payload(open(inputFileName, "rb").read())
            Encoders.encode_base64(self.attachmentPart)
            self.attachmentPart.add_header('Content-Disposition', 'attachment', filename =inputFileName)
            self.msg.attach(self.attachmentPart)
        
        s = smtplib.SMTP('smtp.mandrillapp.com', 587)

        #to use, change this to your own login credentials
        s.login('example@gmail.com', 'S_2Upi9mZEd6yOdAYk9WwA')
        s.sendmail(self.msg['From'], self.msg['To'], self.msg.as_string())
        s.quit()


