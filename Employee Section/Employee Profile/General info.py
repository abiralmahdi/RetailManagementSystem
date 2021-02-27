from tkinter import *
from tkinter import ttk
import pandas as pd
import csv
import sys
import datetime
import schedule
import tkinter.messagebox
from datetime import date

emp_data = pd.read_csv('EmployeeRecords.csv')
empl_id = emp_data['ID No'] == 101



root = Tk()

root.geometry('1000x550')
root.title('Retail Management System')
# root.minsize(460, 540)
# root.maxsize(460, 540)

frame1 = Frame(root, borderwidth='2', relief=RIDGE, bg='deepskyblue4')
identity = Label(frame1, text= 'Abir', fg='black', bg='deepskyblue4', pady='20',
             font=('Calibri', 15, 'bold'))
identity.grid(row=0, column=0)

post = Label(frame1, text= '101', fg='black', bg='deepskyblue4', pady='20',
             font=('Calibri', 15, 'bold'))
post.grid(row=0, column=0)

#title = Label(frame1, text='Retail Management System', fg='black', bg='deepskyblue4', pady='20',
#              font=('Copperplate Gothic Bold', 20, 'bold'))

#title.pack()
frame1.pack(fill=X)

frame2 = Frame(root, borderwidth='10', relief=RIDGE, bg='deepskyblue4')
frame2.pack(fill=BOTH, expand=1)




root.mainloop()