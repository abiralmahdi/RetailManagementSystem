
from tkinter import *
from tkinter import ttk


root=Tk()

treeview = ttk.Treeview(root)


# set up the columns and headings
# In reality "Member ID" would be exported from the database
treeview["columns"] = ["Member ID", "Full Name"]
treeview["show"] = "headings"
treeview.heading("Member ID", text="Member ID")
treeview.heading("Full Name", text="Full Name")

# Add content using (where index is the position/row of the treeview)
# iid is the item index (used to access a specific element in the treeview)
# you can set iid to be equal to the index


tuples = [(1, "Name1"), (2, "Name2"), (3, 'Abir')]

for i in range(3):
    no = int(input('no : '))
    inpt = input('Enter name : ')
    tuples.append((no, inpt))

index = iid = 0
for row in tuples:
    treeview.insert("", index, iid, values=row)
    index = iid = index + 1

treeview.pack()

root.mainloop()