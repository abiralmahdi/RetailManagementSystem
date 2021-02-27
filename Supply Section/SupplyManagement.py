from tkinter import *
from tkinter import ttk
import pandas as pd
import csv, sys
import tkinter.messagebox



def update_data():
    selected_item = database.focus()  ## get selected item
    print(selected_item)
    print(selected_item[1::])
    hex = selected_item[1::]
    dec = int(hex)
    idx = dec - 1
    database.delete(selected_item)

    database_pd = pd.read_csv('SupplyRecords.csv')

    database_pd.iloc[idx, 0] = idval.get()
    database_pd.iloc[idx, 1] = nameval.get()
    database_pd.iloc[idx, 2] = catval.get()
    database_pd.iloc[idx, 3] = costval.get()
    database_pd.iloc[idx, 4] = qtyval.get()
    database_pd.iloc[idx, 5] = qtyval.get() * costval.get()
    database_pd.to_csv('SupplyRecords.csv', index=0)

    database.insert("", idx, values=(database_pd.iloc[idx, 0],
                                     database_pd.iloc[idx, 1],
                                     database_pd.iloc[idx, 2],
                                     database_pd.iloc[idx, 3],
                                     database_pd.iloc[idx, 4],
                                     database_pd.iloc[idx, 5]
                                     ))

    id_entry.delete(0, END)
    name_entry.delete(0, END)
    cat_entry.delete(0, END)
    cost_entry.delete(0, END)
    qty_entry.delete(0, END)


def delete():
    global sure_root
    sure_root = Toplevel()
    sure_root.title('Remove Employee')
    sure_root.geometry('400x100')
    sure_root.maxsize(400, 100)
    sure_root.minsize(400, 100)

    warning = Label(sure_root, text='Are you sure you want to remove this Product? ')
    remove_button = Button(sure_root, text='Remove', pady=20, command=remove, width=7)
    warning.pack()
    remove_button.pack()

    sure_root.mainloop()


def remove():
    try:
        selected_item = database.focus()  ## get selected item

        database_pd = pd.read_csv('SupplyRecords.csv')
        remove = database.item(selected_item)['values'][0]

        database_pd = database_pd.loc[database_pd['ID No'] != remove]
        database_pd.to_csv('SupplyRecords.csv', index=0)

        database.delete(selected_item)
        with open('SupplyRecords.csv', 'a+') as records:
            writer = csv.writer(records)

        id_entry.delete(0, END)
        name_entry.delete(0, END)
        cat_entry.delete(0, END)
        cost_entry.delete(0, END)
        qty_entry.delete(0, END)

        sure_root.destroy()

    except IndexError:
        index_root = Toplevel()
        index_root.title('Selection Error')
        index_root.geometry('400x100')
        index_root.maxsize(400, 100)
        index_root.minsize(400, 100)

        warnings = Label(index_root, text='Please select a record first! ')
        warnings.pack()

        index_root.mainloop()


def submit_value():
    # costval = IntVar()
    # qtyval = IntVar()

    if idval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form')
    elif nameval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form')
    elif catval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form')
    elif costval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form')
    elif qtyval.get() == '':
        tkinter.messagebox.showinfo('Error', 'Please fill up the full form')

    else:
        try:
            with open('SupplyRecords.csv', 'a+') as records:
                writer = csv.writer(records)
                writer.writerow(
                    [idval.get(), nameval.get(), catval.get(), costval.get(), qtyval.get(),
                     qtyval.get() * costval.get()])
                records.close()

            with open('SupplyRecords.csv') as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    id = row['ID No']
                    namevalcsv = row['Name']
                    catvalcsv = row['Category']
                    costval = row['Cost']
                    qtyval = row['Quantity']
                    totcost = row['Total Cost']

            database.insert("", END, values=(id, namevalcsv, catvalcsv, costval, qtyval, totcost))

            id_entry.delete(0, END)
            name_entry.delete(0, END)
            cat_entry.delete(0, END)
            cost_entry.delete(0, END)
            qty_entry.delete(0, END)

        except PermissionError:
            tkinter.messagebox.showinfo('Permission Error', 'Please close the database (csv) file ')

        # except TclError:
        #   tkinter.messagebox.showinfo('Value Error', 'Please use integer numbers in the specific entry fields.')



def cursor():
    try:
        selected_item = database.focus()  ## get selected item
        print(selected_item)
        # print(selected_item[])
        idval.set(database.item(selected_item)['values'][0])
        nameval.set(database.item(selected_item)['values'][1])
        catval.set(database.item(selected_item)['values'][2])
        costval.set(database.item(selected_item)['values'][3])
        qtyval.set(database.item(selected_item)['values'][4])

    except IndexError:
        tkinter.messagebox.showinfo('Error', 'Please select one record')


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
form_text = Label(frame2, text='Fill up the following form for adding supplies ', fg='white', bg='deepskyblue4',
                  pady='20', padx='5', font=('Calibri', 15, 'bold'))
form_text.grid()

id = Label(frame2, text='ID No : ', fg='white', bg='deepskyblue4', font=(10))
id.grid(row=1, column=0, stick=W, padx=20)

name = Label(frame2, text='Name : ', fg='white', bg='deepskyblue4', font=(10))
name.grid(row=2, column=0, stick=W, padx=20)

cat = Label(frame2, text='Category : ', fg='white', bg='deepskyblue4', font=(10))
cat.grid(row=3, column=0, stick=W, padx=20)

cost = Label(frame2, text='Cost : ', fg='white', bg='deepskyblue4', font=(10))
cost.grid(row=4, column=0, stick=W, padx=20)

qty = Label(frame2, text='Quantity : ', fg='white', bg='deepskyblue4', font=(10))
qty.grid(row=5, column=0, stick=W, padx=20)

idval, nameval, catval, = StringVar(), StringVar(), StringVar()
costval = IntVar()
qtyval = IntVar()

# totcost = qtyval.get()*costval.get()


id_entry = Entry(frame2, textvariable=idval)
id_entry.place(x=150, y=69)

name_entry = Entry(frame2, textvariable=nameval)
name_entry.place(x=150, y=93)

cat_entry = ttk.Combobox(frame2, values=
[
    'Grocery',
    'Fast Food',
    'Clothes',
    'Electronics',
    'Souvenir',
],
                         textvariable=catval
                         )

cat_entry.place(x=150, y=117)

cost_entry = Entry(frame2, textvariable=costval)
cost_entry.place(x=150, y=142)

qty_entry = Entry(frame2, textvariable=qtyval)
qty_entry.place(x=150, y=167)

submit = Button(frame2, text='Submit', command=submit_value)
submit.place(x=105, y=330)

del_data = Button(frame2, text='Delete', command=delete)
del_data.place(x=165, y=330)

update = Button(frame2, text='Update [Under Development]')
update.place(x=225, y=330)

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

database['columns'] = ['ID No', 'Name', 'Category', 'Cost', 'Quantity', 'Total Cost']

database['show'] = 'headings'
database.heading('ID No', text='ID No')
database.heading('Name', text='Name')
database.heading('Category', text='Category')
database.heading('Cost', text='Cost')
database.heading('Quantity', text='Quantity')
database.heading('Total Cost', text='Total Cost')

database.column('ID No', width=100)
database.column('Name', width=100)
database.column('Name', width=100)
database.column('Cost', width=100)
database.column('Quantity', width=100)
database.column('Total Cost', width=100)

database.pack(fill=BOTH, expand=1)

# database.bind('<ButtonRelease-1>', cursor)

scrollbar.config(command=database.yview)
scrollbarh.config(command=database.xview)

try:
    with open('SupplyRecords.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            id = row['ID No']
            namevalcsv = row['Name']
            catvalcsv = row['Category']
            costvalcsv = row['Cost']
            qtyvalcsv = row['Quantity']
            totcostcsv = row['Total Cost']
            database.insert("", END, values=(id, namevalcsv, catvalcsv, costvalcsv, qtyvalcsv, totcostcsv))



except FileNotFoundError:
    with open('SupplyRecords.csv', 'a+') as records:
        writer = csv.writer(records)
        writer.writerow(
            ['ID No', 'Name', 'Category', 'Cost', 'Quantity', 'Total Cost'
             ])
    records.close()

load = Button(frame3, text='Load Data', command=cursor)
load.grid(row=3, column=0)

frame4.place(x=50, y=100, width=700, height=300)
frame3.place(x=416, y=94, height=563, width=862)


def empl():
    pass


def supl():
    pass


def fin():
    pass


def acc():
    pass


def logout():
    pass


menubar = Menu(root)

mainmenu = Menu(menubar, tearoff=0)
mainmenu.add_command(label='Employee Section', command=empl)
mainmenu.add_command(label='Supply Section', command=supl)
mainmenu.add_command(label='Finance Section', command=fin)
menubar.add_cascade(label='Main Menu', menu=mainmenu)

accounts = Menu(menubar, tearoff=0)
accounts.add_command(label='Account Details', command=acc)
accounts.add_command(label='Log Out', command=logout)
menubar.add_cascade(label='Manage Account', menu=accounts)

root.config(menu=menubar)
root.mainloop()
