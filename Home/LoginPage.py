from tkinter import *
from tkinter import ttk
import pandas as pd
import csv, sys
import tkinter.messagebox


accounts_admin = {
    'admin1': 'pass123',
    'admin2': 'pass123'
}

accounts_employee = {
    'abir': 'pass123',
    'abrar': 'pass456',
    'kamal': 'pass789'
}

def login():
    
    if loginval.get() == 'Admin':
        if uservar.get() in accounts_admin:
            if passvar.get() == accounts_admin[uservar.get()]:
                tkinter.messagebox.showinfo('Success', 'Login Successful!')

            else:
                tkinter.messagebox.showerror('Login error', 'Incorrect Password!')

        elif uservar.get() not in accounts_admin:
            tkinter.messagebox.showerror('Login error', 'No such account found!')

    elif loginval.get() == 'Employee':
        if uservar.get() in accounts_employee:
            if passvar.get() == accounts_employee[uservar.get()]:
                tkinter.messagebox.showinfo('Success', 'Login Successful!')

            else:
                tkinter.messagebox.showerror('Login error', 'Incorrect Password!')

        elif uservar.get() not in accounts_employee:
            tkinter.messagebox.showerror('Login error', 'No such account found!')
     
    elif loginval.get() == '':
        tkinter.messagebox.showerror('Login error', 'Please confirm whom you are logging in as.')

    if uservar.get() == '':
        tkinter.messagebox.showerror('Login error', 'Please fill up the full form.')
    
    elif uservar.get() == '':
        tkinter.messagebox.showerror('Login error', 'Please fill up the full form.')
    
    else:
        pass


root = Tk()

root.geometry('500x600')
root.title('Retail Management System')
root.minsize(460, 540)
root.maxsize(460, 540)

frame1 = Frame(root, borderwidth='10', relief=RIDGE, bg='deepskyblue4')
title = Label(frame1, text='Retail Management System', fg='white', bg='deepskyblue4', pady='20',
              font=('Copperplate Gothic Bold', 18, 'bold'))
title.pack()
frame1.pack(fill=X)

frame3= Frame(root, borderwidth='10', relief=RIDGE, bg='deepskyblue4')

intro_label = Label(frame3, text='Enter account credentials to log in to the system ', font=('calibri', 15, 'bold', 'underline'), bg='deepskyblue4', fg='white') 


form_text = Label(frame3, text='Login Page', fg='white', bg='deepskyblue4',
                  pady='0', padx='5', font=('Copperplate Gothic Bold', 15, 'bold'))


uservar, passvar, loginval = StringVar(), StringVar(), StringVar()


form_text.pack(padx=10, pady=10)
intro_label.pack()

frame2 =  Frame(frame3, bg='deepskyblue4')

login_type = Label(frame3, text='Login As:', font=('calibri', 15, 'bold'), bg='deepskyblue4', fg='white')

login_type_entry = ttk.Combobox(frame3, values=
[
    'Admin',
    'Employee'
],
                         textvariable=loginval
                         )

#login_type_entry.grid(row=0, column=1, pady=20)
#login_type.grid(row=0, column=0, pady=20)

login_type.pack(pady=10)
login_type_entry.pack()



user = Label(frame2, text='Username', font=('calibri', 15, 'bold'), bg='deepskyblue4', fg='white')
user.grid(row=1, column=0, pady=10)

userentry = Entry(frame2, textvariable=uservar)
userentry.grid(row=1, column=1)


passw = Label(frame2, text='Password', font=('calibri', 15, 'bold'), bg='deepskyblue4', fg='white')
passw.grid(row=2, column=0)
passentry = Entry(frame2, textvariable=passvar)
passentry.grid(row=2, column=1)

login_button = Button(frame2, text='Login', font=('calibri', 11), width=7, command=login)
login_button.grid(row=3, column=1, pady=20)

forgot_button = Button(frame2, text='Forgot Password', font=('calibri', 11))
forgot_button.grid(row=4, column=1, pady=0)


frame2.pack(fill=BOTH, expand=1, padx=60, pady=20)
frame3.pack(fill=BOTH, expand=1)


root.mainloop()
