from tkinter import *
from tkinter import ttk
import pandas as pd
import csv, sys, os, shutil
import tkinter.messagebox



def load():
    try:
        selected_item = database.focus()  ## get selected item
        print(selected_item)
        # print(selected_item[])
        idval.set(database.item(selected_item)['values'][0])
        nameval.set(database.item(selected_item)['values'][1])
        fnameval.set(database.item(selected_item)['values'][2])
        mnameval.set(database.item(selected_item)['values'][3])
        contactval.set(database.item(selected_item)['values'][4])
        emailval.set(database.item(selected_item)['values'][5])
        professionval.set(database.item(selected_item)['values'][6])
        desigval.set(database.item(selected_item)['values'][7])
        payval.set(database.item(selected_item)['values'][8])


    except IndexError:
        tkinter.messagebox.showinfo('Error', 'Please select one record')




def submit_value():

    if idval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')


    elif idval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')

    elif nameval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')
    elif fnameval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')

    elif mnameval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')
    elif contactval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')
    elif emailval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')

    elif professionval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')

    elif desigval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')

    elif payval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form ')



    else:
        try:
            with open('MemberRecords.csv', 'a+') as records:
                writer = csv.writer(records)
                writer.writerow(
                    [idval.get(), nameval.get(), fnameval.get(), mnameval.get(), contactval.get(), emailval.get(),
                     professionval.get(), desigval.get(), payval.get()])
                records.close()

            with open('MemberRecords.csv') as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    id = row['ID No']
                    namevalcsv = row['Name']
                    fnamevalcsv = row['Fathers Name']
                    mnamealcsv = row['Mothers Name']
                    contactvalcsv = row['Contact']
                    emailvalcsv = row['Email']
                    professionvalcsv = row['profession']
                    desigvalcsv = row['Designation']
                    payvalcsv = row['Pay']

            database.insert("", END, values=(id, namevalcsv, fnamevalcsv, mnamealcsv, contactvalcsv,
                                             emailvalcsv, professionvalcsv, desigvalcsv, payvalcsv))

            os.mkdir('Member Profile\\' + idval.get() + nameval.get())


            os.mkdir('Member Profile\\' + idval.get() + nameval.get()+'\Leaves')
            with open('Member Profile\\' + idval.get() + nameval.get()+'\Leaves\LeaveRecords.csv', 'a+') as leave_records:
                writer = csv.writer(leave_records)
                writer.writerow(['No.', 'From', 'To', 'Reference', 'Cause'])
                leave_records.close()


            os.mkdir('Member Profile\\' + idval.get() + nameval.get()+'\Complaints')
            with open('Member Profile\\' + idval.get() +  nameval.get()+'\Complaints\Complaints.csv', 'a+') as complaints_records:
                writer = csv.writer(complaints_records)
                writer.writerow(['No.', 'Date', 'From', 'Subject'])
                complaints_records.close()


            os.mkdir('Member Profile\\' + idval.get() + nameval.get()+'\Mails')
            with open('Member Profile\\' + idval.get() +  nameval.get()+'\Mails\LetterRecords.csv', 'a+') as letter_records:
                writer = csv.writer(letter_records)
                writer.writerow(['No.', 'Date', 'To', 'Subject'])
                letter_records.close()


            os.mkdir('Member Profile\\' + idval.get() + nameval.get()+'\Transanctions')
            with open('Member Profile\\' +  idval.get() + nameval.get()+'\Transanctions\Trans.csv', 'a+') as trans_records:
                writer = csv.writer(trans_records)
                writer.writerow(['No.', 'Date', 'Time', 'Amount'])
                trans_records.close()
            


            id_entry.delete(0, END)
            name_entry.delete(0, END)
            fname_entry.delete(0, END)
            mname_entry.delete(0, END)
            contact_entry.delete(0, END)
            email_entry.delete(0, END)
            profession_entry.delete(0, END)
            desig_entry.delete(0, END)
            payentry.delete(0, END)
            password_registry_entry.delete(0, END)

        except PermissionError:
            tkinter.messagebox.showinfo('Permission Error', 'Please close the database (csv) file ')


def delete():
        msg = tkinter.messagebox.askquestion('Sure?', 'Are you sure you want to remove the Member and all his/her details?')
        if msg == 'yes':
            remove()

        else:
            pass



def remove():
    try:
            #selected_item = database.selection()[0] ## get selected item
            # print(database.item(selected_item))
            # print(remove)
        selected_item = database.focus() ## get selected item

        database_pd = pd.read_csv('MemberRecords.csv')
        remove = database.item(selected_item)['values'][0]
        specify = database_pd.loc[database_pd['ID No'] == remove]
        id = specify.iloc[0, 0]
        name_remove = specify.iloc[0, 1]
        database_pd = database_pd.loc[database_pd['ID No'] != remove]
        database_pd.to_csv('MemberRecords.csv', index=0)

        database.delete(selected_item)
        with open('MemberRecords.csv', 'a+') as records:
            writer = csv.writer(records)

    except IndexError:
        tkinter.messagebox.showinfo('Error', 'Please choose a record')




def update_data():

    selected_item = database.focus() ## get selected item
            # print(database.item(selected_item))
    database_pd = pd.read_csv('MemberRecords.csv')
    remove = database.item(selected_item)['values'][0]
            # print(remove)
    database_pd = database_pd.loc[database_pd['ID No'] != remove]
    database_pd.to_csv('MemberRecords.csv', index=0)

    database.delete(selected_item)
    with open('MemberRecords.csv', 'a+') as records:
        writer = csv.writer(records)


    idval.set('abir')
    nameval.set('fds')
    fnameval.set('dfdf')
    mnameval.set('dfgdf')
    contactval.set('dfgdf')
    emailval.set('dfgdf')
    professionval.set('dfgdf')
    desigval.set('dfgdf')
    payval.set('dfgdf')


def raise_frame(frame):
    frame.tkraise()


def view_empl_details():

    def under_dev():
        tkinter.messagebox.showinfo('Under development','This feature is under development.\n Sorry for the incovenience')

    def update_view():
        database_csv = pd.read_csv('MemberRecords.csv')
        specific_row = database_csv.loc[database_csv['ID No'] == view_id]
        specific_row.iloc[0, 2] = fnameval.get()
        specific_row.iloc[0, 3] = mnameval.get()
        specific_row.iloc[0, 4] = contactval.get()
        specific_row.iloc[0, 5] = emailval.get()
        specific_row.iloc[0, 8] = payval.get()
        specific_row.iloc[0, 6] = professionval.get()
        specific_row.to_csv('MemberRecords.csv', index=0)

    def info_view():
        framex = Frame(frame2, bg='deepskyblue4')

        info_button = Button(framex, text='Member Profile', height=2, padx=5, command=info_view)
        info_button.place(x=50, y=20)
        complaint_button = Button(framex, text='Complaints', height=2, padx=5, command=complaint_view)
        complaint_button.place(x=150, y=20)
        letters_button = Button(framex, text='Letters and Mails', height=2, padx=5, command=letters_view)
        letters_button.place(x=250, y=20)
        leave_button = Button(framex, text='Attendence and Leave', height=2, padx=5)
        leave_button.place(x=350, y=20)
        payroll_button = Button(framex, text='Payroll and Trananctions', height=2, padx=5)
        payroll_button.place(x=450, y=20)

        frame4 = Frame(framex, borderwidth='10', relief=GROOVE, bg='white')

        fname_view = Label(frame4, text='Father\'s Name : ' , fg='black', bg='white', font=('Calibri', 14), padx=20, pady=10)
        fname_view.grid(row=0, column=0, sticky=W)

        mname_view = Label(frame4, text='Mother\'s Name : ' , fg='black', bg='white', font=('Calibri', 14), padx=20, pady=10)
        mname_view.grid(row=1, column=0, sticky=W)

        contact_view = Label(frame4, text='Contact : ' , fg='black', bg='white', font=('Calibri', 14), padx=20, pady=10)
        contact_view.grid(row=2, column=0, sticky=W)
    
        email_view = Label(frame4, text='Email Address : ', fg='black', bg='white', font=('Calibri', 14), padx=20, pady=10)
        email_view.grid(row=3, column=0, sticky=W)
    
        pay_view = Label(frame4, text='Pay : ' , fg='black', bg='white', font=('Calibri', 14), padx=20, pady=10)
        pay_view.grid(row=4, column=0, sticky=W)

        profession_view = Label(frame4, text='profession : ' , fg='black', bg='white', font=('Calibri', 14), padx=20, pady=10)
        profession_view.grid(row=5, column=0, sticky=W)

        fname_view_entry = Entry(frame4, textvariable=fnameval, width=30)
        fname_view_entry.grid(row=0, column=1)

        mname_view_entry = Entry(frame4, textvariable=mnameval, width=30)
        mname_view_entry.grid(row=1, column=1)

        contact_view_entry = Entry(frame4, textvariable=contactval, width=30)
        contact_view_entry.grid(row=2, column=1)

        email_view_entry = Entry(frame4, textvariable=emailval, width=30)
        email_view_entry.grid(row=3, column=1)

        pay_view_entry = Entry(frame4, textvariable=payval, width=30)
        pay_view_entry.grid(row=4, column=1)
    
        profession_view_entry = Entry(frame4, textvariable=professionval, width=30)
        profession_view_entry.grid(row=5, column=1)

        load()


        update_data_view = Button(frame4, text='Update', command=under_dev)
        update_data_view.grid(row=6, column=1, pady=50)

        frame4.pack(expand=1, fill=BOTH, padx=50, pady=90)
        framex.pack(fill=BOTH, expand=1)


    def complaint_view():
        framex = Frame(frame2, bg='deepskyblue4')
        
        info_button = Button(framex, text='Member Profile', height=2, padx=5, command=info_view)
        info_button.place(x=50, y=20)
        complaint_button = Button(framex, text='Complaints', height=2, padx=5, command=complaint_view)
        complaint_button.place(x=150, y=20)
        letters_button = Button(framex, text='Letters and Mails', height=2, padx=5, command=letters_view)
        letters_button.place(x=250, y=20)
        leave_button = Button(framex, text='Attendence and Leave', height=2, padx=5)
        leave_button.place(x=350, y=20)
        payroll_button = Button(framex, text='Payroll and Trananctions', height=2, padx=5)
        payroll_button.place(x=450, y=20)

        
        frame4 = Frame(framex, bg='deepskyblue4', borderwidth='10', relief=RIDGE)

        scrollbar = Scrollbar(frame4)
        scrollbar.pack(side=RIGHT, fill=Y)

        scrollbarh = Scrollbar(frame4, orient='horizontal')
        scrollbarh.pack(side=BOTTOM, fill=X)


        database = ttk.Treeview(frame4)

        database['columns'] = ['No', 'Date', 'From', 'Subject']
        database['show'] = 'headings'
        database.heading('No', text='No')
        database.heading('Date', text='Date')
        database.heading('From', text='From')
        database.heading('Subject', text='Subject')

        database.column('No', width=50)
        database.column('Date', width=100)
        database.column('From', width=100)
        database.column('Subject', width=200)

        database.pack(fill=BOTH, expand=1)

        # database.bind('<ButtonRelease-1>', cursor)

        scrollbar.config(command=database.yview)
        scrollbarh.config(command=database.xview)
        frame4.place(x=70, y=100, width=600, height=350)

        frame5 = Frame(frame2, bg='deepskyblue4', borderwidth='10', relief=RIDGE)
        scrollbar_details = Scrollbar(frame5)
        scrollbar_details.pack(side=RIGHT, fill=Y)

        complaint_details = Text(frame5)
        complaint_details.pack(fill=BOTH, expand=1)
        complaint_details.configure(state='disabled')


        scrollbar_details.config(command=complaint_details.yview)

        frame5.place(x=700, y=100, width=400, height=350)

        load_complaint = Button(frame2, text='Load Complaint', height=2, padx=5)
        load_complaint.place(x=1150, y=150)
        
        open_complaint = Button(frame2, text='Open Complaint', height=2, padx=5)
        open_complaint.place(x=1150, y=220)

        framex.pack()

        #frame3.pack(expand=1, fill=BOTH, padx=50, pady=50)

    def letters_view():
        framex = Frame(frame2, bg='deepskyblue4')

        frame4 = Frame(framex, bg='deepskyblue4', borderwidth='10', relief=RIDGE)
        info_button = Button(framex, text='Member Profile', height=2, padx=5, command=info_view)
        info_button.place(x=50, y=20)
        complaint_button = Button(framex, text='Complaints', height=2, padx=5, command=complaint_view)
        complaint_button.place(x=150, y=20)
        letters_button = Button(framex, text='Letters and Mails', height=2, padx=5, command=letters_view)
        letters_button.place(x=250, y=20)
        leave_button = Button(framex, text='Attendence and Leave', height=2, padx=5)
        leave_button.place(x=350, y=20)
        payroll_button = Button(framex, text='Payroll and Trananctions', height=2, padx=5)
        payroll_button.place(x=450, y=20)


        scrollbar = Scrollbar(frame4)
        scrollbar.pack(side=RIGHT, fill=Y)

        scrollbarh = Scrollbar(frame4, orient='horizontal')
        scrollbarh.pack(side=BOTTOM, fill=X)


        database = ttk.Treeview(frame4)

        database['columns'] = ['No', 'Date', 'To', 'Subject']
        database['show'] = 'headings'
        database.heading('No', text='No')
        database.heading('Date', text='Date')
        database.heading('To', text='To')
        database.heading('Subject', text='Subject')

        database.column('No', width=50)
        database.column('Date', width=100)
        database.column('To', width=100)
        database.column('Subject', width=200)

        database.pack(fill=BOTH, expand=1)

        # database.bind('<ButtonRelease-1>', cursor)

        scrollbar.config(command=database.yview)
        scrollbarh.config(command=database.xview)
        frame4.place(x=70, y=100, width=600, height=350)

        frame5 = Frame(frame2, bg='deepskyblue4', borderwidth='10', relief=RIDGE)
        scrollbar_details = Scrollbar(frame5)
        scrollbar_details.pack(side=RIGHT, fill=Y)

        complaint_details = Text(frame5)
        complaint_details.pack(fill=BOTH, expand=1)
        complaint_details.configure(state='disabled')


        scrollbar_details.config(command=complaint_details.yview)

        frame5.place(x=700, y=100, width=400, height=350)

        load_complaint = Button(frame2, text='Load Letter', height=2, padx=5)
        load_complaint.place(x=1150, y=150)
        
        open_complaint = Button(frame2, text='Open Letter', height=2, padx=5)
        open_complaint.place(x=1150, y=220)
        framex.pack()

    def leave_view():
        pass

    def Transanctions_view():
        pass



    selected_item = database.focus() ## get selected item

    view_id = database.item(selected_item)['values'][0]
    view_name = database.item(selected_item)['values'][1]
    view_post = database.item(selected_item)['values'][7]    

    parent_view = Toplevel()

    parent_view.geometry('1000x550')
    parent_view.title('Retail Management System')
#   root.minsize(460, 540)
#   root.maxsize(460, 540)

    frame1 = Frame(parent_view, borderwidth='5', relief=RIDGE, bg='deepskyblue4')
    inframe1 = Frame(frame1, borderwidth='1', bg='deepskyblue4')
    
    identity = Label(inframe1, text=view_name , fg='white', bg='deepskyblue4', font=('Copperplate gothic bold', 17), padx=40)
    identity.grid(row=1, column=0)
    

    idno = Label(inframe1, text='ID : '+str(view_id) , fg='white', bg='deepskyblue4', font=('Copperplate gothic bold', 15), padx=40)
    idno.grid(row=0, column=0, sticky=W)
    

    post = Label(inframe1, text=view_post , fg='white', bg='deepskyblue4', font=('Copperplate gothic bold', 12), padx=40)
    post.grid(row=2, column=0, sticky=W)

    inframe1.pack(fill=X, expand=1, pady=15, padx=40)
    frame1.pack(fill=X)

    frame2 = Frame(parent_view, borderwidth='3', relief=RIDGE, bg='deepskyblue4')
    
    ''' THE SWITCHING PART OF THE PROGRAM '''

    info_button = Button(frame2, text='Member Profile', height=2, padx=5, command=info_view)
    info_button.place(x=50, y=20)
    complaint_button = Button(frame2, text='Complaints', height=2, padx=5, command=complaint_view)
    complaint_button.place(x=150, y=20)
    letters_button = Button(frame2, text='Letters and Mails', height=2, padx=5, command=letters_view)
    letters_button.place(x=250, y=20)
    leave_button = Button(frame2, text='Attendence and Leave', height=2, padx=5)
    leave_button.place(x=350, y=20)
    payroll_button = Button(frame2, text='Payroll and Trananctions', height=2, padx=5)
    payroll_button.place(x=450, y=20)
    

    frame2.pack(fill=BOTH, expand=1)


    parent_view.mainloop()

    






root = Tk()

root.geometry('1000x550')
root.title('Retail Management System')
# root.minsize(460, 540)
# root.maxsize(460, 540)

frame1 = Frame(root, borderwidth='10', relief=RIDGE, bg='deepskyblue4')
title = Label(frame1, text='Retail Management System', fg='white', bg='deepskyblue4', pady='20',
              font=('Copperplate Gothic Bold', 20, 'bold'))

title.pack()
frame1.pack(fill=X)

frame2 = Frame(root, borderwidth='10', relief=RIDGE, bg='deepskyblue4')
form_text = Label(frame2, text='Fill up the following form for recruiting Member ', fg='white', bg='deepskyblue4',
                  pady='20', padx='5', font=('Calibri', 15, 'bold'))
form_text.grid()

id = Label(frame2, text='ID No : ', fg='white', bg='deepskyblue4', font=(10))
id.grid(row=1, column=0, stick=W, padx=20)

name = Label(frame2, text='Name : ', fg='white', bg='deepskyblue4', font=(10))
name.grid(row=2, column=0, stick=W, padx=20)

fname = Label(frame2, text='Fathers Name : ', fg='white', bg='deepskyblue4', font=(10))
fname.grid(row=3, column=0, stick=W, padx=20)

mname = Label(frame2, text='Mothers Name : ', fg='white', bg='deepskyblue4', font=(10))
mname.grid(row=4, column=0, stick=W, padx=20)

contact = Label(frame2, text='Contact : ', fg='white', bg='deepskyblue4', font=(10))
contact.grid(row=5, column=0, stick=W, padx=20)

email = Label(frame2, text='Email Address : ', fg='white', bg='deepskyblue4', font=(10))
email.grid(row=6, column=0, stick=W, padx=20)

profession = Label(frame2, text='profession : ', fg='white', bg='deepskyblue4', font=(10))
profession.grid(row=7, column=0, stick=W, padx=20)

desig = Label(frame2, text='Designation : ', fg='white', bg='deepskyblue4', font=(10))
desig.grid(row=8, column=0, stick=W, padx=20)

pay = Label(frame2, text='Pay : ', fg='white', bg='deepskyblue4', font=(10))
pay.grid(row=9, column=0, stick=W, padx=20)

password_registry = Label(frame2, text='Password : ', fg='white', bg='deepskyblue4', font=(10))
password_registry.grid(row=10, column=0, stick=W, padx=20)

submit = Button(frame2, text='Submit', command=submit_value)
submit.place(x=175, y=360)

del_data = Button(frame2, text='Delete', command=delete)
del_data.place(x=115, y=400)


update = Button(frame2, text='Update')
update.place(x=175, y=400)

view_details = Button(frame2, text='View Details', command=view_empl_details)
view_details.place(x=235, y=400)





idval, nameval, fnameval, mnameval, contactval, emailval, professionval, desigval, payval = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
searchval = StringVar()
password_registryval = StringVar()

id_entry = Entry(frame2, textvariable=idval)
id_entry.place(x=150, y=69)

name_entry = Entry(frame2, textvariable=nameval)
name_entry.place(x=150, y=93)

fname_entry = Entry(frame2, textvariable=fnameval)
fname_entry.place(x=150, y=117)

mname_entry = Entry(frame2, textvariable=mnameval)
mname_entry.place(x=150, y=142)

contact_entry = Entry(frame2, textvariable=contactval)
contact_entry.place(x=150, y=167)

email_entry = Entry(frame2, textvariable=emailval)
email_entry.place(x=150, y=191)

profession_entry = Entry(frame2, textvariable=professionval)
profession_entry.place(x=150, y=215)

desig_entry = Entry(frame2, textvariable=desigval)
desig_entry.place(x=150, y=239)

payentry = Entry(frame2, textvariable=payval)
payentry.place(x=150, y=263)

password_registry_entry = Entry(frame2, textvariable=password_registryval)
password_registry_entry.place(x=150, y=288)


frame2.pack(side=LEFT, fill=BOTH)

frame3 = Frame(root, bg='deepskyblue4', borderwidth='10', relief=RIDGE)
text3 = Label(frame3, text='Search ID : ', bg='deepskyblue4', fg='white', padx=40, pady=20, font=('Calibri', 12, 'bold'))
text3.grid(row=0, column=0, sticky='w')

search = ttk.Combobox(frame3, values=
[
    'Name',
    'ID',
    'Contact',
    
], 
textvariable=searchval)
search.grid(row=0, column=1)

search_button = Button(frame3, text='Search')
search_button.grid(row=0, column=3, padx=10)

load_button = Button(frame3, text='Load record', command=load)
load_button.grid(row=0, column=4)


frame4 = Frame(frame3, bg='deepskyblue4', borderwidth='10', relief=RIDGE)



scrollbar = Scrollbar(frame4)
scrollbar.pack(side=RIGHT, fill=Y)

scrollbarh = Scrollbar(frame4, orient='horizontal')
scrollbarh.pack(side=BOTTOM, fill=X)

tuples = ['test']

database = ttk.Treeview(frame4)

database['columns'] = ['ID No', 'Name', 'Fathers Name', 'Mothers Name', 'Contact', 'Email', 'profession', 'Designation', 'Pay']
database['show'] = 'headings'
database.heading('ID No', text='ID No')
database.heading('Name', text='Name')
database.heading('Fathers Name', text='Fathers Name')
database.heading('Mothers Name', text='Mothers Name')
database.heading('Contact', text='Contact')
database.heading('Email', text='Email')
database.heading('profession', text='profession')
database.heading('Designation', text='Designation')
database.heading('Pay', text='Pay')

database.column('ID No', width=100)
database.column('Name',  width=100)
database.column('Fathers Name', width=100)
database.column('Mothers Name', width=100)
database.column('Contact', width=100)
database.column('Email', width=100)
database.column('profession', width=100)
database.column('Designation', width=100)
database.column('Pay', width=100)

database.pack(fill=BOTH, expand=1)



scrollbar.config(command=database.yview)
scrollbarh.config(command=database.xview)



try:
    with open('MemberRecords.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            id = row['ID No']
            namevalcsv = row['Name']
            fnamevalcsv = row['Fathers Name']
            mnamealcsv = row['Mothers Name']
            contactvalcsv= row['Contact']
            emailvalcsv = row['Email']
            professionvalcsv = row['profession']
            desigvalcsv = row['Designation']
            payvalcsv = row['Pay']

            database.insert("", END, values=(id, namevalcsv, fnamevalcsv, mnamealcsv, contactvalcsv,
             emailvalcsv, professionvalcsv, desigvalcsv, payvalcsv))

except FileNotFoundError:
    with open('MemberRecords.csv', 'a+') as records:
        writer = csv.writer(records)
        writer.writerow(
            ['ID No', 'Name', 'Fathers Name', 'Mothers Name', 'Contact', 'Email', 'profession', 'Designation', 'Pay'
             ])
    records.close()





frame4.place(x=50, y=100, width=700, height=300)
#frame3.place(x=453, y=96, height=560, width=826)
frame3.pack(fill=BOTH, expand=1)




root.mainloop()