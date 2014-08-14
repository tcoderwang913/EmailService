
Email Service (Back-End)
=============
This simple email service tries to provide a simple GUI for users to send emails with two underlying 
Email service providers: Mailgun and Mandrill. It is coded in python. 


Major components and functionalities
====================================
It comprises two major components:
1. A GUI that users use to input relevant email information such as:
    1.a) To: the recipient email address
    1.b) Subject: subject of the email
    1.c) Attach: the name of the file you would like to attach as attachment
    1.d) A textbox that users input text messages
    1.e) After all the above necessary information are filled, simply click the "Send" button, it will send the email to
         the recipient specified in the "To" field
2. The backend that handles the email sending service. It relies on the two email service providers and the Python Email and SMTP library.
In other words, all emails are sent by SMTP. The reason for choosing SMTP is because Python has a solid library that supports this protocol
and it is simple to use. The user of the service is hidden from which service provider is being used underlyingly. When one of the Email 
service provider is failed, this Email service will use the other Email service provider in automatic way

For attachments, you can add more than one files by putting file names in the text area separated by white-space


Requirement to use
==================
In order to send the emails with Mailgun or Mandrill, you need to first create accounts with these two Email service providers.
You can then update the login information in mailgun_send_email.py and mandrill_send_email.py.

Usage
=====
You can download or fork the branch to your local machine, then go the EmailService directory, type:
       
       python email_app.py 

in the terminal. 

After providing "To","Subject" and "Attachments" as well as text message body, you can click the send button to send the emails.


Limitations
===========
Currently, in order to add attachments, you need to give the name of the file to attach and you need to put the file 
under the same directory as email_app.py. You can specify more than one files.
In the future, it would be nice to add code to explore the file system to add the files
and to make the backend more flexible to deal with different types of files


Contact
========
Song Wang: songwanguvm07@gmail.com
Stackoverflow profile: http://stackoverflow.com/users/1760345/taocp
Linkedin profile:https://www.linkedin.com/in/swtcoder
