from tkinter import *
from tkinter import ttk
import pandas as pd
import csv, sys

root = Tk()

tree = ttk.Treeview(root)

tree['columns'] = ['Name', 'Email', 'Contact']

tree['show'] = 'headings'
tree.heading('Name', text='Name')
tree.heading('Email', text='Email')
tree.heading('Contact', text='Contact')

tree.pack()

with open('test.csv', 'a+') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Email', 'Contact'])
    writer.writerow(['Abir', 'abir', '123'])
    writer.writerow(['ABC', 'abc', '433'])
f.close()

read = pd.read_csv('test.csv')
#print(read)



root.mainloop()


