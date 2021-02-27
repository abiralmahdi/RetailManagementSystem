from tkinter import *
from tkinter import ttk
import pandas as pd
import csv
import sys
import datetime
import schedule
import tkinter.messagebox
from datetime import date

def calc_capital():
    empl_data = pd.read_csv('EmployeeRecords.csv')
    salary = empl_data['Pay'].sum()
    empval.set(salary)
    
    supply_data = pd.read_csv('SupplyRecords.csv')
    whole_sale = supply_data['Total Cost'].sum()
    wholesaleval.set(whole_sale)

    capitalval.set(investval.get()-(elecval.get()+ empval.get()+rentval.get()+taxval.get()+wholesaleval.get()))


def update_data():
    selected_item = database.focus()  ## get selected item
    print(selected_item)
    print(selected_item[1::])
    hex = selected_item[1::]
    dec = int(hex)
    idx = dec - 1
    database.delete(selected_item)

    database_pd = pd.read_csv('FinanceRecords.csv')

    database_pd.iloc[idx, 0] = noval.get()
    database_pd.iloc[idx, 1] = monthval.get()
    database_pd.iloc[idx, 2] = investval.get()
    database_pd.iloc[idx, 3] = elecval.get()
    database_pd.iloc[idx, 4] = empval.get()
    database_pd.iloc[idx, 5] = rentval.get()
    database_pd.iloc[idx, 6] = taxval.get()
    database_pd.iloc[idx, 7] = wholesaleval.get()
    database_pd.iloc[idx, 8] = capitalval.get()
    database_pd.to_csv('FinanceRecords.csv', index=0)

    database.insert("", idx, values=(database_pd.iloc[idx, 0],
                                     database_pd.iloc[idx, 1],
                                     database_pd.iloc[idx, 2],
                                     database_pd.iloc[idx, 3],
                                     database_pd.iloc[idx, 4],
                                     database_pd.iloc[idx, 5],
                                     database_pd.iloc[idx, 6],
                                     database_pd.iloc[idx, 7],
                                     database_pd.iloc[idx, 8]))

    no_entry.delete(0, END)
    month_entry.delete(0, END)
    invest_entry.delete(0, END)
    elec_entry.delete(0, END)
    emp_entry.delete(0, END)
    rent_entry.delete(0, END)
    tax_entry.delete(0, END)
    wholesale_entry.delete(0, END)
    capitalentry.delete(0, END)


def delete():
    pass
    #global sure_root
    #sure_root = Toplevel()
    #sure_root.title('Remove Employee')
    #sure_root.geometry('400x100')
    #sure_root.maxsize(400, 100)
    #sure_root.minsize(400, 100)

    #warning = Label(sure_root, text='Are you sure you want to remove this Employee? ')
    #remove_button = Button(sure_root, text='Remove', pady=20, command=remove, width=7)
    #warning.pack()
    #remove_button.pack()

    #sure_root.mainloop()



def remove():
    try:

        selected_item = database.focus()  ## get selected item

        database_pd = pd.read_csv('FinanceRecords.csv')
        remove = database.item(selected_item)['values'][0]

        tkinter.messagebox.askyesno('Sure?', 'Are you sure you want to remove the record?')

        database_pd = database_pd.loc[database_pd['No'] != remove]
        database_pd.to_csv('FinanceRecords.csv', index=0)

        database.delete(selected_item)
        with open('FinanceRecords.csv', 'a+') as records:
            writer = csv.writer(records)

        no_entry.delete(0, END)
        month_entry.delete(0, END)
        invest_entry.delete(0, END)
        elec_entry.delete(0, END)
        emp_entry.delete(0, END)
        rent_entry.delete(0, END)
        tax_entry.delete(0, END)
        wholesale_entry.delete(0, END)
        capitalentry.delete(0, END)


    except IndexError:
        tkinter.messagebox.showinfo('Error', 'Please select a record')


def submit_value():
    if noval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form')
    elif noval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form')
    elif monthval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form')
    elif investval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form')
    elif elecval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form')
    elif empval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form')
    elif rentval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form')
    elif taxval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form')
    elif wholesaleval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form')
    elif capitalval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form')

    else:
        try:
            with open('FinanceRecords.csv', 'a+') as records:
                writer = csv.writer(records)
                writer.writerow(
                    [noval.get(), monthval.get(), investval.get(), elecval.get(), empval.get(), rentval.get(),
                     taxval.get(), wholesaleval.get(), capitalval.get()])
                records.close()

            with open('FinanceRecords.csv') as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    id = row['No']
                    monthvalcsv = row['Month']
                    investvalcsv = row['Invest']
                    elecalcsv = row['Electricity']
                    empvalcsv = row['Employee']
                    rentvalcsv = row['Rent']
                    taxvalcsv = row['Tax']
                    wholesalevalcsv = row['Wholesale Cost']
                    capitalvalcsv = row['Capital']

            database.insert("", END, values=(id, monthvalcsv, investvalcsv, elecalcsv, empvalcsv,
                                             rentvalcsv, taxvalcsv, wholesalevalcsv, capitalvalcsv))

            no_entry.delete(0, END)
            month_entry.delete(0, END)
            invest_entry.delete(0, END)
            elec_entry.delete(0, END)
            emp_entry.delete(0, END)
            rent_entry.delete(0, END)
            tax_entry.delete(0, END)
            wholesale_entry.delete(0, END)
            capitalentry.delete(0, END)

        except PermissionError:
            tkinter.messagebox.showinfo('Permission Error', 'Please close the database (csv) file ')


def cursor():
    try:
        selected_item = database.focus()  ## get selected item
        print(selected_item)
        # print(selected_item[])
        noval.set(database.item(selected_item)['values'][0])
        monthval.set(database.item(selected_item)['values'][1])
        investval.set(database.item(selected_item)['values'][2])
        elecval.set(database.item(selected_item)['values'][3])
        empval.set(database.item(selected_item)['values'][4])
        rentval.set(database.item(selected_item)['values'][5])
        taxval.set(database.item(selected_item)['values'][6])
        wholesaleval.set(database.item(selected_item)['values'][7])
        capitalval.set(database.item(selected_item)['values'][8])

    except IndexError:
        tkinter.messagebox.showinfo('Error', 'Please select one record')



def automation():
    database_pd1 = pd.read_csv('FinanceRecords.csv')
    database_pd = database_pd1.tail(1)

    a = database_pd.iloc[0, 0]
    b = database_pd.iloc[0, 1]
    print(b)
    c = database_pd.iloc[0, 8]
    d = database_pd.iloc[0, 3]
    e = database_pd.iloc[0, 4]
    f = database_pd.iloc[0, 5]
    g = database_pd.iloc[0, 6]
    h = database_pd.iloc[0, 7]
    i = c-(d+e+f+g+h)

    try:
        with open('FinanceRecords.csv', 'a+') as records:
            writer = csv.writer(records)
            writer.writerow(
                [a, b, c, d, e, f, g, h, i])
            records.close()

        with open('FinanceRecords.csv', 'r') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                id = row['No']
                monthvalcsv = row['Month']
                investvalcsv = row['Invest']
                elecalcsv = row['Electricity']
                empvalcsv = row['Employee']
                rentvalcsv = row['Rent']
                taxvalcsv = row['Tax']
                wholesalevalcsv = row['Wholesale Cost']
                capitalvalcsv = row['Capital']

        database.insert("", END, values=(id, monthvalcsv, investvalcsv, elecalcsv, empvalcsv,
                                         rentvalcsv, taxvalcsv, wholesalevalcsv, capitalvalcsv))


    except PermissionError:
        tkinter.messagebox.showinfo('Permission Error', 'Please close the database (csv) file ')




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
form_text = Label(frame2, text='Fill up the following form for adding transaction ', fg='white', bg='deepskyblue4',
                  pady='20', padx='5', font=('Calibri', 15, 'bold'))
form_text.grid()

id = Label(frame2, text='No : ', fg='white', bg='deepskyblue4', font=(10))
id.grid(row=1, column=0, stick=W, padx=20)

month = Label(frame2, text='Month : ', fg='white', bg='deepskyblue4', font=(10))
month.grid(row=2, column=0, stick=W, padx=20)

invest = Label(frame2, text='Invest : ', fg='white', bg='deepskyblue4', font=(10))
invest.grid(row=3, column=0, stick=W, padx=20)

elec = Label(frame2, text='Electricity Bill : ', fg='white', bg='deepskyblue4', font=(10))
elec.grid(row=4, column=0, stick=W, padx=20)

emp = Label(frame2, text='Employee Salary : ', fg='white', bg='deepskyblue4', font=(10))
emp.grid(row=7, column=0, stick=W, padx=20)

rent = Label(frame2, text='Rent : ', fg='white', bg='deepskyblue4', font=(10))
rent.grid(row=6, column=0, stick=W, padx=20)

tax = Label(frame2, text='Tax : ', fg='white', bg='deepskyblue4', font=(10))
tax.grid(row=5, column=0, stick=W, padx=20)

wholesale = Label(frame2, text='Wholesale Cost : ', fg='white', bg='deepskyblue4', font=(10))
wholesale.grid(row=8, column=0, stick=W, padx=20)

capital = Label(frame2, text='Capital : ', fg='white', bg='deepskyblue4', font=(10))
capital.grid(row=9, column=0, stick=W, padx=20)

submit = Button(frame2, text='Submit', command=submit_value)
submit.place(x=105, y=330)

del_data = Button(frame2, text='Delete', command=remove)
del_data.place(x=165, y=330)

update = Button(frame2, text='Update [Under Development]')
update.place(x=225, y=330)

calc_button = Button(frame2, text='Calculate other data', command=calc_capital)
calc_button.place(x=120, y=370)

noval, monthval, investval, elecval, empval, rentval, taxval, wholesaleval, capitalval = StringVar(), StringVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()

no_entry = Entry(frame2, textvariable=noval)
no_entry.place(x=150, y=69)

month_entry = Entry(frame2, textvariable=monthval)
month_entry.place(x=150, y=93)
monthval.set(datetime.date.today().strftime('%b'))

invest_entry = Entry(frame2, textvariable=investval)
invest_entry.place(x=150, y=117)

elec_entry = Entry(frame2, textvariable=elecval)
elec_entry.place(x=150, y=142)

emp_entry = Entry(frame2, textvariable=empval)
emp_entry.place(x=150, y=215)

rent_entry = Entry(frame2, textvariable=rentval)
rent_entry.place(x=150, y=191)

tax_entry = Entry(frame2, textvariable=taxval)
tax_entry.place(x=150, y=167)

wholesale_entry = Entry(frame2, textvariable=wholesaleval)
wholesale_entry.place(x=150, y=239)

capitalentry = Entry(frame2, textvariable=capitalval)
capitalentry.place(x=150, y=263)

frame2.pack(side=LEFT, fill=BOTH)

frame2.pack(side=LEFT, fill=BOTH)

frame3 = Frame(root, bg='deepskyblue4', borderwidth='10', relief=RIDGE)
text3 = Label(frame3, text='Search ID : ', bg='deepskyblue4', fg='white', padx=40, pady=20,
              font=('Calibri', 12, 'bold'))
text3.grid(row=0, column=0, sticky='w')

search = Entry(frame3)
search.grid(row=0, column=1)

search_button = Button(frame3, text='Search')
search_button.grid(row=0, column=3, padx=20)

frame4 = Frame(frame3, bg='deepskyblue4', borderwidth='10', relief=RIDGE)

scrollbar = Scrollbar(frame4)
scrollbar.pack(side=RIGHT, fill=Y)

scrollbarh = Scrollbar(frame4, orient='horizontal')
scrollbarh.pack(side=BOTTOM, fill=X)

tuples = ['test']

database = ttk.Treeview(frame4)

database['columns'] = ['No', 'Month', 'Invest', 'Electricity', 'Employee', 'Rent', 'Tax',
                       'Wholesale Cost', 'Capital']
database['show'] = 'headings'
database.heading('No', text='No')
database.heading('Month', text='Month')
database.heading('Invest', text='Invest')
database.heading('Electricity', text='Electricity')
database.heading('Employee', text='Employee')
database.heading('Rent', text='Rent')
database.heading('Tax', text='Tax')
database.heading('Wholesale Cost', text='Wholesale Cost')
database.heading('Capital', text='Capital')

database.column('No', width=100)
database.column('Month', width=100)
database.column('Invest', width=100)
database.column('Electricity', width=100)
database.column('Employee', width=100)
database.column('Rent', width=100)
database.column('Tax', width=100)
database.column('Wholesale Cost', width=100)
database.column('Capital', width=100)

database.pack(fill=BOTH, expand=1)

# database.bind('<ButtonRelease-1>', cursor)

scrollbar.config(command=database.yview)
scrollbarh.config(command=database.xview)

try:
    with open('FinanceRecords.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            id = row['No']
            monthvalcsv = row['Month']
            investvalcsv = row['Invest']
            elecalcsv = row['Electricity']
            empvalcsv = row['Employee']
            rentvalcsv = row['Rent']
            taxvalcsv = row['Tax']
            wholesalevalcsv = row['Wholesale Cost']
            capitalvalcsv = row['Capital']

            database.insert("", END, values=(id, monthvalcsv, investvalcsv, elecalcsv, empvalcsv,
                                             rentvalcsv, taxvalcsv, wholesalevalcsv, capitalvalcsv))



except FileNotFoundError:
    with open('FinanceRecords.csv', 'a+') as records:
        writer = csv.writer(records)
        writer.writerow(
            ['No', 'Month', 'Invest', 'Electricity', 'Employee', 'Rent', 'Tax', 'Wholesale Cost', 'Capital'
             ])
    records.close()


load = Button(frame3, text='Load Data', command=cursor)
load.grid(row=3, column=0)

frame4.place(x=50, y=100, width=700, height=300)
#frame3.place(x=453, y=96, height=560, width=826, fill=X, expand=1)
frame3.pack(fill=BOTH, expand=1)

if date.today().day == 28:
    schedule.every().day.at('17:00').do(automation) 

else:
    pass

while 1:
    schedule.run_pending()
    root.mainloop()


#else:
 #   pass


