from Tkinter import *
from mailgun_send_email import *
from mandrill_send_email import *


class Email_Sender_GUI(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.createToLabel(master)
        self.createSubjectLabel(master)
        self.createMessageArea(master)
        self.createSendButton(master)
        self.createAttachButton(master)

        self.to=' '
        self.subject =' '
        self.msg =' '
        self.fileList = ' '
        self.senderMandrill = sendEmail_Mandrill()
        self.senderMailgun = sendEmail_Mailgun()

    def createToLabel(self,master):
        self.toLabel= Label(self.master, text="To")
        self.toLabel.grid(row=0,column=0)
        self.toEntryText = StringVar()
        self.toEntry = Entry(self.master, width=30, textvariable =self.toEntryText)
        self.toEntry.grid(row=0, column=1)
        self.toEntry.focus_set()
        self.toEntry.bind('<Leave>',self.getToEntryText)

    def createSubjectLabel(self,master):
        self.subjectLabel = Label(self.master, text="Subject")
        self.subjectLabel.grid(row=1, column=0)
        self.subjectEntryText = StringVar()
        self.subjectEntry = Entry(self.master, width =30,textvariable= self.subjectEntryText)
        self.subjectEntry.grid(row=1,column=1)
        self.subjectEntry.focus_set()
        self.subjectEntry.bind('<Leave>', self.getSubjectEntryText)

    def createAttachButton(self, master):
        self.attachmentButton = Label(self.master, text="Attach")
        self.attachmentButton.grid(row=2,column=0)
        self.filenames = StringVar()
        self.attachEntry = Entry(self.master, width =30, textvariable = self.filenames)
        self.attachEntry.grid(row=2, column=1)
        self.attachEntry.focus_set()
        self.attachEntry.bind('<Leave>', self.getFullPathFile)



    def createMessageArea(self, master):
        
        self.text = Text(self.master, height=30, width=50,font=("Helvetica",12),relief = SOLID)
        self.sbar = Scrollbar(self.master) 
        self.sbar.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.sbar.set)
        self.text.grid(row=3,column=0, columnspan=2)
        self.text.delete('1.0', END)                 
        self.text.insert('1.0', 'please start typing your message here,after finishing, press ESCAPE key')                
        self.text.mark_set(INSERT, '1.0')            
        self.text.focus_set()
        self.text.bind('<Escape>', self.gettext)

    def createSendButton(self,master):
    	self.sendButton = Button(self.master, text="Send", command=self.sendEmail)
    	self.sendButton.grid(row=10,column=0, padx =40)


    def gettext(self,event):                               
        self.msg = self.text.get('1.0', END +'-1c')

    def getToEntryText(self,event):
        self.to = self.toEntry.get()

    def getSubjectEntryText(self, event):
        self.subject = self.subjectEntryText.get()

    def getFullPathFile(self, event):
        self.text = self.attachEntry.get()
        self.fileList = self.text.split()

    def sendEmail(self):
        try:
            self.senderMandrill.send(self.subject, self.to, self.msg, self.fileList)
        except:
            self.senderMailgun.send(self.subject, self.to, self.msg, self.fileList)



root = Tk()
root.geometry("500x550")
root.title("Email Sending Service")
app = Email_Sender_GUI(root)
app.mainloop()

