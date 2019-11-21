from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from tkinter import *
import tkinter.messagebox as messagebox
import smtplib

#图形窗口
class Useritfc(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        #发送者邮箱
        self.emailLable = Label(self, text='Email:')
        self.emailLable.pack()
        self.emailInput = Entry(self)
        self.emailInput.pack()
        #邮箱密码
        self.passwordLable = Label(self, text='Password:')
        self.passwordLable.pack()
        self.passwordInput = Entry(self, show='*')
        self.passwordInput.pack()
        #接受者邮箱
        self.recieverLable = Label(self, text='reciever:')
        self.recieverLable.pack()
        self.recieverInput = Entry(self)
        self.recieverInput.pack()
        #发送smtp
        self.smtpLable = Label(self, text='SMTP:')
        self.smtpLable.pack()
        self.smtpInput = Entry(self)
        self.smtpInput.pack()
        #发送内容
        self.sendtextLable = Label(self, text='text:')
        self.sendtextLable.pack()
        self.sendtextInput = Entry(self)
        self.sendtextInput.pack()
        #确认按钮
        self.submitButton = Button(self, text='Submit', command=self.submit)
        self.submitButton.pack()

    def submit(self):
        s_email = self.emailInput.get()
        s_password = self.passwordInput.get()
        s_reciever = self.recieverInput.get()
        s_smtp = self.smtpInput.get()
        s_sendtext = self.sendtextInput.get()
        if s_email and s_password and s_reciever and s_smtp and s_sendtext:
            startsend(s_smtp, s_email, s_password, s_reciever, s_sendtext)
            messagebox.showinfo('Message', 'OK!')
            self.sendtextInput.delete(0, END)
        else:
            #填表出错弹窗
            messagebox.showinfo('Message', 'Please input all item correctly!')



def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def startsend(smtp, email, pswd, reciever, sendtext):
    msg = MIMEText(sendtext, 'html', 'utf-8')
    msg['From'] = _format_addr('JimmyPy <%s>' % email)
    msg['To'] = _format_addr('Admin <%s>' % reciever)
    msg['Subject'] = Header('Sup Bro!', 'utf-8').encode()

    server = smtplib.SMTP(smtp, 25) # SMTP协议默认端口是25
    server.starttls()
    server.set_debuglevel(1)
    server.login(email, pswd)
    server.sendmail(email, [reciever], msg.as_string())
    server.quit()


#启动窗口程序
app = Useritfc()
app.master.title('SMTP email sender')
app.mainloop()