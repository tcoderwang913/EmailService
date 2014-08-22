import os
import smtplib

from email.mime.text import MIMEText

from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders

class sendEmail_Mailgun():
    def send(self,subject, dest,message, fileList):
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
        
        s = smtplib.SMTP('smtp.mailgun.org', 587)

        #to use, change this to your own login credentials
        s.login('credential example', '2ccf6863bba6d62bbcaa28a0249ca743')
        s.sendmail(self.msg['From'], self.msg['To'], self.msg.as_string())
        s.quit()


